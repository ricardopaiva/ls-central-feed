---
title: "LS Central hotfixes - 28.2.2, Release date August 11, 2026 - Hotfixes"
product: LS Central
version: "28.2.2"
subproduct: 
minor_version: "28.2"
date: 2026-08-11 00:00:00+00:00
order: 4
guid: d0dd3fc5bd46b75f8e30f93f744bc27b1a1cddb6
---

<strong>86121 KOT Line Qty had a different type from the table, making the KOTs route to be not routed</strong>
<ul><li>Kitchen Order Tickets (KOTs) with item lines that had a decimal quantity failed to update their KOT status in LS Central. As a result, orders never reached <b>served</b> status and were not cleaned up from the Web KDS database. This was fixed.</li></ul>
<strong>85982 Subscribe to Web Service 250 character limit</strong>
<ul><li>Details not available.</li></ul>
<strong>85732 Average Cost Issues in Recipes Due to Refund Postings</strong>
<ul><li>Refunding a recipe item at the POS no longer throws off its average cost. Previously, refunding a recipe — whether to cash or to a customer account — could post the recipe and its ingredients with an inconsistent quantity, pushing the average cost calculation to an invalid value and sometimes causing a cost adjustment error.<ul><li>Refunds now post correctly, and average cost stays accurate.</li></ul></li><li><b>Action required by partners:</b>
<ul>
<li>None. This corrects postings going forward — it does not retroactively fix average cost on entries posted before upgrading; stores that hit the overflow error historically may want to review cost entries for those items.</li>
</ul>
</li></ul>
<strong>85625 Skip "No routing" for item error message</strong>
<ul><li>The POS no longer shows a routing error banner when an item is intentionally left without a kitchen route for a given sales type. You still see <b>No Routing</b> on the KOT and "NR" in the journal for these items, so you can confirm routing status without an interrupting popup.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>83950 [CAS-15533-Z5H7] POS SaaS - Deal Modifier Qty. per UOM Incorrect on POS Transaction Line, Sales Entries, and Item Ledger Entries</strong>
<ul><li>Deal modifiers set up with a quantity per unit of measure greater than 1 now sell the full amount.</li><li>Before, a modifier configured for example, 3 ounces of a spirit only recorded 1 unit on the receipt, so sales totals, tax, and inventory understated what was actually poured or used.</li><li><b>Action required by partners:</b>
<ul>
<li>None. No setup change is needed after updating.</li>
</ul>
</li></ul>
<strong>83793 CO Prepayment Invoice</strong>
<ul><li>You can now reduce an item’s quantity — or remove it entirely — on a customer order at the POS when prepayment invoicing is turned on, without hitting an error. Prepayment invoices and credit memos stay in step with your change, so cancelling a whole order no longer posts a duplicate prepayment credit or invoice.</li><li style="font-weight: bold;">Action required by partners:<ul><li style="font-weight: normal;">None. No setup or configuration changes are needed.</li></ul></li></ul>
<strong>81440 EMAIL_C command not working</strong>
<ul><li>Details not available.</li></ul>
<strong>79594 Store Coupon and Manufacture Coupon</strong>
<ul><li>Previously, in Store Coupon and Manufacture Coupon code is not able to create new code by number series set in HO store. This was fixed.</li></ul>
