---
title: "Pharmacies hotfixes - 28.0.18 Pharmacies, Release date August 18, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.18"
subproduct: Pharmacies
minor_version: "28.0"
date: 2026-08-18 00:00:00+00:00
order: 108
guid: ae0cd1ebb8c1251d5c22cfc2dd14d249d1103adb
---

<strong>83923 FMD - "Medicines Verification Log" Alert ID field is missing</strong>
<ul><li>Changes in W1 Extension:<ul><li>New Alert ID field (Text[250]) on the Medicines Verification Log table, populated when the log entry is created from the pack verification response.</li><li>The Alert ID column is shown on the Medicines Verification Log page, next to NMVS ID and on Web Templates</li><li>The value is read from the raw data response returned for the single pack verification; if the response contains no alert identifier, the field is left blank.</li></ul></li></ul>
