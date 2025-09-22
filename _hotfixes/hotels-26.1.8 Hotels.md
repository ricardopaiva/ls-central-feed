---
title: "Hotels hotfixes - 26.1.8 Hotels, Release date August 22, 2025 - Hotfixes"
product: Hotels
version: "26.1.8 Hotels"
date: 2025-08-22 00:00:00+00:00
---

<strong>70121 Hotel POS Payment – Error Pop-up Resets Amount to $0.00</strong>
<ul><li><li>  The new value was ignored, after an invalid refund amount was entered. This was fixed. </li></li></ul>
<strong>70120 Member Card No not linked when POS transaction started from the reservation page in POS</strong>
<ul><li><li>Fixed an issue where Member Card No was not in refund POS Trans</li></li></ul>
<strong>69803 Hotel Group Reservation Status is not allowed to be changed once confirmed (confirm if standard functionality)</strong>
<ul><li><li>It is now possible to change between different Confirmed statuses on individual and group reservations. <b>Note:</b> It is only possible to do this in group reservations if the new Status also exists for individual reservations (Reservation Type = Room).</li></li></ul>
<strong>69338 Adding an activity on a hotel POS using BOOKPRODLIST does not add the activity to DRE</strong>
<ul><li><li>Not calling <b>UpdateActivityCust</b>(Rec) procedure where the <b>Activity Customer</b> is being updated, if it exist in hotel but not in activity.</li></li></ul>
<strong>67784 Allocating Room in Backoffice changes the Unit on DRE</strong>
<ul><li><li>There was an issue, allocating rooms in Backoffice changed the prices. This was fixed.</li></li></ul>
<strong>65684 Room gets housekeeping status Vacant-Clean even though room is still checked in</strong>
<ul><li><li>Housekeeping Status Vacant Clean and Vacant Cleaning Request are no longer allowed if Reservation is In House. Setting the status to <b>Clean</b> on an In House Reservation set the Housekeeping Status to Vacant Clean, instead of <b>Occupied Clean</b>. This was fixed.</li></li></ul>
