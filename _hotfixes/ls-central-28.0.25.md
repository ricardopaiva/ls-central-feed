---
title: "LS Central hotfixes - 28.0.25, Release date July 21, 2026 - Hotfixes"
product: LS Central
version: "28.0.25"
subproduct: 
minor_version: "28.0"
date: 2026-07-21 00:00:00+00:00
order: 1
guid: 7cb9745d23e32aae20f16a0f63c10f4054961bc3
---

<strong>84091 V28.1 Customer Order Create - Confirm Button Disabled</strong>
<ul><li>The <b>Customer Order Confirm</b> button in the POS is now configurable. You can assign one of two commands to it:<ul><li><b>CO_OK</b> - the Confirm button stays disabled until a sourcing option (ship, collect, or vendor) is selected for the order. This is the standard behavior introduced in v28 and remains unchanged.</li><li><b>CUSTOM</b> with parameter <b>CO_OK</b> - the Confirm button is always enabled, so staff can confirm the order without selecting a sourcing option first. This restores the order flow that existed before v28.</li></ul>Both commands confirm the order in exactly the same way; only the timing of when the button becomes available differs.</li><li><b>Action required by partners</b>: none for the standard setup. If you want the pre-v28 flow (Confirm always available), assign a Confirm button using the <b>CUSTOM</b> command with parameter <b>CO_OK</b> in your POS layout.</li></ul>
<strong>83738 Selling Item for UOM with qty per different from base causes discount calculation issue</strong>
<ul><li>Fixed an issue where the discount on a customer order sold in a unit of measure with a quantity-per-unit different from the base unit was scaled incorrectly when the order was collected at the POS. The discount amount was divided by the base-unit quantity instead of the selling-unit quantity, so a 20% discount could show as little as 1.86% after collection. The discount now scales correctly for any selling unit of measure.</li></ul>
