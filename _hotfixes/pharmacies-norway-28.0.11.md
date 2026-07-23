---
title: "Pharmacies hotfixes - 28.0.11 Norway, Release date July 21, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.11"
subproduct: Norway
minor_version: "28.0"
date: 2026-07-21 00:00:00+00:00
order: 101
guid: 7a3cbe5b61463db2249318172906d66f9392aa9b
---

<strong>84111 Boots-UAT | ASCBC-1385 | UAT - Veterinary diagnose code incorrect when copying presc.</strong>
<ul><li>Veterinary prescriptions created from a PDD (<b>PDD</b> &gt; <b>New</b> &gt; <b>Paper Prescription</b>) now correctly carry over the <b>Animal diagnose code</b> field from the original prescription. Previously, the code was copied in the wrong format, which could cause errors when the pharmacy tried to send delivery information to EIK.</li></ul>
<strong>84206 When a paper prescription or an emergency prescription is created from the PDD Details page in GUI, the order does not open automatically in the GUI</strong>
<ul><li>Previously, creating a paper or emergency prescription from the PDD Details page left the PDD Details and PDD List pages open, so the resulting order did not open automatically in the GUI until you closed those pages manually. PDD-related pages now close automatically when the prescription is created, so the order opens as expected.</li></ul>
<strong>84526 B2B - The Break-Pack Details feature cannot be opened</strong>
<ul><li>Fixed an issue where the <b>Break-Pack Details</b> dialog could not be opened from B2B orders.</li></ul>
