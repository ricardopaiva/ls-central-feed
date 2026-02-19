---
title: "Pharmacies hotfixes - 27.0.10 Iceland, Release date February 17, 2026 - Hotfixes"
product: Pharmacies
version: "27.0.10"
subproduct: Iceland
minor_version: "27.0"
date: 2026-02-17 00:00:00+00:00
order: 87
guid: 0d6875f23e8e88a0e0cce919a6ac9f942fcaabf0
---

<strong>76822 Update the import of Lyfjaverdskra to show new fields and catagories</strong>
<ul><li>IS: Importing of Medicine Catalogue now uses field <b>HmerkingLyfjastofnunar</b> to determine if the drug is Hospital drug. Blank <b>Afgreidslumati</b> is replaced with <b>'R'</b> to reflect what the catalogue contains.</li><li>Before the import is processed for the first time, User should navigate to the import defaults, empty the table and re-generate the data or, If the data is different from the defaults, create new entries with <b>Afgreidslumati = 'R'</b> instead of existing entries where Afgreidslumati is blank.</li></ul>
<strong>78071 IS Dispense subscriber missing in 27.1</strong>
<ul><li>Subscribed to new event in Pharmacy W1.</li></ul>
