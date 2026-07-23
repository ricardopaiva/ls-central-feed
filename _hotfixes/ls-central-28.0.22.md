---
title: "LS Central hotfixes - 28.0.22, Release date June 30, 2026 - Hotfixes"
product: LS Central
version: "28.0.22"
subproduct: 
minor_version: "28.0"
date: 2026-06-30 00:00:00+00:00
order: 4
guid: 60e741ecc7d2e74f251d7a6aa29f1548f87fe15a
---

<strong>83567 Modify trigger on Item Distribution table (10000704) linked to Item</strong>
<ul><li>Details not available.</li></ul>
<strong>83288 Incorrect sign at start float difference</strong>
<ul><li>Details not available.</li></ul>
<strong>83230 Franchise Return Process Documentation - Error can not return</strong>
<ul><li><b>Franchise Process:</b>
<ol>
<li value="1">Franchise return processing was improved, to correctly handle return receipts from end to end.</li>
<li value="2">Return documents now flow more reliably into outbound franchise messages with clearer, consistent document mapping.</li>
<li value="3">Quantity handling for returns was refined so shipped and invoiced values are reported more accurately.</li>
<li value="4">Matching of inbound return documents to purchase returns was strengthened to reduce mislinked documents.</li>
<li value="5">Posting behavior for return quantities was improved to prevent incorrect quantity updates in some scenarios.</li>
<li value="6">Internal processing checks were expanded to improve stability during automated return document handling.</li>
</ol>
</li></ul>
<strong>83021 SC-3939-when we do refund and scans items with RFID, Item is selected but quantity is not updated</strong>
<ul><li>Details not available.</li></ul>
<strong>82935 Customer Order - Bank Transfer incorrect message</strong>
<ul><li>Customer Order - Bank Transfer incorrect message.<ul><li>There was an incorrect message when picking Customer Order on POS that had tender type Bank Transfer and was already applied. This was fixed. </li></ul></li></ul>
<strong>82881 Add telemetry to the Authenticat request on License Manager</strong>
<ul><li>License Manager API authentication calls are now traced in Application Insights to support diagnostics and usage analysis.</li></ul>
<strong>81834 Current Availability - Bug with changing quantity</strong>
<ul><li>There was an issue where changing the quantity of a transaction line did not correctly update current availability. This was fixed. </li><li>There was an issue, where ordering a deal in the Self-Service Kiosk left deal lines incorrectly inserted when an ingredient was out of stock. This was fixed. </li></ul>
<strong>79035 SSK - voided deal increases availability</strong>
<ul><li>Void order without increasing availability.</li></ul>
