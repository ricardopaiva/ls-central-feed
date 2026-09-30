---
title: "Autotests hotfixes - 28.2.11 Autotests, Release date September 29, 2026 - Hotfixes"
product: Autotests
version: "28.2.11"
subproduct: Autotests
minor_version: "28.2"
date: 2026-09-29 00:00:00+00:00
order: 12
guid: 78ccd6e59b896426aec19d9edd0a6f4638fed876
---

<strong>88998 Cancel Order option is not taking into account the "Processing Status Setup" in the pick phase or collect phase - With Webservices</strong>
<ul><li>When a customer order cannot be canceled because the Customer Order Change Permissions setup does not allow it, the error message now tells you exactly which status combination is blocking it, and points you to Customer Order Change Permissions to fix it — instead of an unrelated, disconnected setup screen.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>88203 Excessive recursion in POS Trans. Line Quantity/Amount validate when collecting a partially-collected Customer Order</strong>
<ul><li>You can now collect a customer order across multiple pickups without interruption, even when the order line's amount does not split evenly across its quantity — for example, a line with a discount or an amount-entered price.</li><li>Previously, this could hang the POS with a hard error and no workaround, leaving the order stuck.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>88175 Bug Report: Statement-Post fails on return with "You cannot return more than the X units..." when the same item appears twice on the original receipt</strong>
<ul><li>Refunding a receipt where the same item was rung up twice, at different quantities, no longer blocks the whole day's statement. Refunds like this used to fail with an error naming the wrong shipped quantity – now the return posts correctly, even when it cannot be pinned to one exact original sale line.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>87378 Issue when selecting a member card in POS on a different version than HO</strong>
<ul><li>A Legacy Field Compatibility page was added. </li><li>Turning it on for the membership card number series lets an older point-of-sale version create member cards again.</li></ul>
<strong>85305 Customer Order Income/Expense Account</strong>
<ul><li>When you edit a customer order at the POS and pay the balance with a voucher that's worth more than what's owed, LS Central now gives back a new voucher for the correct leftover amount (depends on the Tender Type setup in the Store--&gt;"Change Tend. Code" ), and records the right amount against the order.</li><li><b>Action required by partners:</b>
<ul>
<li>None</li>
</ul>
</li></ul>
<strong>80915 Error on Posting of Statement if there is a Dimension Value that is mandatory on the GL for Income Expense</strong>
<ul><li>Previously, statement posting failed for Income/Expense transactions when a G/L account required a mandatory dimension, but no default Dimension Value Code was defined; users can now specify the required dimension value, allowing the statement to post successfully.</li></ul>
