---
title: "Shopify BC Connector hotfixes - 29.0.4 Shopify BC Connector, Release date November 12, 2026 - Hotfixes"
product: Shopify BC Connector
version: "29.0.4"
subproduct: Shopify BC Connector
minor_version: "29.0"
date: 2026-11-12 00:00:00+00:00
order: 42
guid: a1a90edebd875709c68146203bb5d21388cc3f3f
---

<strong>91575 LS BC Shopify Connector Auto send MetaData</strong>
<ul><li>Send LS MetaData metafields to Shopify as soon as Add Items creates a product. When Use MetaData Mapping is on for the shop, the new product gets its metafields right away, so you no longer need to run Sync Products or the LS MetaData action as a second step.</li><li>If the metafield push fails, the item is still created and the remaining items in the report carry on. The metafields come with the next Sync Products run or LS MetaData action.</li><li>Products imported from Shopify, and shops with Use MetaData Mapping off, work as before.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
