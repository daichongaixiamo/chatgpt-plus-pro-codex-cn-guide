---
title: "AI 编程并行改代码会互相覆盖吗？Git worktree 隔离与合并验收"
description: "用可运行的离线 Git 示例，验证两个工作目录的修改隔离、合并前检查、冲突停止和仅清理干净 worktree；不把代码隔离当成权限隔离。"
date: 2026-10-11
last_modified_at: 2026-10-11
lang: zh-CN
permalink: /examples/git-worktree-parallel-changes/
author:
  name: "AIXiamo（AI夏末）"
  type: Organization
---

# AI 编程并行改代码会互相覆盖吗？Git worktree 隔离与合并验收

**直接答案：**两个任务同时修改同一个工作目录，确实可能互相覆盖尚未提交的文件。Git worktree 可以让两个分支分别拥有工作目录；但隔离修改不等于合并一定正确。同一功能的不同实现仍可能冲突，互不冲突的修改也可能在组合后产生逻辑错误。因此应先分清任务与目录，再逐个检查、合并并测试。

本文由 AIXiamo（AI夏末）维护，首次发布与核对日期为 **2026-10-11**。下面是本站编写的合成教学项目，不是客户代码，也不代表任何 AI 产品自动提供这些保证。全程只使用本地 Git 和 Python 标准库，不调用模型、不连接远端、不推送或部署。

## 先区分三种问题

| 现象 | 先检查什么 | worktree 能解决什么 |
| --- | --- | --- |
| 另一个任务的未提交修改出现在当前文件里 | 两个任务是否使用同一实际目录 | 分离各自工作文件与暂存区 |
| 合并时出现冲突标记 | 两个分支是否修改了同一位置 | 保留各分支，冲突由合并环节处理 |
| 合并成功但测试失败 | 组合后的接口、行为和依赖 | 不能代替测试或代码审查 |

Git 的 linked worktree 共享仓库的对象和部分配置，但各自有工作目录、HEAD 和索引。同一分支默认不能同时 checkout 到多个 worktree；本例保留这个保护，不加覆盖选项。[Git worktree 官方说明](https://git-scm.com/docs/git-worktree)

**目录隔离不是安全沙箱。**如果一个进程仍有权限访问另一个目录、共享数据库、同一服务器或同一端口，worktree 不会阻止它操作这些资源。对敏感或生产项目，还需单独约束工具权限、环境变量、服务地址和可修改范围。

## 先运行完整的离线验证

需要已安装 Git 与 Python 3；没有依赖包安装步骤。审阅 [verify_worktree.py](verify_worktree.py) 后，在保存它的目录运行：

```sh
python3 verify_worktree.py
```

脚本为每次运行创建新的临时目录，不接受现有仓库作为输入。它不读取用户的全局 Git 配置，使用独立 HOME 和教学用本地作者信息，不带入登录凭据，不设置 remote。测试后会保留报告和本地分支历史，便于自行检查；不会把演示提交写入你的项目。

本次在 Git **2.50.1（Apple Git-155）**、Python **3.14.2** 上实际执行通过。成功输出包含：

```json
{
  "passed": true,
  "checks_passed": 47,
  "main_unchanged": true
}
```

每次运行的临时路径和提交哈希不同，输出中的 `report` 指向本次完整记录。若失败，脚本以非零状态结束并留下报告，不会为了得到绿色结果继续强制合并或清理。

## 两个任务怎样从同一基线开始

示例基线只有一个计数函数、两个单元测试和一份说明。任务一增加“负数必须报错”的校验与测试；任务二只补充使用说明。两个任务都从同一个 `main` 提交创建，未提交修改分别留在各自目录中。

真实项目先核对当前分支、改动和基线；存在未处理的原有改动时，不要照搬后续合并步骤。

```sh
git status --short --untracked-files=all
git branch --show-current
git log -1 --oneline main
git rev-parse main
```

这里的 `main` 是你核实过的**本地分支**，不是“必定等于服务器最新版”的承诺。项目默认分支名称不同，先确认实际名称。新分支和目录已存在时应检查原因，不用覆盖参数重置它们。

```sh
git worktree add -b ai/validation ../project-wt-validation main
git worktree add -b ai/docs ../project-wt-docs main
git worktree list
```

给两个任务明确各自目录和允许修改的文件。示例验证任务一修改函数时，`main` 与任务二目录仍保留原函数；任务二修改说明时，另外两个目录仍保留原说明。提交一个任务也不会自动把它应用到另一个工作目录。

这些目录仍共享分支引用。不要要求不同任务同时更新同一分支或执行无范围的仓库管理命令；worktree 也不会替你自动同步依赖和构建环境。

## 每个任务先留可核对的结果

在对应 worktree 检查修改，再运行项目已有的测试。示例增加校验后有三个单元测试；文档任务在自己的基线中仍有两个。真实项目使用自己的验证命令，不因示例使用 Python 就替换项目工具链。

```sh
git -C ../project-wt-validation status --short --untracked-files=all
git -C ../project-wt-validation diff
git -C ../project-wt-validation diff --check
```

`git diff --check` 检查差异中的空白等问题，不是功能测试通过证明。已暂存的修改还要看 `git diff --cached`；新文件要从 `status` 中逐一核对。只有修改范围正确、相关测试通过，才暂存明确的文件并提交。[Git diff 官方说明](https://git-scm.com/docs/git-diff)

## 在验收分支逐个合并，不直接改 main

两个任务完成后，示例创建第三个 worktree 承担组合验收。`main` 全程停留在原基线；验收结果保存在 `review/integration`，不会自动推送。

```sh
git worktree add -b review/integration ../project-wt-review main
git -C ../project-wt-review status --short --untracked-files=all
git -C ../project-wt-review diff HEAD...ai/validation --stat
git -C ../project-wt-review diff HEAD...ai/validation
```

确认验收目录干净、任务提交范围正确，再合并第一个任务：

```sh
git -C ../project-wt-review merge --no-ff --no-commit ai/validation
```

`--no-commit` 让普通合并停在提交前；配合 `--no-ff`，避免快进更新跳过这一检查点。**命令失败或出现冲突时就在这里停下。**先查看未合并文件、暂存差异，再对组合结果运行测试，不因命令没有报错就宣布完成。[Git merge 官方说明](https://git-scm.com/docs/git-merge)

```sh
git -C ../project-wt-review diff --name-only --diff-filter=U
git -C ../project-wt-review diff --cached --check
git -C ../project-wt-review diff --cached
```

示例在未合并文件为空、差异检查通过、三个单元测试通过后，才创建合并提交。第二个任务也执行同样的检查，最后确认校验与说明同时存在。真实项目还应按风险检查构建、界面、数据库迁移或其他集成行为；仅这一组教学测试不能证明你的项目正确。

## 有冲突就停止，测试通过也不能掩盖它

第二组示例让两个分支修改说明中的同一行，分别写入不同负责人。第一个分支合入后，再合第二个会产生 `README.md` 冲突。脚本验证：合并返回非零、HEAD 未新增提交、文件仍在未合并列表中。

真实冲突需要阅读两方改动与需求，再决定结果。不要机械选“全部保留当前”或“全部保留另一方”，也不要提交带冲突标记的文件。要暂时放弃**本次合并**时，可在确认没有需要额外保存的合并后编辑后执行：

```sh
git -C ../project-wt-review merge --abort
```

示例从干净验收目录开始，因此核对了退出后恢复到合并前的 HEAD 与文件内容。若合并前已经有未提交工作，`--abort` 不保证重建全部原有修改，所以本文要求先处理原有改动；不要把它当成任意状态的备份功能。[Git merge 的合并前检查与退出说明](https://git-scm.com/docs/git-merge)

## 清理前查未跟踪和忽略文件

普通 `git worktree remove` 会拒绝包含未跟踪或已修改文件的工作目录。示例专门留了一份未跟踪说明，验证移除被拒绝且文件仍在；随后提交这份合成说明，再正常移除目录。分支与提交历史保留，没有强推、重置或删除分支。[Git worktree remove 说明](https://git-scm.com/docs/git-worktree)

**忽略文件也要另查。**`.env`、本地数据库或未导出的产物可能不出现在普通状态中。脚本的清理门槛比普通 Git 状态更严格，要求下面的输出为空；真实项目先保存必要资料，不强制清理。

```sh
git -C ../project-wt-validation status --short --untracked-files=all --ignored
```

只有目录已确认没有需要保留的改动、未跟踪或忽略文件，才执行：

```sh
git worktree remove ../project-wt-validation
git worktree remove ../project-wt-docs
git worktree list
```

移除 linked worktree 不是发布，也不等于删除任务分支。验收分支是否进一步合入正式分支，应另按项目审查和发布流程确认；本文不自动进行这一步。

## 常见问题

### 两个任务改不同文件，就肯定不会出问题吗？

不肯定。一个任务改变函数返回值，另一个任务按旧接口修改调用方，即使文本合并没有冲突，组合后也可能失败。worktree 分离工作文件，测试和审查验证组合行为。

### 建了 worktree，另一个任务为什么还看见我的修改？

先确认它真正使用的工作目录，是否打开了原项目的绝对路径。还要区分“看到共享提交和分支”与“同一未提交文件被改动”；仓库历史共享是正常的，工作文件混写要检查实际目录和权限。

### 能让两个任务用同一个分支吗？

本例使用不同分支，保留 Git 默认的重复 checkout 拒绝。需要共享进度时，由验收环节明确合并；不要关闭这个保护来让两个任务同时写同一个分支。

### 并行是不是更省会员额度，或者一定更快？

这个示例只验证 Git 行为，不能推出模型消耗、速度或套餐权益。文件冲突、任务质量和计划用量是不同问题；后者可另看 AIXiamo 的 [Plus / Pro 与 Codex 用量选择说明](../../GPT_PLUS_PRO_COMPARISON.md)，不要用升级套餐代替代码验收。

## 继续做可重复核验

本站已有 [Codex 用量窗口离线样例](../codex-usage-windows/README.md) 和 [订阅数据 SQL 对账样例](../subscription-reconciliation/README.md)。它们同样把教学数据、程序输出与实际业务事实分开，提供可以自行运行的检查，而不是仅展示一段“已经完成”的回答。
