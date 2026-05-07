---
title: "Localization hotfixes - 28.0.3 Local Functionality N-America, Release date May 5, 2026 - Hotfixes"
product: Localization
version: "28.0.3"
subproduct: Local Functionality N-America
minor_version: "28.0"
date: 2026-05-05 00:00:00+00:00
order: 25
guid: 73e79bb764107cd283e813aa0219288b23c0c163
---

<strong>81015 LSC NA - Penny Rounding Customer Order</strong>
<ul><li>There was an issue where penny rounding on Customer Order deposits was calculated incorrectly per payment line, causing pre-approved payment amounts to not match the order total.</li><li>This also caused order cancelation to incorrectly generate a spurious small negative deposit refund line on the POS.</li></ul>
<strong>80082 LSC NA - Issue with the incorrect tax amounts</strong>
<ul><li>There was an  issue in split-bill scenarios where selecting a payment tender (such as Visa) would incorrectly recalculate and display a different amount than the seat's original balance.</li><li>The transaction register now correctly reflects the original split amount for each seat.</li></ul>
