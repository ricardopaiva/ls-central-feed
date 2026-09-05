---
title: "LS Central hotfixes - 28.2.4, Release date August 17, 2026 - Hotfixes"
product: LS Central
version: "28.2.4"
subproduct: 
minor_version: "28.2"
date: 2026-08-17 00:00:00+00:00
order: 3
guid: 2c40c1fd931aac0cafa9bf1d5d61d5f11e387eee
---

<strong>86325 Returning transaction based on transaction with both sales entry and income expense fails</strong>
<ul><li>Returning a POS transaction that generated a Customer Order and a Sales Order, with both a sales entry and an income/expense entry no longer fails with <b>The POS Trans. Line already exists</b> error.</li></ul>
<strong>86214 Update and add integration event</strong>
<ul><li>Added integration events:<ul><li>OnBeforeDelRecord (POS Trans. Lines)</li><li>OnAfterSetVariantCode_OnItemLine (POS Transaction Events)</li><li>and extended OnAfterTSDataEntries_TypeCreateDataEntry (POS Infocode Utility</li><li>new ReturnValue parameter).</li></ul></li></ul>
<strong>85603 Update access modifier and add new method</strong>
<ul><li>Procedure GetConnectionLog was added in Request Handler codeunit to access ConnectionLog_g.</li></ul>
<strong>85373 Declare Tender as Currency</strong>
<ul><li>Operators can now declare foreign-currency tenders and the keypad opens, fixing a silent failure that occurred when no currency setup rows existed for that tender type.</li></ul>
