---
title: "Shopify BC Connector hotfixes - 28.2.6 Shopify BC Connector, Release date October 27, 2026 - Hotfixes"
product: Shopify BC Connector
version: "28.2.6"
subproduct: Shopify BC Connector
minor_version: "28.2"
date: 2026-10-27 00:00:00+00:00
order: 32
guid: ef575cf3a7c83d463c6b34e9114746bf1ad99a6c
---

<strong>89222 AL - Shopify order lines get wrong Unit of Measure for LS Central items with 2+ variant dimensions (Microsoft Shopify Connector defect)</strong>
<ul><li>Shopify order lines for items with two or more variant dimensions, like colour and size, no longer pick up the wrong unit of measure. Orders now correctly use the item's sales unit of measure instead of a size or colour value.</li><li><b>Action required by partners:</b>
<ul>
<li>None. The fix applies automatically after upgrading. Shopify order lines already imported with the wrong unit of measure still need a manual correction on the Shopify Order subform before they are processed into a customer or sales order.</li>
</ul>
</li></ul>
