---
title: "LS Central hotfixes - 28.2.6, Release date September 1, 2026 - Hotfixes"
product: LS Central
version: "28.2.6"
subproduct: 
minor_version: "28.2"
date: 2026-09-01 00:00:00+00:00
order: 1
guid: 5cf49a7b046c1c370313a95b147f3bb9fd2cf9e9
---

<strong>86876 Cancel item on CO with Prepayment Invoice</strong>
<ul><li>Voiding a line on a fully prepaid, multi-line Customer Order now completes correctly.</li><li>Previously, if another line on the same order was still open when a line was voided, finalizing the order could fail with <b>There is nothing to post because the document does not contain a quantity or amount</b>, because the system attempted to recreate a prepayment invoice for an order that was already fully invoiced.</li><li>The Customer Order prepayment invoice logic (LSC CO Prepayment Invoice Mgt) now checks whether there is a genuine uninvoiced prepayment amount left before attempting to recreate the invoice, and skips it cleanly when there is none -- matching the credit-memo-side guard already shipped for this scenario.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>86585 Codeunit 99008906 "LSC POS Price Utility" needs corrected event "OnBeforeSelectMultibuy" in the "SelectMultibuy" function!</strong>
<ul><li>Parameter ReturnValue: boolean added in OnBeforeSelectMultibuy in POS Price Utility.</li></ul>
<strong>86402 Changing quantity on deal including deal modifiers with added amount</strong>
<ul><li>When you change the quantity of a deal that includes a deal modifier with an added amount, the price now correctly reflects that added amount at every quantity.</li><li>Previously, increasing the quantity after choosing a paid modifier could quietly shrink or drop the added amount from the total.</li><li><b>Action required by partners</b>:<ul><li>None.</li></ul></li></ul>
<strong>86165 SC-4636-Events needed in LS Central v25</strong>
<ul><li>The OnBeforePrintLineFormatString event has new SectionID and NodeName parameters.</li><li>New overload procedure PrintLine with SectionID and NodeName parameters.</li><li>PrintTenderDeclSlip, PrintTenderDeclLines and PrintRemoveAddTenderLines now trigger new PrintLine overload.</li><li>The OnBeforePrintInfoCodeLine event has new ICode and ISubCode parameters.</li></ul>
<strong>85285 Mobile POS replicates wrong staff permissions after full device resync (manager privileges denied)</strong>
<ul><li>Staff with manager privileges can once again void transactions, process returns, and complete sales on Mobile POS. Previously, on a device that cleared its database and did a full resync, everyone in a store could be replicated with the wrong permissions — copied from a single staff record — so managers were wrongly told they don't have manager privileges. Now each staff member's own permissions replicate to the device correctly.</li><li><b>Action required by partners</b>
<ul>
<li>Update to a build that includes this fix, then let devices replicate. Corrected permissions apply on the next sync — no manual cleanup needed.</li>
<li>If a device was worked around by manually deleting rows from its local permission table, no further action is needed.</li>
<li>Affected versions: 28.0 and 28.1 (also in latest).</li>
</ul>
</li></ul>
<strong>85142 POS Return – Reason Infocode selection not triggered when returning by receipt / from transaction list</strong>
<ul><li>Reason infocode now appears for receipt and transaction-list returns.</li></ul>
<strong>84501 Bugfix: do not use ItemUOMBuffer.Code when generating item labels</strong>
<ul><li>Generating item labels through the scheduler no longer fails for items that lack the unit of measure last used during shelf label generation.</li></ul>
