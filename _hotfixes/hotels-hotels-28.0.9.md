---
title: "Hotels hotfixes - 28.0.9 Hotels, Release date May 20, 2026 - Hotfixes"
product: Hotels
version: "28.0.9"
subproduct: Hotels
minor_version: "28.0"
date: 2026-05-20 00:00:00+00:00
order: 61
guid: 0b1383a4e958291ad937087eb7f173db04bea6f1
---

<strong>82285 LS Hotel Upgrade Issue from v26.1 to v28 when Daily Room Rate was removed</strong>
<ul><li>There was an issue, with LS Hotel extension upgrade failure that aborted with <b>Daily Room Rate Price does not exist for ...</b> when migrating reservation folios. This was fixed. </li></ul>
<strong>81111 Unit price changes in price builder are overwritten after confirmation</strong>
<ul><li>Manual price and line discount changes on Price Builder lines in a new reservation are now preserved after adding a guest, changing the customer, or confirming the reservation. Previously these values could be replaced with the rate's default price.</li><li>This also resolves an error that would appear when editing the guest name after changing Price Builder lines.</li></ul>
