---
title: "LS Central hotfixes - 28.0.11, Release date May 12, 2026 - Hotfixes"
product: LS Central
version: "28.0.11"
subproduct: 
minor_version: "28.0"
date: 2026-05-12 00:00:00+00:00
order: 10
guid: 2480f2c194011da1ee30e97fc0f419a10d616d08
---

<strong>81993 EFT CleanUpPrintLines should not use Background Session</strong>
<ul><li>Details not available.</li></ul>
<strong>81927 Printing error message not cleared out</strong>
<ul><li>An Action was added in the Kitchen Service Configuration page to Clear persistent POS Error Banner messages from the Kitchen Services (Standard or Web).</li><li>It can happen that they are not cleared correctly and keep on appearing on the POS.</li><li>The improved clean up logic  comes in next version.</li></ul>
<strong>81663 Item sync is deleting Compare at price</strong>
<ul><li><b>Skip Compare Price</b> option was added for Shopify to skip sending Compare price during price updates.</li></ul>
<strong>81478 New OnBeforeDeletePOSTransSusp Event</strong>
<ul><li>The event <b>OnBeforeDeletePOSTransSusp_OnDeletePOSTrans to DeletePOSTrans</b> was added in CU 99008909 LSC POS Trans. Server Utility.</li></ul>
<strong>80693 G/L entries missing CO reference number</strong>
<ul><li>GL entries were missing CO reference number when Customer Order refunded on POS.</li><li>Changed objects: Codeunit 10016655 <b>LSC CO POS Functions</b>, Codeunit 99001457 <b>LSC Statement-Post</b>.</li><li>Statement-Post: Customer Order ID was only set on <b>PostingBuffer[1]</b> inside the prepayment invoice branch. <ul><li>The assignment was moved to the end so it applies to all income/expense posting paths, and the same assignment was added in the refund amount path where it was missing entirely.</li></ul></li><li>CO POS Functions:<ul><li>When a refund is recorded on POS, Pre Approved Amount and Pre Approved Amount LCY are now zeroed out on the payment record to prevent stale values from carrying into statement posting.</li></ul></li><li>No schema changes. No new objects.</li></ul>
<strong>80282 UOM Change issue on Mobile Inventory</strong>
<ul><li>In Store Inventory the Default Unit of Measure (UoM) is set in the Store Inventory Worksheet Setup.<ul><li>It can be base unit of measure, sales UoM or Purchase UoM.</li><li>When Item number or Serial number is entered in a journal line then UoM is set automatically according to the default. If <b>Change UoM Allowed</b> is set, then the user can change the UoM manually.</li></ul></li><li>When journal lines are imported via web request <b>StoreInvTransactionSend</b> then if no Uom is set the default UoM is assigned automatically.<ul><li>If UoM is provided, then it is validated according to the default UoM.</li><li>If it is not the default and Change UoM is not allowed, then an error is raised.</li><li>If UoM is provided that is not a UoM for the Item an error is raised.</li></ul></li></ul>
