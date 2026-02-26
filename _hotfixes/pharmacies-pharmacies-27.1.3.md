---
title: "Pharmacies hotfixes - 27.1.3 Pharmacies, Release date February 17, 2026 - Hotfixes"
product: Pharmacies
version: "27.1.3"
subproduct: Pharmacies
minor_version: "27.1"
date: 2026-02-17 00:00:00+00:00
order: 24
guid: 42d17d69b571115bd15df587ed47315d68deea1f
---

<strong>69201 HON-20448 Lagreutleveringsmelding error due to invalid produkkontrollTidspunkt [0001-01-01T00:00:00]</strong>
<ul><li>The <b>Pick information</b> (PickedBy, PickedDate) is now set when the PE completes barcode and label scanning in the Barcode Control Panel. All picked POL lines  receive valid pick data, regardless of the pick method used (manual barcode scanning, auto-pick, or a combination of both).</li><li>When constructing the packing structure for Lagreutleveringsmelding, additional fallback logic was implemented:<ul><li>If a POL line is missing pick values, the system reuses valid pick information from another POL line within the same order, if available.</li></ul></li><li>If a POL line is missing pick values, the system reuses valid pick information from another POL line within the same order, if available.</li><li>This ensures that valid <b>ProduktkontrollTidspunkt</b> values are mapped during posting and prevents errors in the posting queue.</li></ul>
