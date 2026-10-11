#!/usr/bin/env python3
"""Exercise an offline, synthetic Git worktree workflow in a fresh directory."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


BASE_CODE = """def normalize_limit(value):
    return int(value)


def describe_limit(value):
    return f"limit={normalize_limit(value)}"
"""

VALIDATED_CODE = """def normalize_limit(value):
    result = int(value)
    if result < 0:
        raise ValueError("limit must not be negative")
    return result


def describe_limit(value):
    return f"limit={normalize_limit(value)}"
"""

BASE_TESTS = """import unittest
from budget import describe_limit, normalize_limit


class BudgetTests(unittest.TestCase):
    def test_string_count(self):
        self.assertEqual(normalize_limit("3"), 3)

    def test_label(self):
        self.assertEqual(describe_limit(0), "limit=0")
"""

EXTRA_TEST = """
    def test_negative_count(self):
        with self.assertRaises(ValueError):
            normalize_limit(-1)
"""

BASE_README = "# Synthetic fixture\n\nparallel-owner: unset\n"
DOCS_README = BASE_README + "\nUsage: pass a non-negative whole-number count.\n"


class Fixture:
    def __init__(self, root):
        self.root = root
        self.commands = []
        self.checks = []
        self.git = shutil.which("git")
        if not self.git:
            raise RuntimeError("Git is required; no package is installed by this script")
        home = root / "isolated-home"
        home.mkdir()
        self.env = {
            "PATH": os.defpath,
            "HOME": str(home),
            "LC_ALL": "C",
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_SYSTEM": os.devnull,
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_MERGE_AUTOEDIT": "no",
            "PYTHONDONTWRITEBYTECODE": "1",
        }

    def run(self, directory, *args, expected=0):
        command = [self.git, *args]
        result = subprocess.run(
            command, cwd=directory, env=self.env, capture_output=True,
            text=True, timeout=30,
        )
        self.commands.append({
            "cwd": str(directory.relative_to(self.root)),
            "command": ["git", *args],
            "exit": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        })
        if expected is None:
            if result.returncode == 0:
                raise AssertionError(f"Expected refusal: {args}")
        elif result.returncode != expected:
            raise AssertionError(f"Failed {args}: {result.stderr}")
        return result

    def tests(self, directory, expected_count):
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-v"],
            cwd=directory, env=self.env, capture_output=True,
            text=True, timeout=30,
        )
        self.commands.append({
            "cwd": str(directory.relative_to(self.root)),
            "command": ["python3", "-m", "unittest", "discover", "-v"],
            "exit": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        })
        assert result.returncode == 0, result.stderr
        assert f"Ran {expected_count} tests" in result.stderr, result.stderr

    def put(self, directory, name, content):
        (directory / name).write_text(content, encoding="utf-8")

    def check(self, name, condition):
        if not condition:
            raise AssertionError(name)
        self.checks.append({"name": name, "passed": True})

    def clean(self, directory):
        self.check(
            f"clean:{directory.name}",
            self.run(directory, "status", "--porcelain=v1", "--untracked-files=all", "--ignored").stdout == "",
        )

    def commit(self, directory, message, *files):
        self.run(directory, "diff", "--check")
        self.run(directory, "add", "--", *files)
        self.run(directory, "diff", "--cached", "--check")
        self.run(directory, "diff", "--cached")
        self.run(directory, "commit", "-m", message)
        self.clean(directory)

    def review_and_merge(self, directory, branch, message):
        self.clean(directory)
        before = self.run(directory, "rev-parse", "HEAD").stdout.strip()
        self.run(directory, "log", "--oneline", f"HEAD..{branch}")
        self.run(directory, "diff", f"HEAD...{branch}", "--stat")
        self.run(directory, "diff", f"HEAD...{branch}")
        self.run(directory, "merge", "--no-ff", "--no-commit", branch)
        self.check(
            f"merge_paused_before_commit:{branch}",
            self.run(directory, "rev-parse", "HEAD").stdout.strip() == before,
        )
        self.run(directory, "rev-parse", "--verify", "MERGE_HEAD")
        self.check(
            f"no_unmerged_paths:{branch}",
            self.run(directory, "diff", "--name-only", "--diff-filter=U").stdout == "",
        )
        self.run(directory, "diff", "--cached", "--check")
        self.run(directory, "diff", "--cached")
        self.tests(directory, 3)
        self.run(directory, "commit", "-m", message)
        self.clean(directory)

    def remove_clean(self, main, directory):
        self.clean(directory)
        self.run(main, "worktree", "remove", str(directory))
        self.check(f"clean_removal:{directory.name}", not directory.exists())

    def exercise(self):
        main = self.root / "main-repo"
        main.mkdir()
        self.run(main, "init", "-b", "main")
        self.run(main, "config", "user.name", "AIXiamo Offline Fixture")
        self.run(main, "config", "user.email", "fixture@example.invalid")
        self.run(main, "config", "commit.gpgSign", "false")
        self.run(main, "config", "core.autocrlf", "false")
        hooks = self.root / "empty-hooks"
        hooks.mkdir()
        self.run(main, "config", "core.hooksPath", str(hooks))
        self.put(main, "budget.py", BASE_CODE)
        self.put(main, "test_budget.py", BASE_TESTS)
        self.put(main, "README.md", BASE_README)
        self.put(main, ".gitignore", "__pycache__/\n")
        self.tests(main, 2)
        self.commit(main, "Create synthetic baseline", "budget.py", "test_budget.py", "README.md", ".gitignore")
        baseline = self.run(main, "rev-parse", "main").stdout.strip()

        validation = self.root / "wt-validation"
        docs = self.root / "wt-docs"
        self.run(main, "worktree", "add", "-b", "ai/validation", str(validation), "main")
        self.run(main, "worktree", "add", "-b", "ai/docs", str(docs), "main")
        self.check("same_starting_commit", all(
            self.run(p, "rev-parse", "HEAD").stdout.strip() == baseline
            for p in (validation, docs)
        ))
        self.run(main, "worktree", "add", str(self.root / "wt-duplicate"), "ai/validation", expected=None)
        self.check("same_branch_checkout_refused", not (self.root / "wt-duplicate").exists())

        self.put(validation, "budget.py", VALIDATED_CODE)
        self.put(validation, "test_budget.py", BASE_TESTS + EXTRA_TEST)
        self.run(validation, "diff", "--check")
        self.run(validation, "diff")
        self.tests(validation, 3)
        self.check("uncommitted_code_isolated", all(
            (p / "budget.py").read_text() == BASE_CODE for p in (main, docs)
        ))
        self.commit(validation, "Reject negative fixture counts", "budget.py", "test_budget.py")
        self.put(docs, "README.md", DOCS_README)
        self.run(docs, "diff", "--check")
        self.run(docs, "diff")
        self.tests(docs, 2)
        self.check("uncommitted_docs_isolated", all(
            (p / "README.md").read_text() == BASE_README for p in (main, validation)
        ))
        self.commit(docs, "Document fixture count input", "README.md")

        review = self.root / "wt-review"
        self.run(main, "worktree", "add", "-b", "review/integration", str(review), "main")
        self.review_and_merge(review, "ai/validation", "Review and merge validation")
        self.review_and_merge(review, "ai/docs", "Review and merge docs")
        self.check("combined_result_verified", (review / "budget.py").read_text() == VALIDATED_CODE and (review / "README.md").read_text() == DOCS_README)
        self.remove_clean(main, validation)
        self.remove_clean(main, docs)

        conflict_a = self.root / "wt-conflict-a"
        conflict_b = self.root / "wt-conflict-b"
        self.run(main, "worktree", "add", "-b", "demo/conflict-a", str(conflict_a), "review/integration")
        self.run(main, "worktree", "add", "-b", "demo/conflict-b", str(conflict_b), "review/integration")
        for p, name in ((conflict_a, "validation"), (conflict_b, "docs")):
            self.put(p, "README.md", DOCS_README.replace("parallel-owner: unset", f"parallel-owner: {name}"))
            self.tests(p, 3)
            self.commit(p, f"Assign fixture owner to {name}", "README.md")
        self.review_and_merge(review, "demo/conflict-a", "Review first owner choice")
        before_conflict = self.run(review, "rev-parse", "HEAD").stdout.strip()
        self.clean(review)
        conflict = self.run(review, "merge", "--no-ff", "--no-commit", "demo/conflict-b", expected=1)
        self.check("conflict_stops_merge", "CONFLICT" in conflict.stdout)
        self.check("conflict_does_not_commit", self.run(review, "rev-parse", "HEAD").stdout.strip() == before_conflict)
        self.check("conflict_has_unmerged_path", self.run(review, "diff", "--name-only", "--diff-filter=U").stdout.strip() == "README.md")
        self.run(review, "status", "--short")
        self.run(review, "ls-files", "-u")
        self.run(review, "merge", "--abort")
        self.clean(review)
        self.check("clean_premerge_state_restored", self.run(review, "rev-parse", "HEAD").stdout.strip() == before_conflict and (review / "README.md").read_text() == DOCS_README.replace("parallel-owner: unset", "parallel-owner: validation"))
        self.remove_clean(main, conflict_a)
        self.remove_clean(main, conflict_b)

        dirty = self.root / "wt-dirty"
        self.run(main, "worktree", "add", "-b", "demo/dirty-protection", str(dirty), "review/integration")
        self.put(dirty, "LOCAL_NOTE.txt", "Synthetic note retained by committing before cleanup.\n")
        self.run(main, "worktree", "remove", str(dirty), expected=None)
        self.check("untracked_file_blocks_removal", dirty.exists() and (dirty / "LOCAL_NOTE.txt").exists())
        self.commit(dirty, "Retain synthetic local note", "LOCAL_NOTE.txt")
        self.remove_clean(main, dirty)
        self.remove_clean(main, review)

        self.clean(main)
        self.check("main_baseline_untouched", self.run(main, "rev-parse", "main").stdout.strip() == baseline and (main / "budget.py").read_text() == BASE_CODE and (main / "README.md").read_text() == BASE_README)
        self.check("no_remote_configured", self.run(main, "remote", "-v").stdout == "")
        branches = self.run(main, "for-each-ref", "--format=%(refname:short)", "refs/heads").stdout.splitlines()
        self.check("topic_history_retained", set(branches) == {"main", "ai/validation", "ai/docs", "review/integration", "demo/conflict-a", "demo/conflict-b", "demo/dirty-protection"})
        worktrees = self.run(main, "worktree", "list", "--porcelain").stdout
        self.check("only_main_worktree_remains", worktrees.count("worktree ") == 1)
        return {
            "scope": "fresh synthetic local repository; no network, credentials or existing repository access",
            "git_version": self.run(main, "--version").stdout.strip(),
            "python_version": sys.version.split()[0],
            "fixture_root": str(self.root),
            "checks_passed": len(self.checks),
            "checks": self.checks,
            "commands": self.commands,
            "retained_branches": branches,
            "baseline_commit": baseline,
            "all_linked_worktrees_removed_cleanly": True,
            "main_unchanged": True,
            "production_or_remote_operations": False,
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, help="Existing directory to contain a new unique fixture directory")
    args = parser.parse_args()
    parent = args.output_root.resolve() if args.output_root else None
    if parent and not parent.is_dir():
        parser.error("--output-root must already be a directory")
    root = Path(tempfile.mkdtemp(prefix="aixiamo-worktree-fixture-", dir=parent))
    fixture = Fixture(root)
    try:
        report = fixture.exercise()
    except Exception as error:
        report = {"passed": False, "fixture_root": str(root), "error": str(error), "checks": fixture.checks, "commands": fixture.commands}
        (root / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"FAIL: inspect {root / 'report.json'}", file=sys.stderr)
        return 1
    report["passed"] = True
    (root / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": True, "checks_passed": report["checks_passed"], "git": report["git_version"], "python": report["python_version"], "report": str(root / "report.json"), "main_unchanged": True}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
