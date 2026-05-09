---
title: "Pharmacies hotfixes - 28.0.3 Pharmacies, Release date May 5, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.3"
subproduct: Pharmacies
minor_version: "28.0"
date: 2026-05-05 00:00:00+00:00
order: 38
guid: 6b9ff4a137d103a40690f1da76261693d69de70d
---

<strong>80575 Incorrect Sales Price action on the Pharmacy Item List page</strong>
<ul><li>The Sales Price action now correctly opens the Sales Price page when the old sales experience is active.</li></ul>
<strong>80950 Norwegian "E-prescription search" / "Customer search" window</strong>
<ul><li>Customer-ID on Customer Search Page and Customer First Name on E-Prescription Search Page are labels that now display correct Norwegian translations.</li></ul>
<strong>81377 UAT Commissioner: Missing action "Agent shipment" in retail sales order</strong>
<ul><li>Action Agent Shipment is available in page Retail Sales Order.</li></ul>
<strong>81422 UAT. Split Line generates invalid POLs and blocks prescription dispensing - B defect/High priority</strong>
<ul><li>Split Line action's behavior that prevented prescriptions from being confirmed was fixed.</li></ul>
<strong>81430 Unable to drilldown/open “Other party order payments” from prescription order line</strong>
<ul><li>Field <b>Other Party Payments</b> in <b>Order Totals</b> FactBox in a Prescription Order Line can be opened by clicking its value.</li></ul>
<strong>81485 Error selecting stubstitution in dispense order</strong>
<ul><li>Error in dose dispensing substitution filtered on ATC group was fixed.</li></ul>
<strong>81490 UAT: Commissioner: when an agent has another bill-to customer its not added to the retail sales order</strong>
<ul><li>Instance was fixed, where Customer was not retrieved from Customer card if missing in agent shipment processing.</li></ul>
<strong>81515 UAT. Workflow blocked when a Product Group Prescription has no product selected</strong>
<ul><li>There was an issue that would make it impossible to confirm lines when the same prescription order had a ProdGrup line with no item selected. This was fixed. </li></ul>
<strong>81585 FMD window (LSC PH MV Decommission (10037402, Card)) & related pages</strong>
<ul><li>Norwegian translation on FMD window, MV Decomission and related pages was fixed.</li></ul>
<strong>81630 UAT Commissioner: Agent sales order taken via POS is not marked with linked commissioner in retail sales order</strong>
<ul><li>Details not available.</li></ul>
<strong>81662 Scan Prescription fails when finding posted prescription order</strong>
<ul><li>Scan prescription button now functions properly when inputting a number of a posted prescription order.</li></ul>
