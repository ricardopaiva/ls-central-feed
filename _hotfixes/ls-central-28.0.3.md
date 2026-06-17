---
title: "LS Central hotfixes - 28.0.3, Release date April 21, 2026 - Hotfixes"
product: LS Central
version: "28.0.3"
subproduct: 
minor_version: "28.0"
date: 2026-04-21 00:00:00+00:00
order: 17
guid: 9996b4d685a9c6b768738bd8943cf14909c7ade5
---

<strong>80973 Add integration event for Coupon Entry in Customer Order Line</strong>
<ul><li>Integration event <b>OnAfterInsertCouponEntryOnCOLine</b> was added in the <b>CreateCouponLines</b> procedure in the Customer Order Line table.</li></ul>
<strong>80954 Availability for renting products is showing different values...</strong>
<ul><li>There was an issue with vailability for rental products showing different values due to incorrect date boundary comparisons in resource availability checks. This was fixed. </li><li>There was an issue with overnight availability date calculation when no interval type is configured. This was fixed. </li></ul>
<strong>80917 OnBeforeConstructBarcodeCharacterAdd integration event</strong>
<ul><li>Event <b>OnBeforeConstructBarcodeCharacterAdd</b> was added in LSC Barcode Management.</li></ul>
<strong>80747 New publisher OnBeforeProcessInput</strong>
<ul><li>A new event <b>OnAfterAddOneToLineQuantity_OnProcessInput</b> was added.</li></ul>
<strong>80744 OnBeforeLoadPanelDataOrLookup Param as Var</strong>
<ul><li>Parameter was changed to be passed to event <b>OnBeforeLoadPanelDataOrLookup as var</b>.</li></ul>
<strong>80742 Codeunit 10016658 "LSC CO Create Panel" CustomerOrderDeposit event parameter by Var</strong>
<ul><li>Var was added to parameter in CustomerOrderDeposit.</li></ul>
<strong>80614 EventSubscriber needed for LSC POS Transaction Impl Codeunit - Procedure name CurrencyKeyPressed LS Central OnPrem Version 27.1</strong>
<ul><li>Four new events were added in POS Transaction.</li></ul>
<strong>80599 Currency rounding issue and insufficient memory</strong>
<ul><li><b>SnapPaymentToBalanceOnCurrencyRounding</b> was added to snap payment amount to balance when the difference is within currency rounding tolerance during foreign-currency payments.</li></ul>
<strong>80483 New Publisher OnBeforeFindFilteredCOLines</strong>
<ul><li>New publisher event, <b>OnBeforeFindFilteredCOLines_GetFilteredDocList</b> was added to codeunit <b>LSC CO Web Service Functions</b>.</li><li>Raised in <b>GetFilteredDocList</b> procedure before FindSet() on Customer Order lines in the Pick/Collect panel flow. Use this event to add or modify line filters before the query executes.</li></ul>
<strong>80445 Removed error if transaction has zero table number when opening in Table List Startup</strong>
<ul><li>Error was prevented when attempting to open the POS for a POS transaction with zero table no. in <b>Table List POS Startup</b>.</li></ul>
<strong>80042 When Fully Canceling an Order the "Receipt No." and "Transaction No." on the "LSC Customer Order Status Log" is blank</strong>
<ul><li>Receipt No. and Transaction No. were not populated in the Line Status Changes FactBox when a Customer Order was fully canceled on POS.</li><li>This only affected full order cancelations, while partial cancelations worked correctly. </li><li>LS Central now ensures these values are properly assigned, improving traceability for canceled orders.</li></ul>
<strong>79850 Receipt alignment mismatch - detecting the full-width characters wrongly</strong>
<ul><li>Details not available.</li></ul>
<strong>77253 Investigate different enpoints that are used (printDialog/HttpWrapper) in binary data printing against the Hardware Station</strong>
<ul><li>Details not available.</li></ul>
<strong>77174 CO Multicurrency - Amount mismatch Error when Posting Sales Order</strong>
<ul><li>Multiple issues related to the <b>Multi Currency feature</b> were fixed. </li></ul>
<strong>74340 Statement Batch Posting Problem</strong>
<ul><li>Validation was added, if a <b>Posted Statement</b> with the same number already exist.</li><li>The <b>Open Statement</b> page is closed after posting.</li></ul>
