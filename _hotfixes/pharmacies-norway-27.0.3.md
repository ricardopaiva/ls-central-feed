---
title: "Pharmacies hotfixes - 27.0.3 Norway, Release date February 3, 2026 - Hotfixes"
product: Pharmacies
version: "27.0.3"
subproduct: Norway
minor_version: "27.0"
date: 2026-02-03 00:00:00+00:00
order: 98
guid: a18afbc1053397591787ee4352a6859ad958b503
---

<strong>67638 Possible to start PSD from PDD for non-NIN patient, AND customer changes during registration</strong>
<ul><li>Functionality was fixed: When pressing Initiate PSD on PDD Details page for no NIN customers system throw an error that it is not possible for no NIN customers.</li></ul>
<strong>74888 "String length - customer payment" - Extend the DyreKategori (Animal Species) field to more than Code20</strong>
<ul><li>DyreKategori field was increased from twenty to forty characters.</li></ul>
<strong>75599 Water value - No warning when skipping water value</strong>
<ul><li><b>The logic was changed. Current behavior:</b><![CDATA[
]]><ul><li>
When the <b>Water Values Confirm on Approval</b> setting is enabled on the <b>Prescription Setup Profile</b> if a water value is entered but not accepted, an error is shown after confirming but before TO POS the PO line: <b>Water values are not confirmed. Open the Add Water Qty page to review and confirm before approving the prescription</b>.</li><li>Also by default (when <b>Water Values Confirm on Approval</b> is turned off), <b>BrukernavnTilsattMengdeVann</b> is always populated with the value from the <b>Water Accepted User</b> field.

The general behavior on the Prescr. Order Line Water Qty NO page was fixed when entering values.</li></ul></li><li>
When the <b>Water Values Confirm on Approval</b> setting is enabled on the <b>Prescription Setup Profile</b> if a water value is entered but not accepted, an error is shown after confirming but before TO POS the PO line: <b>Water values are not confirmed. Open the Add Water Qty page to review and confirm before approving the prescription</b>.</li><li>Also by default (when <b>Water Values Confirm on Approval</b> is turned off), <b>BrukernavnTilsattMengdeVann</b> is always populated with the value from the <b>Water Accepted User</b> field.

The general behavior on the Prescr. Order Line Water Qty NO page was fixed when entering values.</li></ul>
<strong>76712 BeregnV2 sends wrong reimbursement paragraph to Eik for Transitional Arrangement</strong>
<ul><li>The reimbursement paragraph mapping was fixed.</li></ul>
<strong>76784 Move acceptance of water value until after confirm, but before going to POS</strong>
<ul><li>Changes were implemented in - 75599 Water value - No warning when skipping water value.</li></ul>
<strong>77171 Error when Credit for Orders after 1 line has already been credited</strong>
<ul><li>Functionality was fixed:<ul><li>When doing credit for orders or credit for lines, the system shows a message if some line is already credited, and if empty prescription order is not created.</li></ul></li><li>When doing credit for orders or credit for lines, the system shows a message if some line is already credited, and if empty prescription order is not created.</li></ul>
