---
title: "LS Central hotfixes - 27.1.19, Release date March 27, 2026 - Hotfixes"
product: LS Central
version: "27.1.19"
subproduct: 
minor_version: "27.1"
date: 2026-03-27 00:00:00+00:00
order: 4
guid: 9a3fd4ca9047f49d5be64be768fd6ecb2be9a5a1
---

<strong>80015 Events for Replen. Journal Calculation</strong>
<ul><li>The following integration events were added to the relevant objects:<ul><li><b>Codeunit LSC Replen. Calc. Wrapper</b><ul><li>OnBeforeDeleteReplenJournalBatchAndTemplate</li></ul></li><li><b>Report LSC Add Items to Replen. Jrnl</b><ul><li>OnCleanupSessionsAndDataOnBeforeDeleteReplenJournalBatchAndTemplate</li></ul></li></ul></li><li><b>Codeunit LSC Replen. Calc. Wrapper</b><ul><li>OnBeforeDeleteReplenJournalBatchAndTemplate</li></ul></li><li>OnBeforeDeleteReplenJournalBatchAndTemplate</li><li><b>Report LSC Add Items to Replen. Jrnl</b><ul><li>OnCleanupSessionsAndDataOnBeforeDeleteReplenJournalBatchAndTemplate</li></ul></li><li>OnCleanupSessionsAndDataOnBeforeDeleteReplenJournalBatchAndTemplate</li></ul>
<strong>80001 Manual card refund not working</strong>
<ul><li>While performing a manual refund on the POS and if <b>Use Refund Payment Selection</b> is active (on POS Terminal Card) the POS does not allow the refund and displays an error saying that no card payments are found to be repaid. This was fixed.</li></ul>
<strong>79911 Replenishment Events</strong>
<ul><li>Codeunit <b>LSC Replen. - Calc. Qtys</b>, with the events accessible via the public codeunit <b>LSC Replen. Calc. Qtys Public</b>.<ul><li>OnAfterFilterSalesHistoryAdjustment</li><li>OnAfterCalcDailySales_SetFilterForItemLedgerEntry</li></ul></li><li>OnAfterFilterSalesHistoryAdjustment</li><li>OnAfterCalcDailySales_SetFilterForItemLedgerEntry</li><li>
<p>Codeunit <b>LSC Replen. Calculation</b></p>
<ul>
<li>
<p>The event <b>OnInsertWorksheetLineOnBeforeSetReplenJournalLinesPar</b> is deprecated and replaced with <b>OnInsertWorksheetLineOnBeforeSetReplenJournalLinesParV2</b>, added with an additional parameter ReplenItemQuantity.</p>
</li>
</ul>
</li><li>
<p>The event <b>OnInsertWorksheetLineOnBeforeSetReplenJournalLinesPar</b> is deprecated and replaced with <b>OnInsertWorksheetLineOnBeforeSetReplenJournalLinesParV2</b>, added with an additional parameter ReplenItemQuantity.</p>
</li></ul>
<strong>79869 EventSubscriber needed for LSC POS Transaction Impl Codeunit - Procedure name CouponPressed LS Central OnPrem Version 27.1</strong>
<ul><li>New events <b>OnBeforeCouponCodeNextItem</b> and <b>OnAfterCouponTenderType</b> were added to <b>LSC POS Transaction Impl</b> codeunit.</li></ul>
<strong>79849 AL: Limit text size from shopify</strong>
<ul><li>The length of Text values in JSON data coming from Shopify was limited to match Central Text/Code length.</li></ul>
<strong>79782 New integration events for Pharmacy</strong>
<ul><li>New event <b>OnBeforeUpdateCOLineOnUpdateOrderLines</b> was added to <b>LSC CO Web Service Func Impl</b> codeunit and event <b>OnBeforeCalculateCompressedQuantityForPicking</b> was added to <b>LSC CO Picking Panel</b> codeunit.</li></ul>
<strong>79772 New Event on Activity Matrix Data JSON codeunit</strong>
<ul><li>New event when populating matrix waiting list.</li></ul>
<strong>79736 EventSubscriber needed for LSC POS Transaction Impl Codeunit LS Central OnPrem Version 27.1</strong>
<ul><li>New events <b>OnBeforeTempPOSTransInsert</b> and <b>OnBeforeProcessSalesPerson</b> were added to <b>LSC POS Transaction Impl</b> codeunit.</li></ul>
<strong>79731 ECOM 26.1 FactBox & rounding issue</strong>
<ul><li>Incorrect tax amount was fixed in Posted Customer Order FactBox.         │</li><li>Invoice rounding amount on Customer Order returns was fixed. </li></ul>
<strong>79726 Wrong "Status Difference" = "Not ordered" in "Retail Receiving" Document when using variants</strong>
<ul><li><b>Status Difference</b> was fixed in Retail Receiving document when using variants.</li></ul>
<strong>79709 Price Update not rounded correctly in Sales Price List Line</strong>
<ul><li>When lines are entered manually or imported from an Excel sheet in <b>Sales Price List</b> line, rounding is according to <b>Unit-Amount Rounding precision</b> setup in General Ledger Setup.</li></ul>
<strong>79603 EventSubscriber needed for LSC POS Controller Codeunit - Procedure name StaffPressed LS Central OnPrem Version 27.1</strong>
<ul><li>IsHandled parameter was added to event <b>OnBeforeStaffLogonV2</b>.</li></ul>
<strong>79599 Added OnAfterCreateReturnKeyValue integration event to codeunit "LSC POS DataSet Utility".</strong>
<ul><li>New integration event <b>OnAfterCreateReturnKeyValue</b> fires at the end of the CreateReturnKeyValue procedure in codeunit 99001565 <b>LSC POS DataSet Utility</b>.</li><li>The event provides the resolved RecRef and computed KeyVal, allowing subscribers to inspect and override the return key value.</li><li>Event signature: OnAfterCreateReturnKeyValue(RecordIDText: Text; var KeyVal: Code[60]; var RecRef: RecordRef)</li><li>Partners extending POS DataSet lookup behavior can now subscribe to this event to customize key value resolution without modifying the standard code.</li></ul>
<strong>79328 Payment Lines Removed When Order Edit Fails</strong>
<ul><li>Payment lines were removed from Customer Orders when a Customer Order Edit failed to process due to errors (such as., increasing quantity). This affected Customer Orders created from Shopify or Magento.</li><li>LS Central now preserves existing payment lines if the update fails, preventing paid orders from appearing unpaid.</li></ul>
<strong>79224 EventSubscriber needed for LSC POS Transaction Codeunit - LS Central OnPrem Version 27.1</strong>
<ul><li>Details not available.</li></ul>
<strong>55093 Customer Orders - Bank Transfer</strong>
<ul><li>Incorrect refund line was fixed in <b>Posted Customer Order</b> when the Customer Order was paid with <b>Bank Transfer tender</b> type.</li></ul>
