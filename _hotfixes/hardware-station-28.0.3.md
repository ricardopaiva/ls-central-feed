---
title: "Hardware Station hotfixes - 28.0.3, Release date  April 29, 2026 - Hotfixes"
product: Hardware Station
version: "28.0.3"
subproduct: 
minor_version: "28.0"
date: 2026-06-12 03:39:56.809327+00:00
order: 40
guid: 4cd511c3c2d52512be28416a218ec4064fdae7a0
---

<strong>80494 Revert custom paper size behavior when width or height are zero</strong>
<ul><li>The original printer paper size selection behavior was restored, when custom paper width or height is not defined, while preserving custom paper sizing for valid dimensions.</li></ul>
<strong>81649 Simulator RFID device fails to load on HWST startup</strong>
<ul><li>There was an issue where creating an RFID device with the <b>Simulator</b> driver caused the device to fail loading on HWST startup. This was fixed. </li></ul>
