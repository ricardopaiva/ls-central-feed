---
title: "LS Central hotfixes - 28.0.7, Release date April 28, 2026 - Hotfixes"
product: LS Central
version: "28.0.7"
subproduct: 
minor_version: "28.0"
date: 2026-04-28 00:00:00+00:00
order: 19
guid: 5963ae199e039dac61392abe0e4556e360bc66aa
---

<strong>81446 Item Transfer Allowed Across Waiters Despite Restriction Setting</strong>
<ul><li>Event <b>OnBeforeOrderTransferToOK</b> was added to <b>LSC Hosp. Transfer Functions codeunit</b>.</li><li>Subscribe to <b>Hosp. Trans. Func. Events</b> codeunit, <b>OnBeforeOrderTransferToOK</b>, to control to which table or order it is allowed to transfer an order or order lines.</li></ul>
<strong>81371Integration Event for Retrieving Unit Price in Replenishment Journal</strong>
<ul><li>The integration event <b>OnBeforeFindUnitPrice</b> was added to the codeunit <b>LSC Replen. Calculation</b>.</li></ul>
<strong>81340 KOT Header Table Locking During Concurrent POS Posting, LS Central 27.0, On-Premise</strong>
<ul><li>Details not available.</li></ul>
<strong>80918 Integration Events for Purchase Documents in Allocation Plan</strong>
<ul><li>The following integration events have been added to codeunit <b>LSC Alloc. Plan Utils</b>, which are accessible through the public codeunit <b>LSC Alloc. Plan Utils Public</b>:<ul><li>OnCreateDocsFromAllocPlanOnBeforeModifyPurchaseHeader</li><li>OnCreateDocsFromAllocPlanOnBeforeInsertPurchaseLine</li><li>OnCreateDocsFromAllocPlanOnBeforeReleasePurchaseDoc</li><li>OnCreatePOBufferLinesAndHdrsOnBeforeInsertPurchaseHeaderBuffer</li><li>OnCreatePOBufferLinesAndHdrsOnBeforeInsertPurchaseLineBuffer</li></ul></li></ul>
<strong>79917 Error message after click on Pay button(POS) and wrong behaviour on clicking Total</strong>
<ul><li>Voiding process was overrided for <b>IncomeExpense</b> lines on calculating Retail Charge in POS.</li><li>Requires LSCentral hotfix.</li></ul>
<strong>79466 LS License Manager You need to activate message</strong>
<ul><li>The <b>You need to activate an LS Central license</b> message no longer appears on environments that obtain their license unit from a Head Office via the <b>GetLicenseUnit webservice</b> (RemotePOS sessions).</li></ul>
