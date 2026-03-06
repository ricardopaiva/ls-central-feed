---
title: "LS Central hotfixes - 27.1.2, Release date February 10, 2026 - Hotfixes"
product: LS Central
version: "27.1.2"
subproduct: 
minor_version: "27.1"
date: 2026-02-10 00:00:00+00:00
order: 10
guid: 43538905d4e589fc14caed5ba7428e898e3cdc36
---

<strong>77624 AL: Contact does not get attached to Customer order</strong>
<ul><li>There was <b>Missing Card ID</b> in Customer order coming from Shopify. This was fixed. </li></ul>
<strong>77568 Integration Event for RIQ Calculation in Replenishment Journal</strong>
<ul><li>An integration event <b>OnBeforeCalculateInventory</b> was added to the report <b>LSC Add Items to Replen. Jrnl</b>.</li></ul>
<strong>77565 Expose Procedures for Allocation Plans</strong>
<ul><li>The following procedures have been exposed and made accessible for extension development:<ul><li>Procedure <b>UpdateDistributedQty</b> in codeunit <b>LSC Alloc. Plan Utils</b>, accessible via the public codeunit <b>LSC Alloc. Plan Utils Public</b>.</li><li>Procedure <b>TestQtyAgainstLimits_withErr</b> in page <b>LSC Alloc. Plan Des. Lines</b>.</li></ul></li><li>Procedure <b>UpdateDistributedQty</b> in codeunit <b>LSC Alloc. Plan Utils</b>, accessible via the public codeunit <b>LSC Alloc. Plan Utils Public</b>.</li><li>Procedure <b>TestQtyAgainstLimits_withErr</b> in page <b>LSC Alloc. Plan Des. Lines</b>.</li></ul>
<strong>77491 Overbooking settings for Dining Reservations activity product does not allow for overbooking</strong>
<ul><li>Overbooking settings are now working for dining reservations.</li></ul>
<strong>77476 Add integration event OnBeforeMakeOrderChecks to Statement-Post</strong>
<ul><li>New event  <b>OnBeforeMakeOrderChecks</b> was added to <b>LSC Statement-Post</b> codeunit.</li></ul>
<strong>77460 AL: Store Opening Hours not showing the Date name</strong>
<ul><li>Missing date name was added to GetStores WS.</li></ul>
<strong>77335 Event Request: ErrorText should be by reference (var) in event OnProcessSuspensionByState_SecErrorChecking of codeunit 99001574 "LSC POS Transaction Events"</strong>
<ul><li><b>OnProcessSuspensionByState_SecErrorChecking</b>  was obsoleted and new event <b>OnProcessSuspensionByState_SecErrorCheckingV2</b> was created with var on the ErrorText parameter.</li></ul>
<strong>76540 Not able to delete empty Statement</strong>
<ul><li>Issue regarding not being able to delete empty statements was fixed.</li></ul>
<strong>76189 LSC SK w1 events</strong>
<ul><li>Events were added to support LSC SK localization.</li></ul>
<strong>76007 AL: Option to select which Order to import</strong>
<ul><li>Shopify Order Pull filter was added to pull Order based on Payment or Fulfillment status or by Sales channel.</li></ul>
<strong>71272 Job Queue for 10016105 LSC WKS Station Kitchen Item</strong>
<ul><li>New Job Queue Entry is available for updating the Web KDS Station Kitchen Item routing automatically, for all related Stations, with regular intervals. </li><li>To populate the Job Queue Entries table, open up the <b>Kitchen Service Configuration</b> page and select the <b>Insert Job Queue Default Entries</b> Action.</li></ul>
