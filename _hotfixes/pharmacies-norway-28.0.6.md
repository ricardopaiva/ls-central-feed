---
title: "Pharmacies hotfixes - 28.0.6 Norway, Release date May 21, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.6"
subproduct: Norway
minor_version: "28.0"
date: 2026-05-21 00:00:00+00:00
order: 80
guid: d9630e7380690d30034514324897b53a224f5b16
---

<strong>79663 Quantity is not correctly shown on PDD Details for Prod. Group lines</strong>
<ul><li>Qty Per Unit and Total Qty are correctly shown on PDD Details Page for those prescriptions where not a whole part of the package was applied.</li></ul>
<strong>79996 Mandatory documentation of water batch</strong>
<ul><li>Water batch changed to non mandatory.</li><li>Message was fixed for scenario when one of mandatory fields is empty.</li></ul>
<strong>80580 Approval of break pack data is too early in the process</strong>
<ul><li>New pharmacy command NO_ACCEPT_BREAK_PACK was added<ul><li>Pharmacy admin tasks need to be processed to get this new command.</li><li>When the command has a flag, <b>"Auth. on Missing Permission" := true</b> then the system is asking for pharmacist login if current user is technician.</li><li>When a pharmacist break pack acceptance is turned on, the system is checking if break pack accepted<ul><li><b>OnBeforeApprove</b></li></ul></li><li>If break pack is not Accepted, then the user cannot approve prescription order line.</li><li>When pharmacist break pack acceptance is turned on, then the system is checking if break pack accepted<ul><li><b>OnBeforePreApprove</b> if break pack is not Accepted. The user cannot pre-approve prescription order line.</li></ul></li></ul></li></ul>
<strong>81273 DotNet error when taking Credit order from Final control to POS</strong>
<ul><li>Posting process of Credit Order was fixed. The request was skipped for not <b>Order</b> Type.</li></ul>
<strong>81456 Change the mapping/logic regarding parenteral responsibility</strong>
<ul><li><b>Mapping</b>:<ul><li>Fixed Father/Mother IDs were replaced with a list of all valid <b>Parent External IDs</b>.</li></ul></li><li><b>Data Source</b>: Parent External IDs are now mapped from the responsible persons within the parentalResponsibility object.</li><li><b>Translations &amp; Localization:</b>
<ul>
<li><b>Parent External ID</b>: Updated to Fødselsnummer foreldreansvar.</li>
<li><b>Field 3</b>: Updated to Foreldreansvar.</li>
</ul>
</li><li>In attachments you can find updated WebTemplates for Customer Info Panel on POS.</li></ul>
<strong>81537 UAT. PO initially loads but fails on first action after user switch</strong>
<ul><li>Switching user mid prescription flow no longer clears the prescription order that was already on screen.</li></ul>
<strong>81739 Clicking ,,Yes" on error messages box is not working correctly</strong>
<ul><li>Exemption Type was cleared to avoid multiple Beregn requests.</li></ul>
<strong>81754 Bag label (customer name) is printed upside down</strong>
<ul><li>It is now possible to invert the vertical orientation of bag labels using the same configuration used for dose labels.</li><li>The caption was changed from <b>Invert Dose Label</b> to <b>Invert Dose/Bag Label</b> to match the new use case.</li></ul>
<strong>81869 PDD List LSC PHNO PDD Info (10061501)</strong>
<ul><li>Objects were translated based on the suggested list.</li></ul>
<strong>81990 Receipt printing H-Prescription insurance payment info</strong>
<ul><li>Insurance Payment Amount in receipts that had H-Prescriptions is now masked on printout.</li></ul>
<strong>82023 Receipt not printing the correct Subtotal when H-Prescriptions are involved</strong>
<ul><li>Subtotal LCY in receipts containing H-Prescriptions is now correctly printed.</li></ul>
<strong>82134 UAT BO. Last withdraw field cannot be edited after PO is confirmed</strong>
<ul><li>It is possible to change <b>Last Withdraw</b> when prescription has the status: New, reserved or approved.</li></ul>
