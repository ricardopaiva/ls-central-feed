---
title: "Shopify BC Connector hotfixes - 28.2.3 Shopify BC Connector, Release date September 1, 2026 - Hotfixes"
product: Shopify BC Connector
version: "28.2.3"
subproduct: Shopify BC Connector
minor_version: "28.2"
date: 2026-09-01 00:00:00+00:00
order: 12
guid: cc19a283921bf550b0fbc46f0ff0befec3e0f8d9
---

<strong>87056 Create Customer Orders fails with a string length error when the Shopify payment gateway name is longer than 10 characters. No Customer Order is created</strong>
<ul><li>Creating a customer order from a Shopify order no longer fails when the payment gateway name, credit card company, or a shipping address field is longer than the field it maps to in LS Central.</li><li>Previously, a gateway such as <b>Nets Easy Checkout</b> caused the whole batch conversion to abort with a string-length error and no customer order was created; these values are now truncated to fit instead. </li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>86949 Shopify: removal of collections and items in collections</strong>
<ul><li>Your Shopify collection sync now correctly batches item removals and confirms each batch succeeds before marking it as complete.</li><li>When more than 200 item memberships are removed in one sync pass, they are sent in multiple requests instead of one oversized request that Shopify rejects. If a removal batch fails, it is automatically retried on the next sync — no more stuck items.</li><li><b>Action required by partners:</b>
<ul>
<li>None. The collection sync now operates transparently with existing configurations.</li>
</ul>
</li></ul>
<strong>86945 Shopify Connector - Multiple Payment Lines in CO</strong>
<ul><li>Customer orders created through the Shopify connector no longer pick up duplicate payment lines when Shopify sends both a pending and a successful transaction for the same payment.</li><li>LS Central now only counts the successful transaction, so the order’s payment balance stays accurate.</li><li><b>Action required by partners:</b>
<ul>
<li>None — the fix applies automatically after upgrading.</li>
</ul>
</li></ul>
<strong>86796 Shopify Connector - Extend LS Retail Inventory Calculation from a single shop-store sourced figure to a per-location sourced figure</strong>
<ul><li>Enable different stock figures for each Shopify location on the same shop. When you set a location filter on a Shopify shop location, the stock sync now calculates inventory from that specific store's location instead of using the shop's default store.</li><li>This lets you set up local pickup or fulfillment scenarios where different Shopify locations show different on-hand quantities.</li><li><b>Action required by partners:</b>
<ul>
<li>Before upgrading, review any Shopify shop that uses the LSC Retail Calculation method and has a non-blank location filter set on one or more of its Shopify locations. After the upgrade, those locations will report stock from their filtered location instead of the shop's default location — the number may change.</li>
<li>Shops without location filters configured will use default store from the Store card.</li>
</ul>
</li></ul>
