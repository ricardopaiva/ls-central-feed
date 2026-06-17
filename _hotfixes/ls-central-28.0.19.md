---
title: "LS Central hotfixes - 28.0.19, Release date June 9, 2026 - Hotfixes"
product: LS Central
version: "28.0.19"
subproduct: 
minor_version: "28.0"
date: 2026-06-09 00:00:00+00:00
order: 1
guid: 261660f22e9a762f0c7119b4e78b49e7c0f27dd5
---

<strong>83257 AL: Missing payment lines on Order Import Shopify</strong>
<ul><li>There was an issue, when orders from Shopify with mix of fulfilled and unfulfilled where pulled, caused missing payment lines in Customer Orders.</li></ul>
<strong>82921 Bug Report: Inconsistent Quantity Signs on Sales Return Order Lines Created by Statement-Post</strong>
<ul><li>Details not available.</li></ul>
<strong>82627 EFT Dialog causes "client callback after write transaction started"</strong>
<ul><li>Card payments through the EFT dialog now run cleanly to the end.</li><li>Previously, finishing a card payment could trigger a runtime error on the POS and add unnecessary processing overhead.</li><li>Payments now complete reliably and a little faster.</li></ul>
<strong>82304 LSC - Statement Posting Error For Customer Account Returns</strong>
<ul><li>Details not available.</li></ul>
<strong>82235 Manufacturer coupons reference number only allows numbers</strong>
<ul><li>Prefix error on Coupons was fixed. Now multiple Prefixes can be used with the same Reference No. as an example.</li></ul>
