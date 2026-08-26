---
title: "Hotels hotfixes - 28.0.23 Hotels, Release date July 28, 2026 - Hotfixes"
product: Hotels
version: "28.0.23"
subproduct: Hotels
minor_version: "28.0"
date: 2026-07-28 00:00:00+00:00
order: 63
guid: 445b9489a15ad1aba8a2f22b8cac31e967398127
---

<strong>85121 Checking in multiple reservations errors out on Room assignment</strong>
<ul><li>You can now check in several reservations together when rooms are assigned manually. Before, selecting two or more arrivals on the Hotel Front Desk and checking them in failed with an error the moment the room picker opened for the second reservation, so staff had to check guests in one at a time. Now every reservation in the selection checks in, and you pick each room as usual.</li><li><b>Action required by partners</b>: None — the fix applies automatically once you update.</li></ul>
<strong>84178 Group reservation invoice posts wrong revenue lines and inflates sub-reservation balances (filter by Paying Res. No., not Group Res. No.)</strong>
<ul><li>When you post an invoice on a group reservation, it now includes only the charges routed to that group. Charges that belong to the individual reservations under the group stay on their own folios, so each reservation keeps its correct balance and can still be settled separately. Additionally, confirmation dialog for creating invoice has been updated to remark when user is creating an invoice to default hotel customer.</li><li><b>Action required by partners</b>: None.</li></ul>
<strong>83694 Hotel API - response consistency and detail improvements (PaymentsGetByNo naming, optional ReservationSave payment, activity/extra lineNo)</strong>
<ul><li>We've made the Hotel API easier and more predictable to work with. If you integrate with it, here's what changed and how to adapt:<ul><li>Consistent name for deposits and payments — the deposit/payment collection is now always returned under <b>payments</b>. Previously it came back as <b>payments</b> when a booking had no deposits but as <b>reservations</b> when it did. Update any code that read the <b>reservations</b> key in that response to use <b>payments</b> instead.</li><li>Payment is now optional when saving a booking — to save or update a booking without a payment, either leave out the <b>payment</b> field entirely or set it to <b>null</b>. Both are accepted, the booking saves normally, and no empty deposit is created. Send the <b>payment</b> object as before whenever a payment applies.</li><li>More detail when looking up a booking — the booking response now exposes the line numbers you need to manage activities and extras: <b>activityDetails</b> now includes a <b>lineNo</b> field; a new <b>reservationExtraDetails</b> array is returned at the booking level listing each reservation extra with its <b>lineNo</b>, item number, description, quantity, and unit price.</li></ul></li><li><b>Action required by partners</b>: Update any integration that reads the deposit/payment collection from PaymentsGetByNo under the <b>reservations</b> key — read <b>payments</b> instead. No other action required.</li></ul>
<strong>78829 Primary Guest created by webservice does not fill "Guest Type" field on "Member Contact" page</strong>
<ul><li>Book a hotel guest through a web service and, if they're not already in your member database, LS Central now fills in their Guest Type automatically. You no longer have to set it by hand before you can close the guest's Member Contact page.</li><li><b>Action required by partners</b>: None.</li></ul>
