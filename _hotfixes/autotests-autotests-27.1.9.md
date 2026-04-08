---
title: "Autotests hotfixes - 27.1.9 Autotests, Release date March 27, 2026 - Hotfixes"
product: Autotests
version: "27.1.9"
subproduct: Autotests
minor_version: "27.1"
date: 2026-03-27 00:00:00+00:00
order: 22
guid: 98603ff43a79b5994fae9b42d8164fc6cbaa7c02
---

<strong>79328 Payment Lines Removed When Order Edit Fails</strong>
<ul><li>Payment lines were removed from Customer Orders when a Customer Order Edit failed to process due to errors (e.g., increasing quantity). This affected Customer Orders created from Shopify or Magento. LS Central now preserves existing payment lines if the update fails, preventing paid orders from appearing unpaid.</li></ul>
<strong>55093 Customer Orders - Bank Transfer</strong>
<ul><li>There was an incorrect refund line in Posted Customer Order when the Customer Order was paid with Bank Transfer tender type. This was fixed. </li></ul>
