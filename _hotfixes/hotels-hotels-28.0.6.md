---
title: "Hotels hotfixes - 28.0.6 Hotels, Release date May 12, 2026 - Hotfixes"
product: Hotels
version: "28.0.6"
subproduct: Hotels
minor_version: "28.0"
date: 2026-05-12 00:00:00+00:00
order: 39
guid: 8ac80ce6c1bac98f73b9aca55ee5a60bde8cfee9
---

<strong>81263 Fire Report Refactor</strong>
<ul><li>The way that the Fire Report was refactored was exported when executing the scheduled job.<ul><li>Previous Fire Report Path fields were removed since it was no longer used.</li><li>New fields were added to be able to setup so the report is sent by email.</li><li>When running from the Hotel Manual Jobs page, the property filter is now applied.</li></ul></li></ul>
<strong>80400 Paying Reservation No. incorrectly updated when assigning activities by selection on confirmed Group Hotel Reservations</strong>
<ul><li>Issue on updating <b>Paying Reservation No.</b> field after assigning activites on confirmed Group Hotel Reservations was fixed.</li></ul>
<strong>79931 No. of persons in Activity Group Card is not filled out when creating a group reservation</strong>
<ul><li>There was an issue on updating <b>No. of persons</b> in Activity Group Card when creating Hotel Group Reservations. It was causing issues on adding new activities and another related actions. This was fixed. </li></ul>
<strong>79765 Issues with rate codes in different currencies</strong>
<ul><li>Precision loss when displaying rates in rate code currency on the reservation FactBox was fixed.</li><li><b>Rate Code Currency Unit Price</b> field was added on Detailed Revenue Entry to store the exact unit price in the rate code currency when this is different that LCY.</li><li>The Rate Change page now displays and operates entirely in the rate code currency.</li></ul>
