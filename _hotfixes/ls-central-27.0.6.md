---
title: "LS Central hotfixes - 27.0.6, Release date November 4, 2025 - Hotfixes"
product: LS Central
version: "27.0.6"
subproduct: 
minor_version: "27.0"
date: 2025-11-04 00:00:00+00:00
order: 7
guid: f5c88db9e1ff9c4f8b7837ca7b57291ed183c1ba
---

<strong>74044 Performance changes on StoreInvTransactionSendV2 web request - II</strong>
<ul><li>Details not available.</li></ul>
<strong>73869 LSC 26.1.34 - Customer Order Currency Error</strong>
<ul><li>An issue was fixed, where the Currency Code field was incorrectly populated with the LCY code instead of being left empty.</li></ul>
<strong>73768 Integration Events For Documents Creation in Allocation Plan #583</strong>
<ul><li>The integration events <i>OnCreateDocsFromAllocPlanOnBeforeInsertPurchaseHeader</i> and <i>OnCreateDocsFromAllocPlanOnBeforeInsertSalesHeader</i> were added in the codeunit <b>LSC Alloc. Plan Utils Public</b>, used by the procedure CreateDocsFromAllocPlan in codeunit <b>LSC Alloc. Plan Utils</b>.</li></ul>
<strong>73656 Add option to skip purging of EFT Print Slip Lines when posting</strong>
<ul><li>Details not available.</li></ul>
<strong>73631 Table List POS Startup performance enhancements</strong>
<ul><li>Performance was enhanced when retrieving dining table status information for graphical, button grid, and list layouts.</li><li>In the dining table list layout, using a data table with source expressions previously caused slow grid performance. Now, if the data table does not include these source expressions, an optimized process is used to populate the grid, resulting in faster loading times.</li><li>To benefit from these improvements, update the data table for the dining table list layout as described in the <b>Performance Improvements for Dining Table List</b> section of the online help.</li><li>A new event to set filters when the staff logs on was added to the dining table list handling codeunit, Table List POS Startup:  <b>OnAfterSetStaffInfoSetGridFilters</b>. Instead of showing all dining tables when logging on, the list can show free tables, or tables that belong to the staff member and so on.</li></ul>
<strong>73609 Business Central Currency & Shopify Order import - Best practice</strong>
<ul><li>Details not available.</li></ul>
<strong>73604 ADD EVENT</strong>
<ul><li>New event, <b>OnBeforeGetVendorSetupOnUpdateItem</b> and <b>OnBeforeGetVendorSetupOnCreateItem</b> were added to <b>LSC Item Import Journal Line</b> codeunit.</li></ul>
<strong>73521 Item Templates - LS27 release build 1243</strong>
<ul><li>An issue with Item Template page where error the error <b>The type NavBoolean is unknown</b> was fixed.</li></ul>
<strong>73496 Lookup in "POS Func. Profile Web Requests" Request ID is not showing Web Request 2.0</strong>
<ul><li>Hotfix original ticket 67277 down to version 24.1.</li></ul>
<strong>72426 SC-2739-EPC & RFID Scanned not there in Voided Trans. line</strong>
<ul><li>Details not available.</li></ul>
<strong>67277 Lookup in "POS Func. Profile Web Requests" Request ID is not showing Web Request 2.0</strong>
<ul><li>Details not available.</li></ul>
<strong>7246 Opening server to server or installs pages multiple times makes the site unresponsive</strong>
<ul><li>Details not available.</li></ul>
