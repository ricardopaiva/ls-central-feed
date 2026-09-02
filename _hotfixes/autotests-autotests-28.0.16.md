---
title: "Autotests hotfixes - 28.0.16 Autotests, Release date August 4, 2026 - Hotfixes"
product: Autotests
version: "28.0.16"
subproduct: Autotests
minor_version: "28.0"
date: 2026-08-04 00:00:00+00:00
order: 30
guid: f78993536d8db0395d3b1ba1d9ea210300e42137
---

<strong>84176 RFID-Error message "Scanned item not found" during RFID return - the line has already been marked for refund so we should skip the message</strong>
<ul><li>During an RFID return, scanning a tag whose line is already fully marked for refund no longer shows a "Scanned item not found" error. Previously, on some configurations this could also trigger a repeating error dialog that made the POS unresponsive during the return.</li></ul>
<strong>83875 LS Central 28.0.8.3554 – Infocode Inputs Not Printed on Customer Order Receipts</strong>
<ul><li>Infocode inputs now printed on Customer Order receipts. When an infocode is set to <b>Print Input on Receipt</b>, the value the cashier keys in now appears on the Customer Order receipt — just as it already does on a regular sales receipt.</li><li>CustomerOrderGetV4 Web Service Updated.</li></ul>
<strong>83588 Item lines not compressing on Store Inventory Journal</strong>
<ul><li>Importing items into a Store Inventory Journal from a barcode file now fills in both the variant code and the unit of measure for every line, taken directly from the scanned barcode. With the variant code in place again, the compress lines function now works correctly.</li><li>This affects only the file import path. Lines received from Inventory Mobile are not affected, including the safeguard that blocks an unwanted unit-of-measure change when changing the unit is not allowed.</li></ul>
<strong>82526 Creating a Sandbox copy from Production - error</strong>
<ul><li>The active license check now skips Microsoft base tables and defers the validation to the unit/field level if needed.</li></ul>
