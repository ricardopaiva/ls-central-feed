---
title: "Pharmacies hotfixes - 27.0.2 Norway, Release date January 27, 2026 - Hotfixes"
product: Pharmacies
version: "27.0.2"
subproduct: Norway
minor_version: "27.0"
date: 2026-01-27 00:00:00+00:00
order: 92
guid: 072a927fa8f730725f504a20aebbffce84867e40
---

<strong>76214 When "Scan prescription" is used to open an existing prescription order - previously handled prescription appears when PE try to change/choose item</strong>
<ul><li>There was an issue, where old prescription line data was kept in the user session. The logic now, resets the session when a new prescription starts, ensuring each prescription is created with fresh line data and does not reference previous orders.</li></ul>
<strong>76600 EIK validation error when trying to confirm prescription order</strong>
<ul><li>Unnecessary mapping of keys was removed from <b>reseptDokHandelsvare</b> from hentResept to Kvalitetsjekk v3 request.</li></ul>
<strong>76944 Customer Payments button not working in GUI</strong>
<ul><li>A Functionality was fixed:<ul><li>When pressing <b>Customer Payments button</b> on POS system shows <b>Get Customer Payments</b> page. When retrieving info with button Get Patient Payments by NIN system is mapping Customer Name and Surname.</li></ul></li><li>When pressing <b>Customer Payments button</b> on POS system shows <b>Get Customer Payments</b> page. When retrieving info with button Get Patient Payments by NIN system is mapping Customer Name and Surname.</li></ul>
<strong>77083 Field from response fails in QC - Extraneous key administreringForskrivning not permitted</strong>
<ul><li>The unnecessary key <b>administreringForskrivning</b> was removed from being mapped from Kvalitetssjekk Utleverings Melding V3 request.</li></ul>
