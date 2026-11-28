---
title: "LS Central hotfixes - 29.0.8, Release date November 24, 2026 - Hotfixes"
product: LS Central
version: "29.0.8"
subproduct: 
minor_version: "29.0"
date: 2026-11-24 00:00:00+00:00
order: 2
guid: eec1440c1e1d12f0778600831651217fd62a8cb6
---

<strong>85007 API: customerOrders - replace CustomerOrderGet/Create/Edit/Update (V3-V6) + CO Pick/sourcing/payment/status ops</strong>
<ul><li>Read and manage customer orders over a single REST/OData API, lsRetail/customerOrder/v1.0. The <b>customerOrders</b> endpoint, with its lines, payments, and discount lines, replaces the separate V3–V6 SOAP operations for reading, creating, and updating orders. You can also cancel or finalize an order and update its payment with actions. To create a full order in one call, use the new <b>RetailCOFullCreate</b> web service. The existing SOAP services keep working, so you can move over when you are ready.</li><li><b>Action required by partners:</b></li><li>  ◦ Create a separate user for each API client, with a retail user record and the correct store number. The API reads and writes only that store's orders.</li><li>  ◦ Use <b>RetailCOFullCreate</b> to create orders from the web. Web orders can't be created header-only.</li></ul>
<strong>87163 Prevent Receipts Printing on Email Copy</strong>
<ul><li>When you email a copy of a receipt or invoice from the POS, it now only sends the email — it no longer also prints a physical copy.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>88723 Would like to modify data before displayed in pos lookuplist</strong>
<ul><li>Details not available.</li></ul>
<strong>91847 Translation not working when BC language is the same as staff language and neither is english</strong>
<ul><li>Details not available.</li></ul>
<strong>91964 Store Inventory Line API - Fix error 409 by locking the Worksheet instead of Store Inventory Lines and other minor improvements</strong>
<ul><li>Send inventory lines from several mobile devices to the same worksheet simultaneously, while making the process more resilient to 429 errors ("We can't save your changes right now...").</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>92097 Add new IntegrationEvents OnAfterProcessAddBenefits</strong>
<ul><li><b>OnAfterProcessAddBenefits</b> event was added to LSC POS Transaction Events.</li><li>  ◦ LSC POS Transaction Impl: ProcessAddBenefits raises the event after the additional benefits pop-up is requested, and when there are no additional benefits.</li></ul>
<strong>92273 Integration Event for Modifying Item Variant</strong>
<ul><li>The integration event OnItemDescriptionOnAfterValidateEventOnBeforeModifyItemVariant was added to codeunit "LSC Product Ext.".</li></ul>
