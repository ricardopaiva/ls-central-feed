---
title: "Hotels hotfixes - 26.1.13 Hotels, Release date September 16, 2025 - Hotfixes"
product: Hotels
version: "26.1.13 Hotels"
date: 2025-09-16 00:00:00+00:00
---

<strong>71333 Amount displayed on multiple Hotel Refunds</strong>
<ul><li><li>Fixed amount displayed on multiple Hotel Refunds from POS.</li></li></ul>
<strong>70918 Incorrect Reservation Payment Entry for Group Booking</strong>
<ul><li><li>Fixed the incorrect amount in the payment entry for Group Booking.</li></li></ul>
<strong>70351 New receipt numbers created</strong>
<ul><li><li>Fixed issues where there are more than one POS Transaction per store/POS terminal. With this fix there can only be one POS Transaction per store/POS terminal number.  If the user does not post (or void) the POS Transaction, it may be voided if a new command or hotel reservation is used, and a new one created.</li></li></ul>
<strong>68272 Deposit schedule is not updated correctly</strong>
<ul><li><li>Deposit scheduler did not recalculate deposit due, after doing refund. This was fixed.</li></li></ul>
<strong>68229 Able to consume same deposit twice if I do not run Night Audit job</strong>
<ul><li><li>Night Audit is Run for the reservation, when it is checked out to consume all paid deposit.  The POS draws the deposit into the journal and marks it as <b>used</b>, to prevent using it twice. It also fixes updating DRE lines on deposit posting correctly.</li></li></ul>
