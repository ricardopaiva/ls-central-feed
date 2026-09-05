---
title: "LS Central hotfixes - 28.2.1, Release date August 4, 2026 - Hotfixes"
product: LS Central
version: "28.2.1"
subproduct: 
minor_version: "28.2"
date: 2026-08-04 00:00:00+00:00
order: 5
guid: 923f2c3d2918f3b4d5073b215f0bb2af87f79a7f
---

<strong>85667 New Event-Publisher on TenderDeclaration #692</strong>
<ul><li>A new integration event, OnBeforeValidateSafeAmount_OnSafePressed, is raised on the Tender Declaration when a safe amount is entered.</li></ul>
<strong>85577 Issue with call center</strong>
<ul><li>Take an order in an offline Call Center and the selected restaurant's POS now opens, ready for you to enter items. Modifying the lines on an existing Call Center order works the same way. Previously both actions returned you to the Call Center main page without opening the POS.</li><li><b>Action required by partners</b>: None. Update to a build that includes this fix.</li></ul>
<strong>85528 make procedure GetSingleTableBuffersByItemDist in codeunit-i "LSC Commerce Req. Functions" publicly available.</strong>
<ul><li>Made procedure GetSingleTableBuffersByItemDist in codeunit "LSC Commerce Req. Functions" publicly available.</li></ul>
<strong>85497 Update POS Post Utility #688</strong>
<ul><li>Adds a new event that fires after the Trans. Payment Entry is inserted while writing the transaction to the database, in the POS Post Utility codeunit.</li></ul>
<strong>85300 Sales Type location not working in version 28</strong>
<ul><li>Sales Type location is now respected when posting POS sales and refunds; returns against an original receipt still post to the store handling the return.</li></ul>
<strong>85150 Update access modifiers and add integration event #684</strong>
<ul><li>Exposes a set of previously internal barcode, offer, coupon, POS and web-service procedures for external extensions, and adds an integration event that fires per line during POS statement posting.</li></ul>
<strong>84875 DIMENSION ERROR DURING RETAIL TRANSFER ORDER POST RECEIPT</strong>
<ul><li>You can now post a retail transfer order receipt without a dimension error when the receiving store doesn't have its own default value for a dimension the item requires.</li></ul>
<strong>84710 Stores can view and modify other stores worksheets.</strong>
<ul><li>A user working on a Store Inventory Journal can no longer access other stores' journals by changing or clearing filters. Also fixed an issue where duplicating the browser page, or changing the region on the My Settings page, opened a new browser window without filters.</li></ul>
<strong>84633 Deadlock on LSCSendSerialCoupon causes double transactions in database</strong>
<ul><li>Fixed an issue where a failed serial coupon synchronization to Head Office during POS posting could cause the same receipt to be posted twice, creating duplicate transactions in the Transaction Register. Posting now rolls back cleanly on a synchronization failure, so a retry no longer creates a duplicate.</li></ul>
<strong>84499 Adding event on POS Transaction & Commission Entry #680</strong>
<ul><li><b>New Events</b>:<ul><li>OnBeforeGetBalanceInCurrencyKeyPressed, in the POS Transaction codeunit</li><li>Several new events in Commission Entry</li></ul></li></ul>
<strong>84176 RFID-Error message "Scanned item not found" during RFID return - the line has already been marked for refund so we should skip the message</strong>
<ul><li>During an RFID return, scanning a tag whose line is already fully marked for refund no longer shows a "Scanned item not found" error. Previously, on some configurations this could also trigger a repeating error dialog that made the POS unresponsive during the return.</li></ul>
<strong>84014 Scheduler message text overflow</strong>
<ul><li>Data Distribution scheduler jobs no longer stop with a string-length error when a source location is unreachable and the connection error message is long. Previously, when a job replicated from several source locations and one could not be reached over the network, an overly long connection error aborted the entire run before the remaining locations were processed. The error message is now shortened when it is too long to store, so the job records the failure for the affected location and continues replicating from the other locations as expected.</li><li><b>Action required by partners</b>: None.</li></ul>
<strong>83875 LS Central 28.0.8.3554 – Infocode Inputs Not Printed on Customer Order Receipts</strong>
<ul><li>Infocode inputs now printed on Customer Order receipts. When an infocode is set to <b>Print Input on Receipt</b>, the value the cashier keys in now appears on the Customer Order receipt — just as it already does on a regular sales receipt.</li><li>CustomerOrderGetV4 Web Service Updated.</li></ul>
<strong>83765 LSC Statement-Calculate: GetSerialLotSalesQty missing transaction Filters</strong>
<ul><li>Fix on calculation of qty. on hand for lot/serial items during statement calculation / posting.</li></ul>
<strong>83588 Item lines not compressing on Store Inventory Journal</strong>
<ul><li>Importing items into a Store Inventory Journal from a barcode file now fills in both the variant code and the unit of measure for every line, taken directly from the scanned barcode. With the variant code in place again, the compress lines function now works correctly.</li><li>This affects only the file import path. Lines received from Inventory Mobile are not affected, including the safeguard that blocks an unwanted unit-of-measure change when changing the unit is not allowed.</li></ul>
<strong>80187 Scheduler job sets next check date to 2 days after running when Error Handling is set to Mark With Error and Retry</strong>
<ul><li>A recurring Scheduler Job that has an Ending Time defined now schedules its next run on the correct day. Previously, a daily job with an Ending Time set and no Starting Time could push its next check date a full day too far, causing the following day to be skipped and scheduled work such as statement auto-calculation to be missed. The next check date and time are now kept within the configured run window without losing a day, and run windows that span midnight are handled correctly.</li><li><b>Action required by partners</b>: None.</li></ul>
