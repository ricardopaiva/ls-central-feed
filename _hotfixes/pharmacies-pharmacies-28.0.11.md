---
title: "Pharmacies hotfixes - 28.0.11 Pharmacies, Release date June 16, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.11"
subproduct: Pharmacies
minor_version: "28.0"
date: 2026-06-16 00:00:00+00:00
order: 85
guid: 11d3762731a39a6709bb7f54e32fad493c00325f
---

<strong>81616 Dose Labels are incorrectly printed out when removing one/more package (Part 2)</strong>
<ul><li>Added a missing VAR to the publisher in the <b>W1</b> repo and a corresponding missing VAR to the subscriber in the <b>NO</b> repo.</li><li>
<p>Additionally, it was identified that the configuration <b>Use Ctrl. Label Barcode</b> in the <b>Prescription Setup Profile table</b> must be set to <b>true</b> for the solution to work correctly.</p>
</li></ul>
<strong>82882 OnBeforeMapLogEntry - Publish Pharmacy Command value</strong>
<ul><li>Not needed for end customer. An event was added. </li></ul>
<strong>82980 Pilot VA Jar - Pre-Approve not working as expected when tecnichian is logged in</strong>
<ul><li>Technical Issue:<ul><li><b>Locked</b> property was added to the fields on Prescription Commands.Enum.al to prevent translation of the Pharmacy Commands.</li><li>Deleting from the translation file the Commands to prevent unwanted translations.</li></ul></li></ul>
<strong>83156 Pick Control Panel completely broken by using Norwegian Region settings</strong>
<ul><li>Pick control panel now functions properly when having Norwegian region settings.</li></ul>
