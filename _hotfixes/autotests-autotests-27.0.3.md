---
title: "Autotests hotfixes - 27.0.3 Autotests, Release date November 4, 2025 - Hotfixes"
product: Autotests
version: "27.0.3"
subproduct: Autotests
minor_version: "27.0"
date: 2025-11-04 00:00:00+00:00
order: 41
guid: fb8732f6a42d4c87233e87904a34112700201aa6
---

<strong>73631 Table List POS Startup performance enhancements</strong>
<ul><li>Performance was enhanced when retrieving dining table status information for graphical, button grid, and list layouts.</li><li>In the dining table list layout, using a data table with source expressions previously caused slow grid performance. Now, if the data table does not include these source expressions, an optimized process is used to populate the grid, resulting in faster loading times.</li><li>To benefit from these improvements, update the data table for the dining table list layout as described in the <b>Performance Improvements for Dining Table List</b> section of the online help.</li><li>A new event to set filters when the staff logs on was added to the dining table list handling codeunit, Table List POS Startup:  <b>OnAfterSetStaffInfoSetGridFilters</b>. Instead of showing all dining tables when logging on, the list can show free tables, or tables that belong to the staff member and so on.</li></ul>
<strong>72426 SC-2739-EPC & RFID Scanned not there in Voided Trans. line</strong>
<ul><li>Details not available.</li></ul>
