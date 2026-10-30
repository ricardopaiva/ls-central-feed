---
title: "Pharmacies hotfixes - 29.1.0 Norway, Release date October 27, 2026 - Hotfixes"
product: Pharmacies
version: "29.1.0"
subproduct: Norway
minor_version: "29.1"
date: 2026-10-27 00:00:00+00:00
order: 5
guid: b170f3873ccda22c81f1a7ca104b17aa8ea5483e
---

<strong>89771 APO-920 Preparation of antibiotics: PE not able to "Add water" documentation after confirm and barcode control</strong>
<ul><li>Add, change, or remove the water for a prescription line, and accept the water values, at any point until the line is approved.<ul><li>This now works after Confirm and after barcode control, from both the Prescription Panel and the Final Control panel.</li><li>Approval checks that the water values are accepted, whether you use Approve, To POS, or Pay Later.</li><li>Prescriptions without water, and water accepted before Confirm, no longer send an extra PDD quality check: the quality check sent at Confirm is the only one.</li><li>When water is accepted, changed, or removed after Confirm, one extra quality check is sent when the line is approved.</li><li>The Water value acceptance stage setting no longer has any effect.</li></ul></li></ul>
