---
title: "Shopify BC Connector hotfixes - 28.2.4 Shopify BC Connector, Release date October 7, 2026 - Hotfixes"
product: Shopify BC Connector
version: "28.2.4"
subproduct: Shopify BC Connector
minor_version: "28.2"
date: 2026-10-07 00:00:00+00:00
order: 30
guid: 469cfb6982b1a5227427a63943ac415eb978bfcb
---

<strong>88470 CO Payment Line - Pre Auth not handled on POS Checkout</strong>
<ul><li>There was an issue where a customer order paid with an e-commerce pre-authorization was treated as fully paid at POS checkout, even though the payment was never captured. The e-commerce integration now receives the capture request when you finish the sale, and the payment is recorded.</li><li>This fix applies when you use an e-commerce integration without LS Commerce Server, which means Send LS Commerce Messages is off in Customer Order Setup.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
