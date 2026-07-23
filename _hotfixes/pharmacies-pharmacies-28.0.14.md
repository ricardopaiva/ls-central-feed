---
title: "Pharmacies hotfixes - 28.0.14 Pharmacies, Release date July 21, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.14"
subproduct: Pharmacies
minor_version: "28.0"
date: 2026-07-21 00:00:00+00:00
order: 102
guid: 5d102cc93afedd8f8964eb4e8ac38239e41d121c
---

<strong>83889 Error when setting ATC filter = TRUE</strong>
<ul><li>Turning on the ATC filter in the Item Substitution Search page (opened via <b>Substitution</b> on a prescription line) could fail with an error stating that a record in the Pharmacy Substitution Item table already existed. The filter would appear enabled after dismissing the error, but the item list would not refresh correctly. This has been fixed — the ATC filter can now be toggled without error.</li></ul>
