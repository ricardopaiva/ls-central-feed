---
title: "LS Central hotfixes - 28.0.26, Release date August 4, 2026 - Hotfixes"
product: LS Central
version: "28.0.26"
subproduct: 
minor_version: "28.0"
date: 2026-08-04 00:00:00+00:00
order: 1
guid: df1d89287b807ce487cdf6b2304d0d01deb11fa4
---

<strong>84710 Stores can view and modify other stores worksheets.</strong>
<ul><li>A user working on a Store Inventory Journal can no longer access other stores' journals by changing or clearing filters. Also fixed an issue where duplicating the browser page, or changing the region on the My Settings page, opened a new browser window without filters.</li></ul>
<strong>84633 Deadlock on LSCSendSerialCoupon causes double transactions in database</strong>
<ul><li>Fixed an issue where a failed serial coupon synchronization to Head Office during POS posting could cause the same receipt to be posted twice, creating duplicate transactions in the Transaction Register. Posting now rolls back cleanly on a synchronization failure, so a retry no longer creates a duplicate.</li></ul>
<strong>84361 [LSC26] Discount Calculation incorrectly for transaction retrieved from suspend</strong>
<ul><li>Fixed issue where discount is incorrectly added after retrieving a suspended transaction.</li></ul>
<strong>84176 RFID-Error message "Scanned item not found" during RFID return - the line has already been marked for refund so we should skip the message</strong>
<ul><li>During an RFID return, scanning a tag whose line is already fully marked for refund no longer shows a "Scanned item not found" error. Previously, on some configurations this could also trigger a repeating error dialog that made the POS unresponsive during the return.</li></ul>
<strong>84014 Scheduler message text overflow</strong>
<ul><li>Data Distribution scheduler jobs no longer stop with a string-length error when a source location is unreachable and the connection error message is long. Previously, when a job replicated from several source locations and one could not be reached over the network, an overly long connection error aborted the entire run before the remaining locations were processed. The error message is now shortened when it is too long to store, so the job records the failure for the affected location and continues replicating from the other locations as expected.</li><li><b>Action required by partners</b>: None.</li></ul>
<strong>83992 codeunit 10000853 "LSC POS Print Utility Impl" procedure PrintExtraIncomeExpense Changes</strong>
<ul><li>Income/Expense extra-print slips can now show the dates from the related POS data entry. When the extra print setup line for an Income/Expense account uses the %VF (Date Created) and %VT (Expiring Date) placeholders, the slip now prints those dates. Previously these placeholders were always blank on Income/Expense slips.</li></ul>
<strong>83875 LS Central 28.0.8.3554 – Infocode Inputs Not Printed on Customer Order Receipts</strong>
<ul><li>Infocode inputs now printed on Customer Order receipts. When an infocode is set to <b>Print Input on Receipt</b>, the value the cashier keys in now appears on the Customer Order receipt — just as it already does on a regular sales receipt.</li><li>CustomerOrderGetV4 Web Service Updated.</li></ul>
<strong>83765 LSC Statement-Calculate: GetSerialLotSalesQty missing transaction Filters</strong>
<ul><li>Fix on calculation of qty. on hand for lot/serial items during statement calculation / posting.</li></ul>
<strong>83588 Item lines not compressing on Store Inventory Journal</strong>
<ul><li>Importing items into a Store Inventory Journal from a barcode file now fills in both the variant code and the unit of measure for every line, taken directly from the scanned barcode. With the variant code in place again, the compress lines function now works correctly.</li><li>This affects only the file import path. Lines received from Inventory Mobile are not affected, including the safeguard that blocks an unwanted unit-of-measure change when changing the unit is not allowed.</li></ul>
<strong>69736 Issue with Optional Benefits on Customer Order in POS – UI Freezes and Items Not Added</strong>
<ul><li>Optional benefits now work on customer orders at the POS. When a total discount offer prompts you to choose optional benefits while charging to a customer order, the benefit items are added to the order as expected and the POS stays responsive — the menu no longer freezes, so you can finish the sale without reaching for the Esc key.</li></ul>
