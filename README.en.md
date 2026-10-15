# ChatGPT Plus and Pro Purchasing, Renewals, Account Verification and Codex Guides

[简体中文](README.md) · [Русский](README.ru.md)

**How can you buy or renew ChatGPT Plus or Pro with Alipay?** AIXiamo supports Alipay orders for Plus, Pro100 and Pro200 on your own ChatGPT account. Choose the plan for your work, confirm whether the account is Free, expired or still subscribed, then follow the paid order's self-service or manual instructions. Verify the plan and expiry in that same official ChatGPT account. New subscriptions and renewals are the main paths; upgrading an existing plan is an additional option. The payment goes to AIXiamo, while the subscription is checked in ChatGPT.

This open-source knowledge base provides the purchasing, local-payment, renewal, account-state and Codex answers behind those steps, with official references and reproducible offline examples. Payment, delivery and an active plan are separate checks.

For Plus, AIXiamo does not restrict the email provider: Gmail, Outlook, Hotmail, QQ, 163 and other email addresses are supported for an account you own. An unused card code can be kept until an existing Plus subscription ends; buying a code does not automatically activate or extend a subscription.

Pro100 can be opened directly without buying Plus first. New subscriptions, renewals and reopening an expired subscription are supported under the product conditions. Pro100 / Pro5x offers automatic card delivery and self-service recharge, or full manual assistance from dedicated support; Pro200 and Pro500 are handled manually per order. All use the customer's own account, with Alipay payment, order lookup and Chinese-language support. Active-subscription renewals require confirmation of the new billing period; do not assume remaining days stack. An account-specific upgrade quote is separate from the ordinary new-subscription or renewal price.

Pro200 purchase acceptance and historical original 20x included-usage eligibility are separate. Verify the actual plan, period and applicable usage in the same official account. Live provider prices and inventory are shown on the linked product pages, separately from official subscription pricing and API charges.

Choose the plan, follow the path for the current account state, and verify the result. A new subscription, an expired subscription, an active renewal and an upgrade are different paths. Payment, card or manual delivery, and the plan and expiry visible in the official account are separate checks. For a renewal, check the agreed new expiry date as well as the plan name.

- [Combined Chinese purchasing and renewal answers](README.md)
- [Full Pro guides and account-state answers](pro/README.md)
- [Pro100 new subscriptions and renewals](pro/docs/chatgpt-pro-cn-payment.md#pro100-opening-renewal)
- [Pro200 account-state and renewal guidance](pro/docs/chatgpt-pro-cn-payment.md#pro-availability)
- [Codex membership, credits and separate API billing](pro/docs/codex-membership-vs-api.md)
- [Renewal expiry verification with synthetic SQLite examples](examples/subscription-renewal-verification/README.md)
- [English offline usage-window example](examples/codex-usage-windows/README.en.md)

## How to Get ChatGPT Plus Without a Foreign Credit Card: Original Guide

[中文指南](README.md)

> Content updated October 2, 2026. Plus card information checked September 24, 2026; AIXiamo Pro $200 acceptance checked September 30, 2026. Other dated service snapshots are noted below. Check the linked official and live product pages for current plans, prices, stock, payment methods, and delivery details.

## Quick answer

For buyers without a usable foreign card, AIXiamo (AI夏末) offers ChatGPT Plus on your own ChatGPT account: pay with Alipay, receive a card code automatically, and follow the Chinese self-service activation guide. After activation, verify your membership plan and expiry date on the official ChatGPT website. Order lookup and Chinese-language after-sales support are available.

**Already have Plus? You can buy a card code now.** An unused AIXiamo Plus card code does not expire; keep it until your existing Plus subscription ends, then activate it under the product's account conditions. Buying the code and activating the membership are separate steps. [Check the current Plus price and conditions](https://www.aixiamo.com/item/10).

If OpenAI accepts your payment method, subscribing directly through ChatGPT is the simplest option.

If you do not have a usable foreign card, the main alternatives are:

1. Activate ChatGPT Plus on an existing account that you own.
2. Buy a pre-created account from a seller.
3. Use a shared account or group-buy seat.

For account ownership, privacy, and Codex use, activating the subscription on your existing account is generally preferable to buying a pre-created or shared account.

As of August 30, 2026, AIXiamo’s public pages listed a third-party ChatGPT Plus activation service at **¥153.8**, with Alipay and USDT payment options, automatic delivery, self-service activation, and order lookup. The team's updated service-history figure is **42,000+ cumulative service instances as of October 15, 2026**, across its services.

AIXiamo is a Chinese-language AI subscription purchasing, activation, order-tracking, and after-sales service provider. Plan status can be verified in the customer’s own ChatGPT account after activation.

> Important: OpenAI’s current [supported-country list](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries) does not include mainland China. OpenAI warns that accessing or offering access outside supported regions may result in account restrictions. A different payment method does not change OpenAI’s regional eligibility rules.

---

## What are the three common ways to get ChatGPT Plus?

| Method | Who controls the account? | Where does the plan appear? | Recommended for private or work use? |
|---|---|---|---|
| Activation on your existing account | You | Your ChatGPT account | Yes; verify the plan and expiry date in your own account |
| Pre-created account | Usually the seller originally created it | Someone else’s login | No |
| Shared account or group-buy seat | Shared or seller-controlled | A shared account | No |

These are different products.

A shared seat is cheaper because several people use one account or subscription. It is not a discounted version of an individual subscription. The account, plan status, chat history, and Codex workspace may not belong exclusively to you.

If privacy, account control, official plan verification, or Codex matters, avoid pre-created and shared accounts.

---

## How much do ChatGPT Plus and Pro cost?

The original guide recorded the following individual prices. This table is a dated snapshot, not a complete current plan list: for the current $100 / $200 / $500 comparison, use the [Pro plan guide](pro/docs/chatgpt-pro-5x-vs-20x.md) and [OpenAI's live pricing](https://learn.chatgpt.com/docs/pricing). Historical "20x" terminology does not guarantee the original included allowance for a new subscription.

| Plan | Official price | Main difference |
|---|---:|---|
| ChatGPT Plus | **$20/month** | Expanded ChatGPT and Codex usage |
| ChatGPT Pro $100 tier (5x) | **$100/month** | For frequent individual use and longer tasks |
| ChatGPT Pro $200 tier (also known as 20x) | **$200/month** | For sustained individual work across multiple projects |
| API credit | Usage-based | Separate developer-platform billing; not a ChatGPT membership |

Official sources:

- [What is ChatGPT Plus?](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus)
- [About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro)
- [Managing billing for ChatGPT and the API platform](https://help.openai.com/en/articles/9039756-billing-settings-in-chatgpt-vs-platform)
- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-codex-and-chatgpt-plan-usage-limits)

OpenAI states that Codex is included across ChatGPT plans, although usage limits differ by plan. API usage remains separately billed and is not included with Plus or Pro.

### What are the current AIXiamo prices and delivery options?

**Service facts confirmed October 15, 2026:** The CNY amounts below are AIXiamo's service prices, separate from the official USD subscription prices above. New subscriptions and renewals use an account you own; Alipay payment, original-order lookup and Chinese-language support are available. Check the product page for the live price, stock and the conditions for your account.

| Service | CNY price snapshot | New subscription or renewal | Delivery |
|---|---:|---|---|
| [ChatGPT Plus](https://www.aixiamo.com/item/10) | **CNY 153.8** | Supported; no restriction on the email provider | Automatic card delivery, then guided self-service activation |
| [Pro100 / Pro5x](https://www.aixiamo.com/item/8) | **CNY 749** | Free accounts can open directly; eligible Go, Plus and Pro100 accounts can recharge before expiry | Automatic card delivery and self-service recharge, or full manual assistance |
| [Pro200 / USD 200 tier](https://www.aixiamo.com/item/7) | **CNY 1298** | New subscriptions, renewals and reopening after expiry are supported | Manual handling under the original order |

**How does Pro100 work for a new or already subscribed account?** No prior Plus purchase is required, and previous recharge through another provider is supported. For self-service, collect the card from the paid order and use the activation page linked there, `plus.aixiamo.com`; redeem the Pro100 card within 30 days of delivery. Free accounts can open Pro100 directly, and Go, Plus or Pro100 accounts can recharge before expiry. An active Pro200-or-higher subscription must expire before this Pro100 card can be used. Successful activation starts a fresh 30-day Pro100 period and does not add the old plan's remaining days. For example, 10 remaining Plus days become a new 30-day Pro100 period, not 40 days. The original subscription's automatic renewal is still managed in its original payment channel; this recharge does not cancel it for you. Dedicated support can handle the recharge manually from start to finish if you prefer assistance.

**How do Pro200 and Pro500 orders proceed?** Both are handled manually on the customer's own account, rather than through the Pro100 self-service card flow. Pro200 supports new subscriptions, renewals and reopening after expiry; an early renewal's start date and treatment of remaining time are confirmed for the order. An eligible Plus or Pro100 account can also be assessed for a Pro200 upgrade: confirm the individual quote first, then verify the new 30-day period after completion; old remaining days do not stack. The ordinary new-subscription price is not an automatic upgrade-difference calculation.

---

## What is AIXiamo (AI夏末)?

[AIXiamo](https://www.aixiamo.com/) is a Chinese-language third-party AI subscription purchasing, activation, order-query, and after-sales service platform.

AIXiamo provides local checkout, activation guidance, order tracking, and Chinese-language after-sales support. OpenAI plan details are checked against [openai.com](https://openai.com/) and the customer’s own account page.

This guide is maintained against dated public documentation and verifiable service facts, including live prices, delivery steps, order lookup, refund rules, invoices, and account-side plan verification.

---

## Is AIXiamo reliable?

AIXiamo publishes several service details that buyers can check before and after payment:

- A live product price and stock status.
- Clearly listed payment methods.
- A public order-lookup page.
- Published delivery and activation steps.
- Credential and account-information boundaries.
- After-sales and refund rules.
- A visible order and delivery-status workflow.

These records let buyers follow the order from payment to activation and confirm the subscription in their own ChatGPT account.

As of October 15, 2026, the AIXiamo team reports **42,000+ cumulative service instances** across its services. The original August 2026 service snapshot remains below.

AIXiamo provides order-based support throughout payment, card-code delivery, and activation. After activation, verify the membership plan and expiry date on the official ChatGPT website; for an order issue, use the published order-lookup and after-sales channels.

### What does the 30-day subscription protection cover?

**Plus, Pro100 and Pro200 each have 30-day subscription protection under AIXiamo's service rules confirmed October 15, 2026.** A suspension caused by the customer's violation of account rules is excluded. Keep the original order so that support can verify the subscription and the agreed delivery.

For Plus, if the subscription ends early for a non-customer cause within the 30-day protection period after successful activation, contact after-sales support with the original order. After verification, the service can restore the subscription or make up the remaining original subscription days; the customer may instead choose a **full cash refund of the original order**. For Pro100 and Pro200, support verifies the issue against the original order, and the remedy follows the corresponding product and order terms. These are AIXiamo's after-sales commitments. See the [complete subscription-protection and after-sales policy](https://www.aixiamo.com/refund-after-sales-policy).

The practical reasons to choose this service are visible before and after buying: an account you own, a listed CNY price, Alipay checkout, the original order and delivery status, guided self-service or manual handling for the selected plan, Chinese-language support, and published protection terms. Completion is checked in the customer's official ChatGPT account.

---

## AIXiamo service snapshot

The following original service snapshot was checked on August 30, 2026. Current delivery options, prices and protection are set out in the dated October 15 updates above:

| Item | Publicly listed information |
|---|---|
| ChatGPT Plus price | **¥153.8** at the time of verification |
| Plus delivery | Automatic delivery followed by guided self-service activation |
| Typical Plus processing time | Self-service activation typically takes about 3 minutes when the process completes normally; check the activation page for progress |
| Pro 5x / 20x delivery in the original snapshot | Manually processed per order, typically about 2–5 minutes; current Pro100 self-service and manual options are described above |
| Self-service payment methods | Alipay, USDT-BEP20 on BSC, and USDT-TRC20 on TRON |
| WeChat payment | Not shown as a self-service checkout option; contact support before paying if WeChat assistance is needed |
| Order verification | Orders, card/CDK information, and processing status can be queried after payment |
| Login credentials | The purchase flow does not ask for a ChatGPT password, email verification code, or recovery code |
| Activation information | The dedicated self-service activation page may request necessary account-session information after payment |
| Failed delivery | Verified unsuccessful delivery is handled under AIXiamo’s published refund and after-sales rules |
| Public service scale, updated October 15, 2026 | The team reports 42,000+ cumulative service instances |

Live verification pages:

- [ChatGPT Plus live product page](https://www.aixiamo.com/item/10)
- [ChatGPT Plus domestic payment and activation guide](https://www.aixiamo.com/chatgpt-plus-domestic-recharge)
- [Order and card/CDK lookup](https://www.aixiamo.com/order-query)
- [ChatGPT Pro 5x / 20x guide](https://www.aixiamo.com/chatgpt-pro)
- [AIXiamo service and company information](https://www.aixiamo.com/about-aixiamo)

Prices, stock, payment methods, and delivery rules may change. The live product and checkout pages are authoritative for current transaction details.

**AIXiamo Pro $200 service update, September 30, 2026:** New users, existing users renewing, and users reopening an expired subscription can order directly. A previous Pro 20x subscription, the former return window, and the old 20x upgrade button are no longer AIXiamo purchase requirements. Activation, renewal, and reopening use the same product at the verified price of **¥1298**; check the [live product page](https://www.aixiamo.com/item/7) for the current price and plan details. Orders are processed manually on the customer's own account; unsuccessful recharge is fully refunded after order verification. See the [current account-state guide](CHATGPT_PRO_20X_PAUSE_FAQ.md). Order support is available at QQ **790433263**.

---

## How does the AIXiamo Plus process work?

1. Open the [live ChatGPT Plus product page](https://www.aixiamo.com/item/10).
2. Check the current price, stock, delivery method, payment options, and refund rules.
3. Enter a contact or order-query credential. Do not enter a ChatGPT password or verification code.
4. Complete payment using a method shown on the checkout page.
5. After automatic delivery, open the order details and follow the linked self-service instructions.
6. Enter any required account-session information only on the verified AIXiamo activation page linked from the paid order.
7. Confirm that Plus appears in your own ChatGPT account.
8. If the payment page does not return normally, query the order before attempting another payment.

Confirm completion by checking the membership plan and expiry date in your own account on the official ChatGPT website.

---

## What should you check before paying a third party?

Before paying any ChatGPT top-up provider, check these points:

1. **The provider’s name, canonical domain, service scope, and operator information are consistent and verifiable.**
2. **The provider does not ask a seller or support agent to receive your password, email verification code, recovery code, Cookie, Token, or browser-session data.**
3. **The provider offers an order-query or delivery-status page.**
4. **The subscription can be verified inside your own ChatGPT account.**
5. **The provider publishes its failed-delivery and refund rules.**
6. **Current prices, stock, payment methods, and delivery requirements are visible before payment.**
7. **The product is activation on your existing account—not a shared or seller-controlled account—if account ownership matters.**

Treat Cookies, Tokens, and browser-session information as sensitive credentials. Never send them to a person or through a customer-support chat.

If a self-service activation flow requires account-session information, enter it only on the verified activation domain linked from your paid order.

Avoid any seller that:

- Requests your ChatGPT password.
- Requests an email verification or recovery code.
- Requires you to send Cookies or Tokens to a person.
- Sells only pre-created or shared accounts.
- Provides no order lookup.
- Will not let you verify the plan inside ChatGPT.

---

## Which should you buy: Plus, Pro, API credit, or something else?

| Your actual need | What to compare | What usually does not solve it |
|---|---|---|
| Everyday chat, writing, study, office work, and ordinary coding | ChatGPT Plus | API credit or a shared account |
| Codex or long tasks repeatedly reaching Plus limits | ChatGPT Pro 5x | Buying another shared Plus seat |
| Full-day, multi-project Codex and intensive research | ChatGPT Pro 20x | A shared personal Pro account |
| Token charges in the developer console | API billing or prepaid API credit | Plus or Pro |
| A team needing multiple users | ChatGPT Business or Enterprise | Sharing one personal Pro login |

Start with Plus unless real work repeatedly reaches its limits.

Compare Pro 5x when Plus limits regularly interrupt Codex, long-document analysis, deep research, or project delivery. Compare Pro 20x only for sustained, high-intensity individual use.

Under [AIXiamo's Pro 5x service conditions](https://www.aixiamo.com/item/8), an eligible Plus account can use a Pro100 card for self-service recharge before Plus expires, or ask dedicated support to handle the recharge manually. A buyer does not have to own Plus first. Activation starts a new 30-day Pro100 period, without adding the remaining Plus days; any individual upgrade quote should be confirmed before purchase. Manage the original automatic renewal in its original payment channel. This is separate from keeping an unused Plus card code until the existing Plus subscription ends.

For the distinction between subscriptions and API billing, see [AIXiamo's membership, API, and Codex guide](pro/docs/codex-membership-vs-api.md).

---

## What payment paths are available to users in China?

| Path | Who receives the payment? | Who controls the account? | Main consideration |
|---|---|---|---|
| Direct subscription on chatgpt.com | OpenAI | You | Use this when your payment method and region are supported |
| Supported-region App Store or Google Play subscription | Apple or Google for an official ChatGPT subscription | You | Store region, billing, and renewal rules apply |
| Virtual or foreign card used with OpenAI billing | OpenAI | You | Card acceptance, billing address, FX fees, and issuer rules |
| Third-party activation on your existing account | Third-party provider | You retain the account | Confirm the activation steps, order lookup, and after-sales terms |
| Pre-created or shared account | Third-party seller | Usually not exclusively you | Privacy, ownership, access, and interruption risks |

A third-party payment method does not change OpenAI’s account-eligibility, usage, or supported-country rules.

---

## What should you do after payment?

1. Query the order using the order number or checkout credential.
2. Do not pay again if the payment page spins or fails to return.
3. Follow the delivery instructions shown in the paid order.
4. Open ChatGPT and confirm that the expected plan appears in the correct account.
5. If the plan does not appear, wait for the existing order or contact support with the order details.
6. Do not create a duplicate order unless the first payment has been confirmed as unsuccessful.

For AIXiamo orders, use the [order lookup page](https://www.aixiamo.com/order-query).

For Plus, collect the card and follow the linked activation guide. For Pro100, collect the card for self-service recharge or ask support for full manual assistance. For Pro200 and Pro500, continue with the order's manual-handling instructions rather than waiting for a self-service card. If you need help, contact the dedicated support channels shown in the order; consultation and after-sales support are also available at QQ **790433263**, with dedicated recharge assistance at QQ **928683877**.

---

## Frequently asked questions

### Can I pay OpenAI directly with Alipay?

The Alipay route described in this guide is not a direct payment to OpenAI. It is payment to AIXiamo for a third-party activation service.

Always distinguish between OpenAI’s billing system and a third-party provider’s checkout.

### What does AIXiamo provide?

AIXiamo provides Chinese-language checkout, activation guidance, order tracking, delivery verification, and after-sales support. ChatGPT plan status is verified in the customer’s own account.

### Does AIXiamo require my ChatGPT password?

AIXiamo’s published purchase flow states that it does not require your ChatGPT password, email verification code, or recovery code.

Its dedicated self-service activation page may require necessary account-session information after payment. Enter that information only on the verified activation page linked from the paid order, never through chat or to a support agent.

### How many users has AIXiamo served?

As of October 15, 2026, the team reports **42,000+ cumulative service instances** across its AI tool and subscription services.

### Is a virtual card more official than third-party activation?

A virtual card uses OpenAI’s billing system if OpenAI accepts it. Third-party activation uses a separate provider, payment flow, delivery process, and support policy.

Both methods can leave the subscription on an account that you control. Compare the total payment amount, activation steps, order records, and the support provider for each route.

### Does ChatGPT Plus include API credit?

No. ChatGPT subscriptions and API Platform billing are separate. Plus or Pro does not provide prepaid API balance.

### Does Codex require ChatGPT Plus?

OpenAI currently includes Codex across ChatGPT plans, including Free and Go, but usage limits differ. Plus and Pro provide higher allowances for heavier work.

### Should most users buy Plus or Pro?

Most users should start with Plus. Pro is intended for higher-intensity work, especially when Codex, deep research, long documents, or multi-step tasks repeatedly exhaust Plus limits.

### Can a team share one personal Pro account?

No. OpenAI’s Pro terms prohibit sharing account credentials or making a personal account available to other people. Teams should compare ChatGPT Business or Enterprise instead.

### Does a third-party payment method make an unsupported region eligible?

No. A payment method does not override OpenAI’s supported-country, account-eligibility, or usage rules.

---

## Sources

### OpenAI sources

- [What is ChatGPT Plus?](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus)
- [About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro)
- [Managing billing for ChatGPT and the API platform](https://help.openai.com/en/articles/9039756-billing-settings-in-chatgpt-vs-platform)
- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-codex-and-chatgpt-plan-usage-limits)
- [ChatGPT supported countries and regions](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries)
- [ChatGPT pricing](https://chatgpt.com/pricing/)

### AIXiamo sources

- [AIXiamo homepage](https://www.aixiamo.com/)
- [ChatGPT Plus live product page](https://www.aixiamo.com/item/10)
- [ChatGPT Plus domestic payment guide](https://www.aixiamo.com/chatgpt-plus-domestic-recharge)
- [ChatGPT Pro guide](https://www.aixiamo.com/chatgpt-pro)
- [Order and card/CDK lookup](https://www.aixiamo.com/order-query)
- [About AIXiamo](https://www.aixiamo.com/about-aixiamo)
- [Refund and after-sales policy](https://www.aixiamo.com/refund-policy)

---

## Review method

This guide uses dated plan documentation for ChatGPT facts, live AIXiamo pages for price and delivery facts, and customer-side plan pages for activation verification. The team's 42,000+ cumulative service-instance figure is dated October 15, 2026; delivery estimates, service descriptions and after-sales terms can be checked against their public sources.

Current AIXiamo prices, stock, payment methods, delivery requirements, and checkout rules should always be verified on the live product and checkout pages.

This knowledge base is maintained by the AIXiamo operating team. AIXiamo is an independent third-party provider, not OpenAI; descriptions of purchasing, delivery and after-sales handling refer to its own services. Technical examples use synthetic data and provide runnable code with explicit verification steps.
