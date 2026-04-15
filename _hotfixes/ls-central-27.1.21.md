---
title: "LS Central hotfixes - 27.1.21, Release date April 10, 2026 - Hotfixes"
product: LS Central
version: "27.1.21"
subproduct: 
minor_version: "27.1"
date: 2026-04-10 00:00:00+00:00
order: 2
guid: da7c17f239f494b94cc59edabd1f5506af2adf26
---

<strong>80225 Extend Enums for Retail Budget #642</strong>
<ul><li>The following enums related to Retail Budgets and Open-to-Buy have been made extensible:<ul><li>LSC Open-to-Buy Type</li><li>LSC Budget Line Type</li><li>LSC Budget Type</li><li>LSC Retail Budget Line Type</li></ul></li><li>LSC Open-to-Buy Type</li><li>LSC Budget Line Type</li><li>LSC Budget Type</li><li>LSC Retail Budget Line Type</li></ul>
<strong>80224 Integration Events for Vendor Performance Management #632</strong>
<ul><li>The following integration events were added to codeunit <b>LSC Vendor Performance Mgt.</b>, which are accessible through the public codeunit <b>LSC Vendor Perf. Mgt. Public</b>:<ul><li>OnUpdatePOReceiptOnBeforeProcessVendorPerfLine</li><li>OnUpdatePostedInvoiceOnBeforeProcessVendorPerfLine</li></ul></li><li>OnUpdatePOReceiptOnBeforeProcessVendorPerfLine</li><li>OnUpdatePostedInvoiceOnBeforeProcessVendorPerfLine</li></ul>
<strong>80186 Concurrency on KDS WS log table</strong>
<ul><li>A safety net on concurrency for Logs was added. </li></ul>
<strong>79980 EventSubscriber needed for LSC POS Transaction Impl Codeunit - Procedure name SuspendTransWithSalesType LS Central OnPrem Version 27.1</strong>
<ul><li>New event, <b>SuspendTransWithSalesTypeOnAfterPrepaymentLines</b> was added to <b>LSC POS Transaction Impl</b> codeunit.</li></ul>
<strong>79918 Integration Event to Check if Item is Excluded from Replenishment</strong>
<ul><li>The integration event <b>OnBeforeIsItemExcludedFromReplenishment</b> was added to codeunit <b>LSC Replen. Calculation</b>.</li></ul>
<strong>79915 There is a retrocompatibility issue on CO's Picking with the 25.3 version synching to RC 28</strong>
<ul><li>Details not available.</li></ul>
<strong>79913 Integration Events to Check Item and Variant for Replenishment Calculation</strong>
<ul><li>The following integration events were added to codeunit <b>LSC Replen. - Calc. Qtys</b>, which are accessible through the public codeunit <b>LSC Replen. Calc. Qtys Public</b>:<ul><li>OnBeforeShouldPlanItem</li><li>OnBeforeShouldPlanVariant</li></ul></li><li>OnBeforeShouldPlanItem</li><li>OnBeforeShouldPlanVariant</li></ul>
<strong>79822 Statement left open after posting</strong>
<ul><li>An error was fixed in the statement posting process. The statement gets posted, but the open statement is not removed.</li><li>The open empty statement can now be deleted manually without an error.</li></ul>
<strong>79693 Customer Order Details Showing pending Amount</strong>
<ul><li>Calculate Non-Refundable Amount in Posted Customer Order Details Infopanel.</li></ul>
<strong>79686 Not possible to add web request to functionality profile</strong>
<ul><li>The error when adding a new POS Functionality Profile Web Request and Web Server was fixed. </li></ul>
<strong>78278 Variants vs UOM selection on POS</strong>
<ul><li>Details not available.</li></ul>
