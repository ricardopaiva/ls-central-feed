---
title: "LS Central hotfixes - 28.0.14, Release date May 19, 2026 - Hotfixes"
product: LS Central
version: "28.0.14"
subproduct: 
minor_version: "28.0"
date: 2026-05-19 00:00:00+00:00
order: 11
guid: 4c1d487d0c4cdc9f1c972482f894ec2e18a2c603
---

<strong>82151 GET_TABLE_DATA V1.0 web service request is never seeded into LSC WS Request / Setup tables</strong>
<ul><li>Details not available.</li></ul>
<strong>82108 Error occurs when selling an item in the POS</strong>
<ul><li>A default value is made sure to be returned  if POS functionality profile does not have a value for decimal places.</li></ul>
<strong>82104 Receipts and Kitchen tickets printing in duplicate</strong>
<ul><li>KOTs are not printed twice anymore, when they are sent from the POS, and not the KDS.</li></ul>
<strong>82022 Add integration events for discount calculations and offer processing</strong>
<ul><li>New integration events were added to support customization of POS discount calculations and offer processing.<ul><li>Sixteen new IntegrationEvent publishers were added to codeunits <b>LSC POS Offer Ext. Utility</b> and <b>LSC POS Price Utility</b>, providing hooks at key points in the discount and offer calculation flow including line pre-total processing, mix-and-match calculations, and discount blocking logic.</li></ul></li></ul>
<strong>82021 IJnlLineMirror procedure internal -> public</strong>
<ul><li>The IJnlLineMirror procedure on codeunit <b>LSC Retail ICT Processes</b> is now public.</li></ul>
<strong>81154 Current Availability Lock prevents concurrent use of AVAILABILITY_MODE from multiple POS terminals</strong>
<ul><li>When setting a <b>Current Availability</b> at POS it locks that functionality on all POS's in the same store.</li><li>If a POS crashes in edit mode, it is possible to clear the state.</li></ul>
<strong>81005 Discount on POS for Customer Order with Partial Collect Applies Full Order Line Discount</strong>
<ul><li>Details not available.</li></ul>
<strong>80632 Items with "Qty not in Decimal" = true show wrong error message when selecting the line for POS Return</strong>
<ul><li>When initiating a POS return and pressing Select on a line where the remaining quantity is a whole number (such as 1), the POS incorrectly displayed the error <b>Item X can only be sold in quantities that are whole numbers.</b> This was fixed.</li></ul>
