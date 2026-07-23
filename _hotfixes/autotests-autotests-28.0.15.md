---
title: "Autotests hotfixes - 28.0.15 Autotests, Release date July 21, 2026 - Hotfixes"
product: Autotests
version: "28.0.15"
subproduct: Autotests
minor_version: "28.0"
date: 2026-07-21 00:00:00+00:00
order: 26
guid: a5ca898b70017e9b3fef366a1c7952066f59248b
---

<strong>84091 V28.1 Customer Order Create - Confirm Button Disabled</strong>
<ul><li>The <b>Customer Order Confirm</b> button in the POS is now configurable. You can assign one of two commands to it:<ul><li><b>CO_OK</b> - the Confirm button stays disabled until a sourcing option (ship, collect, or vendor) is selected for the order. This is the standard behavior introduced in v28 and remains unchanged.</li><li><b>CUSTOM</b> with parameter <b>CO_OK</b> - the Confirm button is always enabled, so staff can confirm the order without selecting a sourcing option first. This restores the order flow that existed before v28.</li></ul>Both commands confirm the order in exactly the same way; only the timing of when the button becomes available differs.</li><li><b>Action required by partners</b>: none for the standard setup. If you want the pre-v28 flow (Confirm always available), assign a Confirm button using the <b>CUSTOM</b> command with parameter <b>CO_OK</b> in your POS layout.</li></ul>
