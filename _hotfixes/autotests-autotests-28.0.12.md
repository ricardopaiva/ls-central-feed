---
title: "Autotests hotfixes - 28.0.12 Autotests, Release date June 23, 2026 - Hotfixes"
product: Autotests
version: "28.0.12"
subproduct: Autotests
minor_version: "28.0"
date: 2026-06-23 00:00:00+00:00
order: 29
guid: 9df3fb951946bbc78c6b6b357baf6e42ac670b9a
---

<strong>83601 Autotest failing on hotfix latest and hotfix 27.1</strong>
<ul><li>Autotest for CO Status Log for FreeText and IncomeExpense changed to explicitly look for CLOSED status.</li></ul>
<strong>83186 Customer Order - discount should not calculate on Sales Order</strong>
<ul><li>Customer Orders from eCommerce no longer pick up unintended discounts when converted to a Sales Order.</li><li>
<p>Previously, when a Customer Order created from a web request was converted into a Sales Order, Business Central would automatically apply the customer's discount group discount to the order lines — even when the original Customer Order had no discount. This lowered the line amounts and triggered an automatic invoice rounding line to reconcile the totals back to the original amount. Customer Orders now transfer to the Sales Order exactly as ordered: line amounts and discounts are preserved, no discount group is re-applied during conversion, and no spurious rounding line is generated.</p>
</li></ul>
<strong>83026 Staff Login Stuck on Terminal on Hybrid Server</strong>
<ul><li>Retry action was added for UpdateStaffCashStatusUtils in POS Transaction Server Utility.</li></ul>
<strong>82852 Bug — POS prompts for scale weight when scanning quantity-embedded barcode for Scale Item</strong>
<ul><li>Details not available.</li></ul>
