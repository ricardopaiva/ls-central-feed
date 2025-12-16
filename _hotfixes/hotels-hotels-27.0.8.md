---
title: "Hotels hotfixes - 27.0.8 Hotels, Release date December 12, 2025 - Hotfixes"
product: Hotels
version: "27.0.8"
subproduct: Hotels
minor_version: "27.0"
date: 2025-12-12 00:00:00+00:00
order: 26
guid: d676c096fe28559bba407c9ebca1829e4db64e7b
---

<strong>75709 Error with booking connector(BEC) with Guest No set to 1</strong>
<ul><li>There was an issue with Booking Engine Connector related to create reservation process, it was returning an error with <b>Guest No.</b> field in Guest table. This was fixed. </li></ul>
<strong>75560 Folio Print Invoice button not printing associated POS receipt</strong>
<ul><li>There was an issue  on printing POS receipts from Folio Print Invoice button. It was not printing correctly. This was fixed. </li></ul>
<strong>74568 Not able to change property when creating a hotel booking</strong>
<ul><li>Several issues were resolved, related to changing the property on draft reservations, for both individual and group bookings. When the property is updated on a draft reservation, all associated information, such as reservation extras, guest lists, and comments, is now correctly updated with the new reservation number. Activities are the only exception; they must be recreated after the property change.</li><li>For group reservations, any existing draft reservations are deleted when changing property and users have used the action <b>create draft reservations</b>. This approach is more efficient since the price/availability table is able to generate updated draft reservations quicker, rather than requiring each one to be individually opened and adjusted (especially since changing the property clears the room type).</li></ul>
