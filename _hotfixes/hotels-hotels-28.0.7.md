---
title: "Hotels hotfixes - 28.0.7 Hotels, Release date May 15, 2026 - Hotfixes"
product: Hotels
version: "28.0.7"
subproduct: Hotels
minor_version: "28.0"
date: 2026-05-15 00:00:00+00:00
order: 30
guid: ccbd57ac8c929ef3c82f9781bd9b00543d1f46a7
---

<strong>82284 BEC REST: auto-create guests to match adult count instead of blocking reservation</strong>
<ul><li>When a Channel Management System (SynXis, SiteMinder, Channex, etc.) sends a hotel reservation through the <b>Booking Engine Connector</b> with <b>fewer guests in the payload than the Adults value on the reservation</b>, the reservation is now created successfully.<ul><li>Any missing guest entries are filled automatically using the <b>Default Member</b> configured on <b>Hotel Setup</b>, mirroring the behaviour of reservations created manually in Business Central. The error <b>Adult count does not match Guest count</b> no longer blocks these reservations.</li><li>The same behaviour applies to both <b>ReservationCreate</b> and <b>ReservationUpdate</b> messages.</li></ul></li><li>If the channel sends more guests than the Adults value, the Adults count is now bumped up to match the payload and the configured extra-adult charge is applied automatically (in interactive sessions the existing confirmation prompt is preserved; in non-interactive web service / OData calls the charge is applied silently).</li></ul>
