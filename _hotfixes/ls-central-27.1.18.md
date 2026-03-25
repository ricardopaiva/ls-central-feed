---
title: "LS Central hotfixes - 27.1.18, Release date March 24, 2026 - Hotfixes"
product: LS Central
version: "27.1.18"
subproduct: 
minor_version: "27.1"
date: 2026-03-24 00:00:00+00:00
order: 1
guid: 1f3cff00028f25caeae3fcc6511b1028b2ce05de
---

<strong>79700 Get items on store inventory worksheet error</strong>
<ul><li>There was an error when using <b>Get items</b> function on store inventory worksheet. This was fixed. </li></ul>
<strong>79696 Device Dialog Pages Cannot be closed if Add-In failed to load</strong>
<ul><li>Details not available.</li></ul>
<strong>79695 New Event - LSC Customer Order Line</strong>
<ul><li>Event, <b>OnBeforeGetVATBusPostingGroup</b> was added in Customer Order Line Table.</li></ul>
<strong>79607 EventSubscriber modification for LSC POS Post Utility Codeunit - Procedure name FindWorkShift LS Central OnPrem Version 27.1</strong>
<ul><li>There is now a new version of the event <b>OnAfterSetWorkShiftDate</b> in CU POS Post Utility.</li></ul>
<strong>79606 EventSubscriber needed for LSC BO Utils Codeunit - Procedure name STDTimeToString LS Central OnPrem Version 27.1</strong>
<ul><li>Event, <b>OnAfterSTDTimeToString</b> was added in BO Utils codeunit.</li></ul>
<strong>79604 We need to have our own posting routine from Transfer Store Inventory Worksheet</strong>
<ul><li>Parameters were added to event <b>OnBeforePostWorksheet</b> in Store Inventory Management.codeunit.</li></ul>
<strong>79602 EventSubscriber needed for LSC POS Refund Mgt. Codeunit - Procedure name ValidateReturnPolicy LS Central OnPrem Version 27.1</strong>
<ul><li>Event, <b>OnBeforeCheckReturnAction</b> was added in POS Refund Mgt.codeunit.</li></ul>
<strong>79490 Void and Copy operation allows voiding of card payments that are older than 24 hrs</strong>
<ul><li>The Void and Copy operation in the Transaction List panel allowed the user to try and void a card payment that was older than <b>today</b>.<p>The Return functionality handles returning and voiding of card payments that are older than <b>today</b> and that functionality should be used in those cases. The POS now stops the user from doing a Void and Copy if there are card payments on the sale and the sale is too old.</p></li><li>If there are no card payments on the sale the POS allows the Void and Copy operation to be run on any sale regardless of when it was created.</li></ul>
<strong>79427 Return transaction sales type code</strong>
<ul><li>Details not available.</li></ul>
