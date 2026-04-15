---
title: "Hotels hotfixes - 27.1.10 Hotels, Release date April 10, 2026 - Hotfixes"
product: Hotels
version: "27.1.10"
subproduct: Hotels
minor_version: "27.1"
date: 2026-04-10 00:00:00+00:00
order: 36
guid: 46a9ba0a41e8a5c8fe528b9dc4a68311d05b7c7c
---

<strong>80362 Hotel-Odd error message with auto allocate room</strong>
<ul><li>Checking in a reservation with no room assigned (and auto-allocate disabled) showed <b>Room is not ready for check-in, housekeeping status is 'Inspection</b>. Now shows <b>No room has been allocated. Please allocate a room before check-in.</b></li><li><b>Note:</b> In future versions (v28 onwards), instead of this error message, a room selection page automatically open for the user to choose a room.</li></ul>
<strong>79548 Unneccesary pop up when allocating room from reservation card</strong>
<ul><li>The unnecessary popup page was removed after allocating room from <b>Room No.</b> lookup in Reservation Card.</li></ul>
<strong>79545 When posting invoice in blank accounting the discount is not added to Sales Lines correctly</strong>
<ul><li>There was an issue where discounts applied to hotel reservations were not correctly reflected on invoice lines when using blank accounting. </li><li>Previously, the discount was visible on DRE lines but disappeared from the Sales Invoice, and closing a preview invoice would overwrite the original DRE values. </li><li>Now, discount information is properly carried over to invoice lines.</li></ul>
