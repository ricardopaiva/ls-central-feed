---
title: "Autotests hotfixes - 27.1.6  Autotests, Release date March 6, 2026 - Hotfixes"
product: Autotests
version: "27.1.6"
subproduct: Autotests
minor_version: "27.1"
date: 2026-03-06 00:00:00+00:00
order: 21
guid: ddce4f89cfb0deb5c9473b97c5e967063af7b129
---

<strong>74871 When doing an item return through the Transaction list the POS cannot do the return if the scale is not on zero</strong>
<ul><li>When returning items the configuration on the Item card: <b>Qty not in Decimals</b> is used to determine if an item can be sold or returned in quantities with decimals and with a quantity below 1.</li><li>When returning a scale item the item is now automatically marked as <b>Manually weighted item</b>.</li></ul>
<strong>74648 If the Scale is not on zero, specific operations on POS should not be allowed</strong>
<ul><li>Details not available.</li></ul>
<strong>74622 When doing an item return the POS should not allow manual entering of weight if there is weight on the scale</strong>
<ul><li>Details not available.</li></ul>
<strong>74620 Tare value needs to be displayed on receipt as manual weight line</strong>
<ul><li>New events, <b>OnAfterPrintItemDetailTransLineSalesInfo</b>, <b>OnAfterPrintItemDetailLineSalesInfo</b> were added to make it possible to print Tare information to comply with scale certification requirements in the US. </li><li>Information about the Tare weight is now saved to a new field <b>Tare Weight</b> in both <b>LSC POS Trans. Line</b> and <b>LSC Trans. Sales Entry</b> tables.</li></ul>
<strong>74596 Repeat item sale should not work if the last item sold was a scale item</strong>
<ul><li>Details not available.</li></ul>
<strong>74559 Tare calculations: If tare value is higher than the returned weight the POS displays a negative quantity</strong>
<ul><li>If the Tare value on the item is higher than the returned weight from the scale, the POS now displays an error message.</li></ul>
