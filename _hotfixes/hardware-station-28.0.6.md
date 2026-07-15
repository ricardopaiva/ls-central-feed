---
title: "Hardware Station hotfixes - 28.0.6, Release date June 2 2026 - Hotfixes"
product: Hardware Station
version: "28.0.6"
subproduct: 
minor_version: "28.0"
date: 2026-07-15 02:07:40.273798+00:00
order: 48
guid: 372ce5eb438296ec8ee33f851838f226f6b499c1
---

<strong>80494 Revert custom paper size behavior when width or height are zero</strong>
<ul><li>The original printer paper size selection behavior was restored, when custom paper width or height is not defined, while preserving custom paper sizing for valid dimensions.</li></ul>
<strong>81649 Simulator RFID device fails to load on HWST startup</strong>
<ul><li>There was an issue where creating an RFID device with the <b>Simulator</b> driver caused the device to fail loading on HWST startup. This was fixed. </li></ul>
<strong>82120 Duplicate Article Addition via QR Scan After RFID EPC Scan</strong>
<ul><li>Normalized EPC values in HWST to always return in uppercase, including EPCs generated through ConvertToEPC, ensuring consistent handling across RFID and manual conversion flows.</li></ul>
<strong>82446 Unable to configure RFID with Nordic Sampo</strong>
<ul><li>An error was fixed, when loading Nordic ID Sampo RFID devices.</li></ul>
