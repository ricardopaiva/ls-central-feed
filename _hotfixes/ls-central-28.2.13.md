---
title: "LS Central hotfixes - 28.2.13, Release date October 6, 2026 - Hotfixes"
product: LS Central
version: "28.2.13"
subproduct: 
minor_version: "28.2"
date: 2026-10-06 00:00:00+00:00
order: 2
guid: 53391e537996737aa6d574baf4710598fc9a029b
---

<strong>88998 Cancel Order option is not taking into account the "Processing Status Setup" in the pick phase or collect phase - With Webservices</strong>
<ul><li>When a customer order cannot be canceled because the Customer Order Change Permissions setup does not allow it, the error message now tells you exactly which status combination is blocking it, and points you to Customer Order Change Permissions to fix it — instead of an unrelated, disconnected setup screen.</li><li>None.</li></ul>
<strong>88298 New event into SendWholeTmpTransaction function in the "LSC POS Trans. Server Utility"</strong>
<ul><li>New integration event was added to POS Transaction Server Utility: OnAfterSendWholeTmpTransaction_TSSendTransaction.</li></ul>
<strong>88203 Excessive recursion in POS Trans. Line Quantity/Amount validate when collecting a partially-collected Customer Order</strong>
<ul><li>You can now collect a customer order across multiple pickups without interruption, even when the order line's amount does not split evenly across its quantity — for example, a line with a discount or an amount-entered price. Previously, this could hang the POS with a hard error and no workaround, leaving the order stuck.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>88188 New event for the GetPostedTransaction function in the ""LSC POS Trans. Server Utility"</strong>
<ul><li>New event was added, OnAfterGetPostedTransaction in Codeunit POS Transaction Server Utility.</li></ul>
<strong>88175 Bug Report: Statement-Post fails on return with "You cannot return more than the X units..." when the same item appears twice on the original receipt</strong>
<ul><li>Refunding a receipt where the same item was rung up twice, at different quantities, no longer blocks the whole day's statement. Refunds like this used to fail with an error naming the wrong shipped quantity – now the return posts correctly, even when it cannot be pinned it to one exact original sale line.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>88171 added OnBeforeSkipRecord event to handle custom skipping logic</strong>
<ul><li>New event OnBeforeSkipRecord was added on Schedule Batch Posting codeunit.</li></ul>
<strong>88170 Store Inventory Management - Event</strong>
<ul><li>New event was added, OnBeforeInsertInStoreStockReqHeader in Codeunit Store Inventory Management.</li></ul>
<strong>87822 Request to add publisher event OnBeforeCalculateMemberPoints (with IsHandled) in codeunit 99009012 "LSC Upgr./Downgr. Management"</strong>
<ul><li>New event, was added OnBeforeCalculateMemberPoints  in codeunit 99009012.</li></ul>
<strong>87781 V28 Card Payment Only Attempting Once Instead of Three Attempts</strong>
<ul><li>There was a  bug where card payments at the POS were not retrying up to the configured number of attempts. This was fixed. </li></ul>
<strong>87652 Franchise Inbound Purchase Return Order Processing Error after upgrade to LS Central 28.2.4.4005</strong>
<ul><li>Retail purchase return orders sent to a franchiser now process successfully when the return confirmation comes back from the franchiser. Previously, some of these inbound messages failed with an error saying you could not return more than a certain number of units, leaving the purchase return order stuck in an error state until support stepped in.</li><li><b>Action required by partners:</b>
<ul>
<li>None. Purchase return orders already stuck in an error state from this issue can be reprocessed (Process Now) once the fix is installed.</li>
</ul>
</li></ul>
<strong>87378 Issue when selecting a member card in POS on a different version than HO</strong>
<ul><li>
<p>Added a Legacy Field Compatibility page. Turning it on for the membership card number series lets an older point-of-sale version create member cards again.</p>
</li></ul>
<strong>86970 Job queue entries not working / Background session in V28 issue</strong>
<ul><li>Job queues no longer stall when sending POS e-receipt emails.</li><li>Sending e-receipt and customer-order emails from the back office no longer starts POS background sessions for every till in head office. Job queues that process these emails now run reliably instead of stalling.</li><li>On busy head-office setups, processing pending email requests could spin up background sessions for each POS at once, exhausting available sessions and blocking the job queue — and other job queues under the same user — from running. This was most visible after upgrading to version 28. Emails now send without that overhead.</li><li>Suppresses the POS background sessions (send transaction, Azure Storage replication, job-queue refresh) only while the back-office <b>Process Pending Requests</b> job runs; normal POS behavior is unchanged.</li><li><b>Action required by partners:</b>
<ul>
<li>None — the fix applies automatically after upgrade.</li>
</ul>
</li></ul>
<strong>85305 Customer Order Income/Expense Account</strong>
<ul><li>When you edit a customer order at the POS and pay the balance with a voucher that's worth more than what's owed, LS Central now gives back a new voucher for the correct leftover amount (depends on the Tender Type setup in the Store--&gt;"Change Tend. Code" ), and records the right amount against the order.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>82225 Printing A5 in version 27</strong>
<ul><li>Reports sent to a hardware station printer now print with the paper kind you have actually set up for that printer.</li><li>Previously, any printer not set to a custom paper kind defaulted to A4, so A5 and other non-default paper sizes printed on the wrong paper or failed outright.</li><li><b>Action required by partners:</b>
<ul>
<li>None — printers already configured with a non-A4, non-custom paper kind print correctly again once the fix ships; no setup changes needed.</li>
</ul>
</li></ul>
<strong>80915 Error on Posting of Statement if there is a Dimension Value that is mandatory on the GL for Income Expense</strong>
<ul><li>Previously, statement posting failed for Income/Expense transactions when a G/L account required a mandatory dimension, but no default Dimension Value Code was defined; users can now specify the required dimension value, allowing the statement to post successfully.</li></ul>
