---
title: "Autotests hotfixes - 28.2.9 Release date September 15, 2026 - Hotfixes"
product: Autotests
version: "28.2.9"
subproduct: 
minor_version: "28.2"
date: 2026-09-15 00:00:00+00:00
order: 11
guid: 250463d49c4d741fc8adc326f7963ab3716fbc5c
---

<strong>88010  Coupon only applied to lowest cost item</strong>
<ul><li>For Coupons with Handling:Tender being used in a transaction with two or more items, it now consistently redeems for its full configured value.</li><li>Previously, if a lower-value item happened to be evaluated before a higher-value one, the coupon could be shortchanged and redeem for less than its real value.</li></ul>
