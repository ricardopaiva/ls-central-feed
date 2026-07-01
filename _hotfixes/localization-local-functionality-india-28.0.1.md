---
title: "Localization hotfixes - 28.0.1 Local Functionality India, Release date June 23, 2026 - Hotfixes"
product: Localization
version: "28.0.1"
subproduct: Local Functionality India
minor_version: "28.0"
date: 2026-06-23 00:00:00+00:00
order: 84
guid: ce51b09f61f23abc95bb772d894a062d808c8fa9
---

<strong>82954 LSC IN - GST amount doubling issue in POS Billing</strong>
<ul><li>GST totals in POS billing are now correct when a transaction contains the same item sold multiple times and the lines are compressed.</li><li>Previously, each child line kept its own GST value even though the parent line already carried the aggregated tax for the group, inflating the total shown on the bill and in posted tax entries.</li></ul>
