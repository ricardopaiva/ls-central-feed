---
title: "Hardware Station hotfixes - 28.0.4, Release date May 19, 2026 - Hotfixes"
product: Hardware Station
version: "28.0.4"
subproduct: 
minor_version: "28.0"
date: 2026-05-19 00:00:00+00:00
order: 53
guid: 3520146726fd281e3ae34b4ef014d1afda73d4ac
---

<strong>80494 Revert custom paper size behavior when width or height are zero</strong>
<ul><li>The original printer paper size selection behavior was restored, when custom paper width or height is not defined, while preserving custom paper sizing for valid dimensions.</li></ul>
<strong>81649 Simulator RFID device fails to load on HWST startup</strong>
<ul><li>There was an issue where creating an RFID device with the <b>Simulator</b> driver caused the device to fail loading on HWST startup. This was fixed. </li></ul>
