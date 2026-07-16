---
title: "Pharmacies hotfixes - 28.0.8 Pharmacies, Release date May 26, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.8"
subproduct: Pharmacies
minor_version: "28.0"
date: 2026-05-26 00:00:00+00:00
order: 103
guid: cda7d3dbb2c63cbbccfad3c09666b08fc8aa4d21
---

<strong>76879 Error Message field is not updated in Posting Queue</strong>
<ul><li>When posting a prescription order, error messages in the posting queue are updated with new errors once the old ones are solved.</li></ul>
<strong>80594 Missing HentPerson request when identifying a local customer using a name search</strong>
<ul><li>When searching Pharmacy Customer by Name HentPersonV2 request is processed for appropriate NIN and after user select needed customer and press Ok button on Customer Search Page.</li></ul>
<strong>81156 Incorrect refund amount on return when item price has changed – refund uses current price instead of original transaction price</strong>
<ul><li>Credit Prescription Order maintains all price information from the original order.</li></ul>
<strong>81435 Get Lines in Credit Orders deletes order when ePrescription is inactive</strong>
<ul><li>Credit orders are not deleted when using the Get Lines action and selecting an inactive prescription.</li></ul>
<strong>81584 Agent/Commissioner - Unable to change payment option on the retail sales order</strong>
<ul><li>Change Payment Option action in <b>Retail Sales Order</b> now does not give an error, even when no <b>Other Charge Line</b> is found.</li></ul>
<strong>81965 Norwegian "Delegate windows GUI"</strong>
<ul><li>The Norwegian translations for the Delegate Window were updated.</li></ul>
