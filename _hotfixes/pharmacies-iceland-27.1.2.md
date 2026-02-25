---
title: "Pharmacies hotfixes - 27.1.2 Iceland, Release date February 17, 2026 - Hotfixes"
product: Pharmacies
version: "27.1.2"
subproduct: Iceland
minor_version: "27.1"
date: 2026-02-17 00:00:00+00:00
order: 23
guid: d16becc70f37342e8d3f1f507480ef8457f127c4
---

<strong>76822 Update the import of Lyfjaverdskra to show new fields and catagories</strong>
<ul><li>IS: Importing of Medicine Catalogue now uses field <b>HmerkingLyfjastofnunar</b> to determine if the drug is Hospital drug. Blank <b>Afgreidslumati</b> is replaced with <b>'R'</b> to reflect what the catalogue contains.</li><li>Before the import is processed for the first time, User should navigate to the import defaults, empty the table and re-generate the data or, If the data is different from the defaults, create new entries with <b>Afgreidslumati = 'R'</b> instead of existing entries where Afgreidslumati is blank.</li></ul>
<strong>77852 Pharmacy Customer Is not updated via action "Update from National Reg." on LSC PH Customer Card</strong>
<ul><li>IS: Pharmacy Customer Information is now updated in the action <b>Update from National Reg.</b> on Pharmacy customer card.</li></ul>
<strong>78071 IS Dispense subscriber missing in 27.1</strong>
<ul><li>Subscribed to new event in Pharmacy W1.</li></ul>
