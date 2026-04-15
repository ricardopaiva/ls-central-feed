---
title: "Autotests hotfixes - 27.1.12  Autotests, Release date April 10, 2026 - Hotfixes"
product: Autotests
version: "27.1.12"
subproduct: Autotests
minor_version: "27.1"
date: 2026-04-10 00:00:00+00:00
order: 23
guid: c80611e6bcf3db0ade0f6d8cd10a256a625f5c3a
---

<strong>79756 Receipt number for Shipment Customer Orders (follow up from 77144)</strong>
<ul><li>Fix on receipt number generated when posting a CO from web as SO.  Related to 77144.  </li><li><b>Note:</b>  Terminal that handles Sales Orders (Sales Order Terminal No. in Customer Order Setup) should not be used as a regular POS Terminal as the numbers series may collide.</li></ul>
<strong>79553 Mobile Inventory - CheckLicenseStatus error</strong>
<ul><li>Adjustments were made to the <b>GetLicenseUnit webservice process</b> to help with deadlocks.</li></ul>
