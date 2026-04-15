---
title: "Hotels hotfixes - 27.1.6 Hotels, Release date March 26, 2026 - Hotfixes"
product: Hotels
version: "27.1.6"
subproduct: Hotels
minor_version: "27.1"
date: 2026-03-26 00:00:00+00:00
order: 40
guid: 6b9b3720f547e4b34cd3b319e86d4f68fce31df7
---

<strong>79852 LS Hotel BEC - Wrong Rate update into Hotel Reservation - from OTA</strong>
<ul><li>There was an issue where hotel reservations received from OTA channels (e.g., Agoda via SiteMinder) were updated with incorrect rate values. The room rate adjustment logic was incorrectly modifying rates for OTA and web bookings, resulting in totals that did not match the original booking amounts. OTA and web reservation rates are now preserved as received.</li></ul>
<strong>79689 Error when changing Activity Status after upgrade to 27.1</strong>
<ul><li>There was an issue where confirming an Activity Group with Package activities would cause an error. This was fixed. </li></ul>
<strong>78977 Hotels changing rooms issue</strong>
<ul><li>The Rate Change page no longer opens when changing the Room No. on a <b>in house reservation</b> in the POS. The Rate Change page only opens if the Room Type changes.</li></ul>
