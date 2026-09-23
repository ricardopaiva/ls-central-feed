---
title: "Autotests hotfixes - 28.2.10 Autotests, Release date September 22, 2026 - Hotfixes"
product: Autotests
version: "28.2.10"
subproduct: Autotests
minor_version: "28.2"
date: 2026-09-22 00:00:00+00:00
order: 11
guid: 8a1580a8f4bfeb68f202494f3ebd0362fb75734d
---

<strong>87887 Azure SAS token renewal on POS fix</strong>
<ul><li>Fix renewal of azure SAS tokens on the POS.</li></ul>
<strong>87587 Kitchen Operation Profile Card Enhancement Request – Ability to Print All Routed Order Lines in a Single Docket</strong>
<ul><li><b>Print Order Items — new print operation</b>
<ul>
<li>For stations using line-level routing (#LINEOPERATIONS), operators previously had to print every routed item one at a time, generating a separate print action per line.</li>
<li>A new Print Order Items operation now prints all items from the same order that are routed to the station that triggered the operation, in one action — one ticket per item.</li>
</ul>
</li><li><b>Print Item — unchanged</b>
<ul>
<li>Continues to print only the single, selected item.</li>
</ul>
</li><li><b>Chit / Print Order — fixed</b>
<ul>
<li>Printing a Chit (order) now correctly prints only the items routed to the station that triggered the print, instead of the full order.</li>
</ul>
</li></ul>
<strong>87564 Problems opening "Store Inventory Journal" Page 10001294 after last hotfix</strong>
<ul><li>Extensions can once again find out which worksheet is open on the Store Inventory Journal page. A recent change to how LS Central stores that state accidentally blocked outside access, breaking extensions that adjust field visibility by worksheet type.</li><li><b>Action required by partners</b>:<ul><li>If your extension previously read the open worksheet's state from session storage on this page, call the new <b>GetStoreInventoryWorksheet(var StoreInventoryWorksheet: Record "LSC Store Inventory Worksheet")</b> procedure from your own <b>OnOpenPage</b> handling instead.</li><li>It returns the currently open worksheet, including its sequence number and worksheet type.</li></ul></li></ul>
<strong>87166 V28.3 POS PRICECH command does not show numpad as popup</strong>
<ul><li>There was an issue where a POS Command with a Parameter, combined with a Post Command that had no Post Parameter, reused the parameter from the main command. This was fixed. </li><li>Also fixed: when the scanned item triggered an automatic discount or offer, with a Post Command such as Change Price could act on the discount line instead of the item's own line and fail with a <b>Price can only be changed on sales line</b> error. It now filters out the discount line.</li></ul>
<strong>84051 Deal Modifier “Added Amount” Not Charging Per Selection</strong>
<ul><li>Selecting a deal modifier item more than once now charges the added amount for each selection. Previously, choosing the same item twice only added the amount once, undercharging the total.</li><li><b>Action required by partners</b>:<ul><li>None.</li></ul></li></ul>
