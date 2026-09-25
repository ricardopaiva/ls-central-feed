---
title: "LS Central hotfixes - 28.2.10 Release date September 15, 2026 - Hotfixes"
product: LS Central
version: "28.2.10"
subproduct: 
minor_version: "28.2"
date: 2026-09-15 00:00:00+00:00
order: 3
guid: 3241c64608fa7309eff94946a7c0fbbd9e0f00b4
---

<strong>87217  Possibility to change Customer Balance Calculation</strong>
<ul><li>New event OnAfterCalculateCBalanceOverLimit added in POS Functions.</li></ul>
<strong>88010 Coupon only applied to lowest cost item</strong>
<ul><li>For coupons with Handling: Tender used in a transaction with two or more items, the coupon now consistently redeems for its full configured value.</li><li>Previously, if a lower-value item happened to be evaluated before a higher-value one, the coupon could be shortchanged and redeem for less than its real value.</li></ul>
