---
title: "LS Central hotfixes - 28.0.19, Release date June 9, 2026 - Hotfixes"
product: LS Central
version: "28.0.19"
subproduct: 
minor_version: "28.0"
date: 2026-06-09 00:00:00+00:00
order: 7
guid: 261660f22e9a762f0c7119b4e78b49e7c0f27dd5
---

<strong>83693 Add COUpdatePayment procedure to handle payment updates in web service functions</strong>
<ul><li>The COUpdatePayment procedure cannot be called, because it is not part of the publicly exposed codeunit.</li><li>The procedure is needed for an extended customer order functionality.</li></ul>
<strong>83692 Add integration event OnBeforeUpdateOrder to allow customization of order update process</strong>
<ul><li>Details not available.</li></ul>
<strong>83690 Added COUpdatePayment to the Public CO Web Service Functions #670</strong>
<ul><li>Details not available.</li></ul>
<strong>83572 Fiscal Printer Communication Issue After Upgrade to LS Central 28</strong>
<ul><li>Details not available.</li></ul>
<strong>83552 Store Group Filter Optimization for Replenishment Journal Calculations</strong>
<ul><li>The Purchase and Transfer Replenishment Journal calculations now pre-filter Replen. Item Quantity (RIQ) records by the locations resolved from the Store Group filter before processing begins. This reduces the number of RIQ records included in the calculation, improving overall performance.</li></ul>
<strong>83527 License Issue on Printing (Activity)</strong>
<ul><li>Receipts now print correctly at the POS even when Bookings isn't licensed or in use.</li><li>Previously, after upgrading, every receipt print could stop with the message <b>Sorry, the current permissions prevented the action</b>, because the print routine always ran a Bookings-related step — even when the receipt had no booking package lines. Receipts now print normally whether or not you use Bookings.</li><li><b>Action required by partners:</b>
<ul>
<li>None. The fix applies automatically once you update to this version.</li>
</ul>
</li></ul>
<strong>83516 Procedure Access for InsertFees</strong>
<ul><li>Partners were given access to internal function InsertFees() using the hotel integration codeunit.</li></ul>
<strong>83269 New mixmatch events #667</strong>
<ul><li>In POS Price Utility codeunit few parameters were added to event <b>OnCalcMixMatchNewOnBeforeCheckWeightItem.</b></li><li> Three events were also added:<ul><li>OnCalcMixMatchNewOnBeforeAddRemainderToMmMembTmp</li><li>OnTriggerMMPopUpOnBeforeAddToMmMembTmp</li><li>OnTriggerMMPopUpOnBeforeProcessMixMatchLineGroup.</li></ul></li></ul>
<strong>83257 AL: Missing payment lines on Order Import Shopify</strong>
<ul><li>There was an issue, when orders from Shopify with mix of fulfilled and unfulfilled where pulled, caused missing payment lines in Customer Orders.</li></ul>
<strong>83186 Customer Order - discount should not calculate on Sales Order</strong>
<ul><li>Customer Orders from eCommerce no longer pick up unintended discounts when converted to a Sales Order.</li><li>
<p>Previously, when a Customer Order created from a web request was converted into a Sales Order, Business Central would automatically apply the customer's discount group discount to the order lines — even when the original Customer Order had no discount. This lowered the line amounts and triggered an automatic invoice rounding line to reconcile the totals back to the original amount. Customer Orders now transfer to the Sales Order exactly as ordered: line amounts and discounts are preserved, no discount group is re-applied during conversion, and no spurious rounding line is generated.</p>
</li></ul>
<strong>83026 Staff Login Stuck on Terminal on Hybrid Server</strong>
<ul><li>Retry action was added for UpdateStaffCashStatusUtils in POS Transaction Server Utility.</li></ul>
<strong>82921 Bug Report: Inconsistent Quantity Signs on Sales Return Order Lines Created by Statement-Post</strong>
<ul><li>Details not available.</li></ul>
<strong>82852 Bug — POS prompts for scale weight when scanning quantity-embedded barcode for Scale Item</strong>
<ul><li>Details not available.</li></ul>
<strong>82627 EFT Dialog causes "client callback after write transaction started"</strong>
<ul><li>Card payments through the EFT dialog now run cleanly to the end.</li><li>Previously, finishing a card payment could trigger a runtime error on the POS and add unnecessary processing overhead.</li><li>Payments now complete reliably and a little faster.</li></ul>
<strong>82311 Archive Transactions - Skipping archiving last transaction for Store No./POS Terminal No. combination - Fixes internal workitem 55605 #663</strong>
<ul><li>Details not available.</li></ul>
<strong>82304 LSC - Statement Posting Error For Customer Account Returns</strong>
<ul><li>Details not available.</li></ul>
<strong>82235 Manufacturer coupons reference number only allows numbers</strong>
<ul><li>Prefix error on Coupons was fixed. Now multiple Prefixes can be used with the same Reference No. as an example.</li></ul>
<strong>80741 Web KDS - LS Import Export</strong>
<ul><li>Recently added Web KDS were added to the Import/Export tool. </li><li>All Web KDS tables can now be exported and imported with the tool.</li></ul>
