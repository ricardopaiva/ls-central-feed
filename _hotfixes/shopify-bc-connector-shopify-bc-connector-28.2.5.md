---
title: "Shopify BC Connector hotfixes - 28.2.5 Shopify BC Connector, Release date October 13, 2026 - Hotfixes"
product: Shopify BC Connector
version: "28.2.5"
subproduct: Shopify BC Connector
minor_version: "28.2"
date: 2026-10-13 00:00:00+00:00
order: 33
guid: c68671c631e13b27d189a15717bf907d76b51d53
---

<strong>89900 BC Shopify connector: pre-auth capture returning PENDING is treated as failure at POS checkout</strong>
<ul><li>Details not available.</li></ul>
<strong>89569 Shopify Collection Creation & Assignment</strong>
<ul><li>Shopify collection sync no longer gets stuck when several collections are waiting to sync in the same run. Before this fix, only the first pending collection reused its existing Shopify collection — every other one tried to create a brand-new collection and failed whenever a matching collection already existed, permanently dropping those products out of sync. Newly created collections are also published to your Shopify sales channel right away, so they are visible to customers immediately instead of needing a manual publish in Shopify admin.</li><li>Action required by partners:<ul style="font-weight: bold;"><li><span style="font-weight: normal;">None — the fix applies automatically. If any Mapping Collection rows were manually remediated as a stopgap (Collection Id set by hand while this defect was open), they can be left as-is; they are not affected by this fix.</span></li></ul></li></ul>
