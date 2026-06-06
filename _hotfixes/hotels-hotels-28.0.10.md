---
title: "Hotels hotfixes - 28.0.10 Hotels, Release date May 26, 2026 - Hotfixes"
product: Hotels
version: "28.0.10"
subproduct: Hotels
minor_version: "28.0"
date: 2026-05-26 00:00:00+00:00
order: 45
guid: 0031b475e62432987addcd08919a1d04570792af
---

<strong>82531 Hotel Reservation - Guest List fails with duplicate Activity Group Member error on single reservation inside a group reservation (LSTS-45329)</strong>
<ul><li>Opening the <b>Guest List</b> from a single hotel reservation that lives inside a <b>Group Reservation</b> no longer throws an <b>Activity Group Member already exists</b> error. The Guest List page now opens correctly in that scenario.<ul><li>Creating a Group Reservation from an individual reservation no longer leaves behind placeholder <b>Group Member</b> rows on the group's guest list — only real guests are shown.</li><li>Opening the Guest List on a reservation that has no Guest assigned now shows a clear message: <b>Assign a Guest to the reservation before opening the Guest List.</b>,  instead of failing or opening an empty page.</li></ul></li></ul>
