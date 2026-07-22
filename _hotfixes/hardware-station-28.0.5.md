---
title: "Hardware Station hotfixes - 28.0.5, Release date May 26 2026 - Hotfixes"
product: Hardware Station
version: "28.0.5"
subproduct: 
minor_version: "28.0"
date: 2026-07-22 02:23:09.173085+00:00
order: 50
guid: af92920438072f77cd3840f9770b286c688e1072
---

<strong>80494 Revert custom paper size behavior when width or height are zero</strong>
<ul><li>The original printer paper size selection behavior was restored, when custom paper width or height is not defined, while preserving custom paper sizing for valid dimensions.</li></ul>
<strong>81649 Simulator RFID device fails to load on HWST startup</strong>
<ul><li>There was an issue where creating an RFID device with the <b>Simulator</b> driver caused the device to fail loading on HWST startup. This was fixed. </li></ul>
<strong>82120 Duplicate Article Addition via QR Scan After RFID EPC Scan</strong>
<ul><li>Normalized EPC values in HWST to always return in uppercase, including EPCs generated through ConvertToEPC, ensuring consistent handling across RFID and manual conversion flows.</li></ul>
