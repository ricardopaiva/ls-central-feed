---
title: "Hotels hotfixes - 28.0.22 Hotels, Release date July 21, 2026 - Hotfixes"
product: Hotels
version: "28.0.22"
subproduct: Hotels
minor_version: "28.0"
date: 2026-07-21 00:00:00+00:00
order: 56
guid: 011433768042e219bd5e3ffc20afcb5f206b9e43
---

<strong>85119 Keep current rates sets the new rate to 0 on a BEC-created reservation (instead of keeping the existing rate)</strong>
<ul><li>Keep current rates now keeps the existing rate on reservations created through the Booking Engine. Before, turning it on zeroed the nightly rate on these reservations; now each night keeps its rate, just like reservations you create in the back office.</li><li>This version also fixes two related issues on the Rate Change and Upgrade pages, on rate codes that use a foreign currency:<ul><li>Keeps a single night's room type change when you turn on Keep current rates, instead of reverting it.</li><li>Shows the new rate in the rate code currency after a room type change, instead of converting it to the local currency.</li></ul></li></ul>
<strong>81300 On changing "Customer No." in Hotel Group Res does not update Customer Invoice Details correctly</strong>
<ul><li>Change or clear the customer on a hotel group reservation and its folios now keep the right payer automatically. Set a customer and the folios bill that customer; clear the customer and they bill the reservation's guest instead. Before, the invoice wouldn't post — it failed with a "customer does not allow multiple posting groups" error — and you had to run Reset Invoice Fields by hand first. This works whether you change the customer from the Group Reservation Card or from Invoice Management.</li></ul>
