---
title: "LS Central hotfixes - 28.0.18, Release date June 2, 2026 - Hotfixes"
product: LS Central
version: "28.0.18"
subproduct: 
minor_version: "28.0"
date: 2026-06-02 00:00:00+00:00
order: 1
guid: 0522f9f37aab8affdd68d179f50c8a7b723a0152
---

<strong>82839 Add option to change RoleID for Drawers</strong>
<ul><li>New event in POS Transaction Functions.codeunit was added to update drawers to open.</li></ul>
<strong>82817 Added handling before RunBatchJob to skip queue entry processing</strong>
<ul><li>New event was added in Batch Posting Codeunit.</li></ul>
<strong>82704 Error when try to open Options of the attributes</strong>
<ul><li>An error was fixed, when opening the options of an attribute.</li></ul>
<strong>82360 AL: Shopify integration: ERR: There is error message in Response XML data</strong>
<ul><li>Collection update in shopify was fixed, to bypass limit of 250 products per collection.</li></ul>
<strong>82121 Duplicate Article Addition via QR Scan After RFID EPC Scan 2</strong>
<ul><li>There was an issue where the same EPC would be stored with different casing making the EPC not unique in the database. This was fixed. </li></ul>
<strong>81997 FBP Incorrect Reward Calculation with Fractional Quantities</strong>
<ul><li>Details not available.</li></ul>
<strong>81447 Price history cleanup</strong>
<ul><li>Event <b>OnBeforeApplyRetentionPolicyToPriceHistoryTable</b> was added to LSC InstallRetentionPolicy.</li></ul>
<strong>81382 Making a better SetWebKDSRouting</strong>
<ul><li>Making the <b>SetWebKDSRouting</b> give us errors by order and not failling the whole order when one order on the batch fails.</li></ul>
