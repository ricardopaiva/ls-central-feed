---
title: "LS Central hotfixes - 28.2.9 Release date September 10, 2026 - Hotfixes"
product: LS Central
version: "28.2.9"
subproduct: 
minor_version: "28.2"
date: 2026-09-10 00:00:00+00:00
order: 4
guid: 5d302ff09e07d4362ce9e32b5248ba1020969602
---

<strong>87703  Issue when using a Coupon as a tender in a transaction</strong>
<ul><li>Coupons used as a payment tender, or scanned by their plain coupon code, now consistently redeem for the coupon's actual per-instance value instead of falling back to the coupon's default header value. This fixes payment lines and discount lines showing the wrong amount for coupons whose value is set per issued instance rather than as a single fixed amount on the coupon.</li></ul>
<strong>87428 LS Central Shopify Connector - Order Pull Filter, Sales Channels</strong>
<ul><li>The Sales Channel filter on Shopify Order Pull now works correctly. Enter the Sales Channel Code shown on the Shopify Mapping page (populated by Get Sales Channels) to import orders from just that channel — for example, Online Store or POS.</li><li><b>Action required by partners:</b> <ul><li>If you already use the Sales Channels filter, re-run Get Sales Channels on the Shopify Mapping page, then re-enter the filter using the Sales Channel Code shown there. The filter no longer accepts a Shopify channel name typed directly, so any previous value needs to be re-entered this way.</li></ul></li></ul>
<strong>87392 Test Connection to Web KDS Service fails with HTTP 400 - SalesType required on KOT item</strong>
<ul><li>Test Connection to Web KDS Service failed with HTTP 400. This was fixed.</li></ul>
<strong>86169 Codeunit 10016666 "LSC CO Picking Panel" does not allow OPOS scanning, and using a replacement codeunit then does not work for manual entry of quantities!</strong>
<ul><li>OPOS scanning was added to the CO Picking Panel. The CO scanning function was also fixed so it correctly searches for items when a barcode is scanned.</li></ul>
