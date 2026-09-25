---
title: "LS Central hotfixes - 28.2.12, Release date September 22, 2026 - Hotfixes"
product: LS Central
version: "28.2.12"
subproduct: 
minor_version: "28.2"
date: 2026-09-22 00:00:00+00:00
order: 1
guid: 5cdfb5db537589f4e585e91646119f8e3362c269
---

<strong>88121 Integration Event for Codeunit LSC Replen. Calc. Child Jrnl.</strong>
<ul><li>An integration event OnAddItemsToReplenJournalOnBeforeSetTableView has been added to the codeunit <b>LSC Replen. Calc. Child Jrnl</b>.</li></ul>
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
<strong>87335 Variant No. assigned to the incorrect product during transaction, causing statement posting failure</strong>
<ul><li>When you scan an item that requires variant selection on the POS web client, the barcode scanner no longer stays active while the variant selection panel is open.</li><li>Previously, scanning a second item before choosing a variant on the panel could insert that second item into the transaction with the wrong variant code, leave the originally scanned item out of the transaction entirely, and later block end-of-day statement posting with an invalid Variant Code error.</li><li>A concurrent scan while a variant selection is pending is now rejected, matching existing native-client behavior.</li><li><b>Action required by partners:</b>
<ul>
<li>None.</li>
</ul>
</li></ul>
<strong>87166 V28.3 POS PRICECH command does not show numpad as popup</strong>
<ul><li>There was an issue where a POS Command with a Parameter, combined with a Post Command that had no Post Parameter, reused the parameter from the main command. This was fixed. </li><li>Also fixed: when the scanned item triggered an automatic discount or offer, with a Post Command such as Change Price could act on the discount line instead of the item's own line and fail with a <b>Price can only be changed on sales line</b> error. It now filters out the discount line.</li></ul>
<strong>84930 Always print out receipts is payment is cash</strong>
<ul><li>Details not available.</li></ul>
<strong>84051 Deal Modifier “Added Amount” Not Charging Per Selection</strong>
<ul><li>Selecting a deal modifier item more than once now charges the added amount for each selection. Previously, choosing the same item twice only added the amount once, undercharging the total.</li><li><b>Action required by partners</b>:<ul><li>None.</li></ul></li></ul>
