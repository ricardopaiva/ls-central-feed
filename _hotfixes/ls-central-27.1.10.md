---
title: "LS Central hotfixes - 27.1.10, Release date March 4, 2026 - Hotfixes"
product: LS Central
version: "27.1.10"
subproduct: 
minor_version: "27.1"
date: 2026-03-04 00:00:00+00:00
order: 1
guid: a9743abff75493e1b488f8e87ed635ba460cdd87
---

<strong>78504 EventSubscriber needed for LSC POS Functions Codeunit - Procedure name ProcessMaskSegments LS Central OnPrem Version 27.1</strong>
<ul><li>New events, <b>OnAfterProcessMaskSegmentsEmployee</b>, <b>OnBeforeInsertPOSLog</b>, <b>OnBeforeInsertTmpTrans</b>, were added.</li><li><b>Note:</b> POSSession was not added as parameter as the codeunit is single instance.</li></ul>
<strong>78255 BEO View needs to support longer text for activity/reservation/charges comments</strong>
<ul><li>There was an issue in <b>Banquet Event view</b> where comment text exceeded 200 characters and would produce an error. Now, very long comment text is split into multiple lines when viewed in the BEO view.</li></ul>
<strong>78216 Event Required to Support Custom CO Panel When CO is Edited</strong>
<ul><li>New event, <b>OnAfterGetCOHeaderInformationFromOrgCOHeader</b> was added to Customer Order Create Panel Codeunit</li></ul>
<strong>77817 Message on Statement</strong>
<ul><li>A piece of code that was missing on version 27.0 and 27.1 was added back.  Moved the check to a bit later into the code.</li></ul>
<strong>77144 Refund customer order from HO on POS with a different receipt no.</strong>
<ul><li>It is possible to refund a CO that is finalized with a Sales Order.  The receipt number of the Transaction created is now a regular receipt number, not the Sales Order Number.</li></ul>
<strong>75643 Enable System manager to alter the timeout hardcoded in Web Service Connection</strong>
<ul><li>Timeout can now be set in milliseconds in <b>Web Service Setup page</b> for Web Service Connections (V1 web requests). Default timeout is and has been 5000 milliseconds or 5 seconds.</li></ul>
<strong>74426 Wish List Integration between E-commerce LS Central</strong>
<ul><li>Details not available.</li></ul>
