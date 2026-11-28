---
title: "Hardware Station hotfixes - 29.0.7, Release date November 27, 2026 - Hotfixes"
product: Hardware Station
version: "29.0.7"
subproduct: 
minor_version: "29.0"
date: 2026-11-27 00:00:00+00:00
order: 20
guid: eb3f09e35d8b4f7ed3552d79ad90d8054df2d65f
---

<strong>88730 Split Hardware Station installer into separate .NET Framework and .NET 10 packages</strong>
<ul><li>Details not available.</li></ul>
<strong>90905 RFID and Comport issues</strong>
<ul><li>Details not available.</li></ul>
<strong>92666 RFID device lost after 26.x to 28.x upgrade, and RFID config overwritten by the POS</strong>
<ul><li>Fixed RFID readers disappearing after upgrading Hardware Station from 26.x to 28.x (existing losses are repaired at startup), stopped the POS from overwriting the RFID reader settings, and made IP-connected readers reconnect automatically after a lost connection without losing their tag cache.</li></ul>
