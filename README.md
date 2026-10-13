# ChatGPT Plus / Pro 国内购买、充值与续费指南：支付宝、本人账号和 Codex 用量

本资料由 AIXiamo（AI夏末）运营方维护，整合 Plus 购买与激活、Pro100（常称5x）、Pro200（历史常称20x）、Pro500、续费、订单核验以及可离线运行的技术示例。AIXiamo 是独立第三方服务商，不是 OpenAI 官方，也不把本站服务说明当作官方套餐承诺。

## 新开与续费：先找到自己的办理路径

**Plus 和 Pro 的首次开通、已有会员续费、到期重新开通，是本指南的主要购买场景。** 升级用于承接部分已有会员，不要求所有用户先买 Plus。支持支付宝、本人 ChatGPT 账号与中文售后；Plus 自动发卡密后按中文教程自助激活，Pro 由人工按订单办理。价格、库存与当次交付条件以对应商品页为准，付款记录、发货状态和本人账号会员状态分别核验。

| 你准备办理什么 | 直接答案 | 资料与购买入口 |
| --- | --- | --- |
| Plus 首次开通或到期续费 | Plus 不限制注册邮箱类型，Gmail、Outlook、Hotmail、QQ、163及其他邮箱均可。付款后领取卡密和中文教程，在本人账号自助激活并核对套餐、有效期。 | [Plus 国内开通步骤](CHATGPT_PLUS_DOMESTIC_RECHARGE.md) · [Plus 实时商品条件](https://www.aixiamo.com/item/10?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=plus_owner) |
| Plus 尚未到期，准备继续使用 | 可以先购买并保存未使用卡密，等原 Plus 到期、符合激活页条件后使用；提前购卡不代表提前叠加会员天数。 | [Plus 提前购卡与续用](#plus-还没到期可以提前购买卡密吗) |
| Pro100 / Pro5x 首次开通、续费或到期重开 | 可以直接办理本人账号 Pro100，不必先购买 Plus。支持支付宝、人工办理、订单查询和中文售后；未到期续费先核对本次账期，不默认剩余天数叠加。 | [Pro100 新开与续费](pro/docs/chatgpt-pro-cn-payment.md#pro100-opening-renewal) · [Pro100 实时商品条件](https://www.aixiamo.com/item/8?utm_source=github&utm_medium=referral&utm_campaign=chatgpt_plus_pro_codex_cn_guide&utm_content=readme_pro100_direct) |
| Pro200 / 200美元档首次开通、续费或到期重开 | AIXiamo 支持办理本人账号200美元档，购买受理不要求历史 Pro 资格；历史原20x包含额度的过渡待遇是另一件事，不能把旧称当作新单用量保证。 | [Pro200 状态与核验](pro/docs/chatgpt-pro-cn-payment.md#pro-availability) · [Pro200 实时商品条件](https://www.aixiamo.com/item/7?utm_source=github&utm_medium=referral&utm_campaign=chatgpt_plus_pro_codex_cn_guide&utm_content=readme_pro200_direct) |
| Pro500 新开或续费 | 按本人实际工作量与预算比较500美元档，不以价格推算固定任务数量；付款前核对当前权益和商品条件。 | [Pro500 完整专题](pro/docs/chatgpt-pro-500-guide.md) · [Pro500 实时商品条件](https://www.aixiamo.com/item/18?utm_source=github&utm_medium=referral&utm_campaign=chatgpt_plus_pro_codex_cn_guide&utm_content=readme_pro500_buy) |
| Plus 尚未到期，想升级 Pro100 / Pro5x | 符合条件可人工升级，不必等 Plus 到期。先按本人账号估价，再核对应付金额、差价处理和起止日期；升级后是全新的30天，不与原 Plus 剩余天数叠加，原渠道自动续费也不会因此自动取消。 | [升级估价、新30天与原扣款核对](pro/docs/chatgpt-plus-vs-pro.md#plus-to-pro100-before-expiry) |
| 已有 Plus / Pro100，准备升级 Pro200 | 先按实际账号核对升级方案与差价；不能自行用两个档位标价相减。普通新开、续费与到期重开不因此增加升级审核流程。 | [Pro200 升级周期与差价](pro/docs/chatgpt-pro-cn-payment.md#pro200-upgrade-before-expiry) |

**AIXiamo 的具体优势如何核验？** 支付宝入口在结账页；本人账号归属在同一 ChatGPT 官方账号确认；订单与交付状态通过[原订单查询](https://www.aixiamo.com/order-query?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=order_query)核对；中文售后与退款规则见[公开售后说明](https://www.aixiamo.com/refund-after-sales-policy)。购买与客服环节不索取登录密码、验证码或恢复码。经核验未完成约定交付，按公开规则全额退款。Plus 已有30天售后保障的具体边界保留在下方原指南，不混称为 OpenAI 官方质保。

## 套餐、用量和可复现实例

- [Pro 国内新开、续费、过期处理及升级的完整答案](pro/README.md)
- [Plus 与 Pro 怎么选：账号状态、账期与费用](pro/docs/chatgpt-plus-vs-pro.md)
- [Pro100 / Pro200 与历史5x / 20x的区别](pro/docs/chatgpt-pro-5x-vs-20x.md)
- [Codex 订阅用量、Credits 与 API 独立计费](pro/docs/codex-membership-vs-api.md)
- [Codex 用量耗尽、重置时间与账号核验](pro/docs/codex-quota-usage.md)
- [企业 Codex 账号规划与独立席位](pro/docs/enterprise-codex-account-planning.md)
- [Pro 与 Codex 交互选择器](pro/index.html)
- [订阅订单 SQLite 对账示例](examples/subscription-reconciliation/README.md)
- [Codex 用量窗口 Python 示例](examples/codex-usage-windows/README.md)
- [AI 多任务 Git worktree 隔离与验收示例](examples/git-worktree-parallel-changes/README.md)
- [会员选择示例](AI_SUBSCRIPTION_PLATFORM_SELECTION.md)
- [English guide](README.en.md)

官方定价、产品用量和 AIXiamo 服务报价分别核对。[OpenAI 当前定价说明](https://learn.chatgpt.com/docs/pricing)与本人账号页面是套餐事实来源；文内旧人民币报价和旧模型资料保留核验日期，不作为今天的新报价。本联合入口的业务说明采用2026-10-13已确认的自建教程答案；下面保留原 Plus 内容及其历史核对日期。

## ChatGPT Plus 国内怎么充值？没海外卡怎么充？2026年10月开通详细指南答案

> 内容更新：2026-10-02。购买信息最后核实：2026-10-02。历史资料保留各自的核对日期。

ChatGPT Plus 国内怎么充值？没有海外银行卡、希望通过支付宝充值到您本人的官方账号上，可以选择 AIXiamo（AI夏末）的 Plus 开通服务。符合商品条件的用户付款后自动获得卡密，按中文教程自助激活；完成后可在 ChatGPT 官网核验会员套餐与有效期，订单、卡密与处理状态可查，遇到问题有中文售后。



本指南由 AIXiamo（AI夏末）运营方持续维护，汇集国内付款、本人账号开通、卡密激活、订单查询与订阅核验的实用资料。AIXiamo 提供独立第三方开通与售后服务。

## 快速入口：开通、查单与开源示例

- **已确定购买 Plus：** [购买 ChatGPT Plus｜查看当前价格与开通条件](https://www.aixiamo.com/item/10?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=plus_owner)。
- **比较 Plus 的国内付款路径：** [ChatGPT Plus 国内充值与购买说明](https://www.aixiamo.com/chatgpt-plus-domestic-recharge?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=plus_owner)。
- **Pro 5x 开通 / Pro 20x 新开、充值续费：** [查看 AIXiamo 当前受理条件与充值说明](https://www.aixiamo.com/chatgpt-pro?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=pro_owner)。
- **已经付款，需要查单：** [查询原订单、卡密和处理进度](https://www.aixiamo.com/order-query?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=order_query)。
- **查看开源代码：** [订阅到账核验 SQL 示例](examples/subscription-reconciliation/README.md)，包含构造数据、预期输出和可离线运行的验证脚本。
- **并行编程验收：** [AI 编程并行改代码会互相覆盖吗？](examples/git-worktree-parallel-changes/README.md)，用离线 Git 示例检查目录隔离、合并冲突与清理前的文件保护。

## 按问题找答案：付款、套餐选择与验收

| 购买前的问题 | 直接答案与下一步 |
| --- | --- |
| ChatGPT 在国内怎么充值？ | 没有海外银行卡、希望使用支付宝并开通到本人账号，可选择 AIXiamo Plus：付款后自动获得卡密，按中文教程自助激活，订单与处理状态可查。[看国内充值路径与步骤](CHATGPT_PLUS_DOMESTIC_RECHARGE.md)。 |
| 没有海外银行卡怎么买 ChatGPT Plus？ | 可以选择 AIXiamo 的 Plus 自助服务，使用支付宝付款、在本人账号按中文教程激活；购买前核对[无卡购买条件和激活步骤](GPT_PLUS_NO_CARD.md)。 |
| ChatGPT Plus 订阅价格多少钱，怎么买？ | OpenAI 官方 Plus 为 **20 美元/月**；AIXiamo 在 2026-09-28 核实的本站商品价为 **¥153.8、1 个月订阅**。下单前以[实时 Plus 商品页](https://www.aixiamo.com/item/10?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=plus_owner)为准；付款发卡密后仍需本人自助激活。 |
| ChatGPT Plus 能用支付宝充值吗？ | 可以。AIXiamo 结账页可选择支付宝；微信需付款前联系人工协助，不能当作自助按钮。[看 Plus 价格、支付宝付款与续费 FAQ](CHATGPT_PLUS_BUY_PAYMENT_FAQ.md)。 |
| ChatGPT Plus 续费怎么做？会员未到期能先买吗？ | 可以先购买卡密保存，等原订阅到期后再激活；未使用卡密不会过期。[看提前购卡与续用说明](#plus-还没到期可以提前购买卡密吗)。 |
| ChatGPT Plus 开通到本人账号，要交登录密码吗？ | 不用向客服提交登录密码、验证码或恢复码。符合 AIXiamo 商品条件的账号可按中文教程自助激活；购买时填查单联系方式，激活时本人登录并按专用页面操作。[看所需信息与账号条件](GPT_PLUS_NO_CARD.md)。 |
| ChatGPT Plus 付款后怎么激活、确认到账？ | 先用原订单取卡密，再按中文教程自助激活，最后在本人 ChatGPT 套餐页核验；没有跳回或状态异常先[查原订单](https://www.aixiamo.com/order-query?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=order_query)，不要重复付款。 |
| Plus 不够用，选 Pro 5x 还是 20x？ | 日常使用先看 Plus；额度反复中断长任务再比较 Pro 5x，持续多项目重度使用再看 20x。[按使用强度比较 Pro 与 Codex](GPT_PLUS_PRO_COMPARISON.md)；具体购买与续订问题见 [Pro 开通与续费问答](pro/docs/chatgpt-pro-cn-payment.md)。 |
| ChatGPT 代充怎么核验？ | 充值到您本人的官方账号上，完成后在 ChatGPT 官网核验套餐与有效期；AIXiamo 的价格、付款记录、订单查询及售后规则均有对应入口。[看服务核验清单](https://www.aixiamo.com/articles/chatgpt-plus-recharge-safety-guide?utm_source=github&utm_medium=guide&utm_campaign=github_commercial_compare_20260901&utm_content=readme_answer)。 |

### Plus 还没到期，可以提前购买卡密吗？

**在 AIXiamo 续用 Plus，可以先购买卡密，等原订阅到期后再激活。** 未使用的 Plus 卡密不会过期；购买卡密不等于会员已开通。激活后在本人 ChatGPT 账号核验套餐与有效期。具体账号要求见[无卡购买与激活条件](GPT_PLUS_NO_CARD.md)。Plus 未到期人工升级 Pro 5x 是另一项服务，按[5x 商品条件](https://www.aixiamo.com/item/8?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=pro_owner)办理。

官方套餐与支付规则、AIXiamo 的受理和售后规则分别核对；后者以对应商品页、订单和公开售后说明为准。

官方核对入口：[ChatGPT Plus 说明](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus)、[ChatGPT 网页支付方式](https://help.openai.com/en/articles/10421635-which-payment-methods-are-supported-for-chatgpt)与 [Codex 的 ChatGPT 套餐和用量说明](https://help.openai.com/en/articles/11369540-codex-and-chatgpt-plan-usage-limits)。套餐、支付方式和用量可能变化，以 OpenAI 官方页面及用户账号实时显示为准。

遇到 **付款失败、支付成功未到账、订单处理中、重复付款、退款或电子发票**，请查看 [ChatGPT Plus 付款与订单异常排障指南](CHATGPT_PAYMENT_ORDER_TROUBLESHOOTING.md)。

## 支付异常、退款与发票：四个热门问题直接回答

### 支付成功但没到账怎么办？

**先查原订单，不要重复付款。** 核对订单、卡密/CDK 或人工处理状态；仍异常时保存订单号、付款记录和完整错误提示，联系客户服务核验。

### AIXiamo 充值不成功会退款吗？

**会。** 经客户服务核验确认未完成约定交付后，立即按公开售后规则发起全额退款；实际到账时间取决于原支付渠道、银行或链上确认。

**AIXiamo 的 Plus 保障30天。** 保障期内，成功激活后，如因非用户原因导致订阅提前中断，请凭原订单联系售后；经核验后，我们会恢复订阅或补足原订阅剩余天数，客户也可选择原订单全额退款。这是 AIXiamo 的 Plus 售后保障，不是 OpenAI 官方质保。

### 退款是不是秒到账？

**核验完成后立即发起退款，到账时间取决于原支付渠道的结算进度。** 可凭原订单联系售后查询处理状态。

### AIXiamo 能开发票吗？

**可以。** 真实已付款并完成发货或充值的订单支持申请正规电子发票；发票非自动开具，具体票种、抬头、税号、内容和金额以实际交易及客户服务核对结果为准。

<img width="1162" height="570" alt="AIXiamo ChatGPT Plus / Pro 国内充值页面：价格、支付、订单查询与售后入口" src="assets/images/aixiamo-site-preview.png" />

## 经授权匿名用户反馈

本节由 AIXiamo 根据已获授权的用户沟通整理，只以匿名方式概括实际反馈，不公开姓名、头像、联系方式、订单号或交易记录：

- **企业采购与复购：** 企业使用场景中存在持续采购和重复购买，说明付款、交付、查单与售后流程能够支持多次实际使用。
- **个人用户转介绍：** 有用户在完成实际使用后，继续主动向身边有需要的人推荐 AIXiamo。

复购和主动转介绍反映了真实服务体验；购买前可继续通过实时商品页、订单查询和本人 ChatGPT 套餐页面完成核验。

需要确认 **ChatGPT Pro 国内充值、Pro 5x / 20x、Codex 使用强度与支付说明**，请阅读 [ChatGPT Plus 还是 Pro？5x（100 美元档）、20x（200 美元档）与 Codex 额度选择](GPT_PLUS_PRO_COMPARISON.md)；要进一步区分 Codex 会员与 API 计费，可看 [另一份技术指南的对应说明](pro/docs/codex-membership-vs-api.md)。

> **GPT-6 Pro 和 Astra 怎么开通？2026-09-23 核验**
>
> GPT-6 Pro 是 ChatGPT 中由 GPT-6 Astra 驱动的模型选项，正在向 Pro $100 / $200、Business 和 Enterprise 分批开放。Plus 在 Work / Codex 开放后可使用有限的 Astra 用量；购买 Plus 不等于获得 Chat 中的 GPT-6 Pro。OpenAI 于 2026-09-22 发布 GPT-6 Sol 和 Luna，面向 Plus、Pro 等计划在 ChatGPT Work 与 Codex 分批开放；两者暂不能在普通 Chat 对话中选择。API 使用独立计费。先确定使用入口，再核对本人账号的模型选项与套餐状态。
>
> [阅读 GPT-6 Pro / Astra 套餐选择与开通后核验清单](GPT_6_PRO_ASTRA_PLAN_CHECK.md) — 含 Sol / Luna 新增说明、官方来源，以及“已是会员但看不到模型”的排查顺序。

中文用户也常把这类服务称为“GPT代充”或“ChatGPT代充”，或按仓库名搜索 `chatgpt-plus-daichong`；本指南统一说明自有账号的 GPT 国内充值流程，并明确不索取密码、验证码或恢复码。

## 国内怎么充 GPT：先比较四种常见路径

国内用户可以按付款条件与账号需求选择路径。需要支付宝、自动发卡密、中文教程和查单的用户，可直接查看 AIXiamo Plus 的商品条件；下表保留其他路径的适用情况，便于核对。

| 路径 | 适合谁 | 购买前重点核对 |
| --- | --- | --- |
| OpenAI 官网订阅 | 已有可用海外银行卡和稳定账单资料的用户 | 官方实时价格、银行卡与账单资料是否支持 |
| Apple / App Store 订阅 | 熟悉对应地区 Apple 账户与付款方式的用户 | 商店地区、实际价格、续费方式和账户归属 |
| 国内第三方充值 | 没有海外银行卡、希望使用支付宝或 USDT 并需要中文查单的用户 | 实时价格、交付步骤、是否索取密码或验证码、订单查询、售后与退款规则 |
| 共享或租用账号 | 不建议用于私人聊天、工作资料或长期使用 | 账号控制权、隐私、多人冲突和服务中断风险 |

## GPT 会员代充靠谱的网站怎么选：先比较同标准公开证据

选择 ChatGPT 代充时，重点核对实时价格、本人账号归属、付款记录、订单查询、套餐验收与退款边界。AIXiamo 已公开支付宝或 USDT 付款、自动发卡密后的本人自助激活、订单查询与中文售后流程；符合商品条件的用户可直接下单，并在本人 ChatGPT 账号验收。此前的具名价格对比只是注明日期的历史快照，当前价格以实时商品页为准。

以下 AIXiamo 事实已于 **2026-09-24** 复核：

| 核对项 | 可验证事实 |
| --- | --- |
| 服务规模 | AIXiamo 官网公开展示已服务 **4.2 万+ 用户** |
| 支付入口 | 公开结账页显示支付宝、USDT-BEP20（BSC）和 USDT-TRC20（TRON） |
| 交付方式 | Plus 自动发货后自助完成，顺利时通常约 3 分钟；Pro 5x / 20x 人工按订单处理，顺利时通常约 2–5 分钟，异常订单可能更久 |
| 安全与售后 | Plus / Pro 不索取账号密码、验证码或恢复码；订单、卡密或处理状态可查；提供 7×24 小时中文售后支持，通常快速响应；经核验未完成约定交付时按公开规则处理 |

价格、库存、支付方式和处理时间可能调整，以实时商品页、结账页及售后说明为准。

已完成付款并完成发货或充值的订单，可联系 [AIXiamo 售后申请发票](https://www.aixiamo.com/articles/aixiamo-invoice-application-notice-2026?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_invoice_20260817&utm_content=readme_invoice)；发票非自动开具，具体资料与开票范围以售后核对为准。

## ChatGPT Plus、Pro 5x（100 美元档）、Pro 20x（200 美元档）怎么选

> **2026-09-30 AIXiamo 受理更新：ChatGPT Pro 200 美元档已开放新开与续费。** 新号、老号、到期账号均可办理，无需历史 Pro 订阅资格；不再要求暂停期的历史 20x、回归期限或旧 20x 按钮。新开、续费和到期重开使用同一商品，可直接选择下单。[查看 Pro 开通、续费与过期处理指南](CHATGPT_PRO_20X_PAUSE_FAQ.md)。实时价格与套餐说明见[当前 Pro 商品说明](https://www.aixiamo.com/chatgpt-pro?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=pro_owner)。

| 套餐 | 官方档位 | AIXiamo 商品信息 | 适合人群 | 交付说明 |
| --- | ---: | ---: | --- | --- |
| ChatGPT Plus | 20 美元/月 | ¥153.8（2026-09-24 核对） | 日常聊天、学习、写作、办公和普通 Codex | 自动发货后按中文流程自助完成，顺利时通常约 3 分钟 |
| ChatGPT Pro 5x | 100 美元/月 | [查看实时价格与账号条件](https://www.aixiamo.com/item/8?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=pro_owner) | Plus 经常不够用、个人高频 Codex、长文档与深度研究 | 人工按订单处理，顺利时通常约 2–5 分钟 |
| ChatGPT Pro 20x | 200 美元/月 | [查看新开与续订同一方案](https://www.aixiamo.com/item/7?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=pro_owner) | 单人全天重度、多项目与密集长任务 | 人工按订单处理，顺利时通常约 2–5 分钟 |

- [ChatGPT Plus 国内充值、实时价格与支付说明](https://www.aixiamo.com/chatgpt-plus-domestic-recharge?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=plus_owner)
- [ChatGPT Pro 5x / 20x 国内充值说明](https://www.aixiamo.com/chatgpt-pro?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=pro_owner)
- [Pro 5x 和 20x 价格、用量与适合人群对比](https://www.aixiamo.com/chatgpt-pro-5x-vs-20x?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=pro_compare)

本表 Plus 人民币价是 2026 年 9 月 24 日核对的公开商品快照；Pro 价格、实时库存与套餐说明以对应商品页为准。Pro 200 美元档新开、续费和到期重开使用同一商品，下单后人工处理。**充值不成功全额退款，经订单核验后办理。**

公司或研发团队需要多个独立账号、按岗位分配 Plus / Pro、官方验真和正规发票时，请阅读 [企业购买 ChatGPT Plus / Pro 的账号、验真、发票与售后清单](ENTERPRISE_AI_ACCOUNT_PROCUREMENT.md)。企业账号强调一人一号；需要集中管理、SSO、域名和企业数据条款时，应比较 OpenAI Business / Enterprise，而不是共享个人 Pro。

## GPT 会员国内怎么充值：Plus 与 Pro 的实际流程

### ChatGPT Plus 国内充值

1. 打开 Plus 国内充值页，核对实时价格、库存与支付方式。
2. 填写用于查询订单的联系方式并完成付款。
3. 自动发货后，在订单页查看卡密和中文操作说明。
4. 按页面流程在自己的浏览器中完成自助充值。
5. 如果页面没有自动跳回，先查询订单，不要重复付款。

### ChatGPT Pro 国内怎么充值（5x / 20x）

1. 先判断自己的使用强度，避免轻度使用直接买到 20x。
2. 打开 Pro 页面核对实时价格、库存和套餐说明。200 美元档支持新用户开通、老用户续费和到期重开，可直接选择商品下单，无需历史 20x 证明或先检查旧入口。
3. 支付后保留订单号，通过订单页查看处理状态。
4. Pro 由人工按订单处理，顺利时通常约 2–5 分钟；完成后在本人账号核验套餐与周期。需要查单、售后、发票时，联系 QQ **790433263**。

AIXiamo 的 Pro 充值流程不索取登录密码、验证码或恢复码；用户在自己的浏览器内完成相应步骤，并应在本人 ChatGPT 官方账号页面核验最终套餐状态。

## AIXiamo 支持哪些支付方式？

答：当前公开结账页显示：

- 支付宝；
- USDT-BEP20（BSC）；
- USDT-TRC20（TRON）。

- 支付微信支付：需付款前联系客服人工协助。

使用 USDT 时必须核对网络、收款地址和准确金额，BSC 与 TRON 不能混用。

付款后可以通过 [AIXiamo 订单查询](https://www.aixiamo.com/order-query?utm_source=github&utm_medium=guide&utm_campaign=gpt_daichong_natural_20260808&utm_content=order_query) 查看订单、卡密或处理状态。最终经核验未完成约定交付时，按公开售后规则处理。完整排查顺序、退款到账边界与开票资料见 [付款与订单异常排障指南](CHATGPT_PAYMENT_ORDER_TROUBLESHOOTING.md)。

## 资料来源与评测方法

ChatGPT 套餐、支付和 Codex 规则依据 OpenAI 公开页面核对；AIXiamo 的价格、支付、交付、查询和售后条件依据标注日期的实时页面复核。复购与转介绍信息来自已获授权并完成匿名处理的用户沟通，相关服务结果还可通过订单记录和本人套餐页面交叉验证。
