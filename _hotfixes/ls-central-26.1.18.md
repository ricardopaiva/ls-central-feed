---
title: "LS Central hotfixes - 26.1.18, Release date August 20, 2025 - Hotfixes"
product: LS Central
version: "26.1.18"
date: 2025-08-20 00:00:00+00:00
---

<strong>70264 Booking POS Posting: Make the Cleanup function lock unfriendly</strong>
<ul><li><li>The Booking Posting POS cleanup () function made more lock efficient by checking if it is empty prior and also the search loop is not started in record locking mode.</li></li>
<li><li><b>Note:</b> This function should rarely write anything to the db.  It would be only in the cases where the POS created a reservation, but the user voided the lines. The reservation would not have any activities and the cleanup tries to delete the empty reservation.</li></li></ul>
<strong>70175 AL: Fix GetSelectedSalesDoc WS</strong>
<ul><li><li><b>GetSelectedSalesDoc</b>
<ul>
<li>Reward Points earned was fixed.</li>
<li>Transaction lookup was fixed, because of empty Transaction record.</li>
<li>Deal line was missing in HospOrder. This was fixed. </li>
<li>Change Payment Line number to actual number + 99 to be able to retrieve original line number.</li>
</ul>
</li></li>
<li><li>Reward Points earned was fixed.</li></li>
<li><li>Transaction lookup was fixed, because of empty Transaction record.</li></li>
<li><li>Deal line was missing in HospOrder. This was fixed. </li></li>
<li><li>Change Payment Line number to actual number + 99 to be able to retrieve original line number.</li></li>
<li><li><b>GetSalesInfoByOrderId</b>
<ul>
<li>Transaction lookup was fixed, because of empty Transaction record.</li>
</ul>
</li></li>
<li><li>Transaction lookup was fixed, because of empty Transaction record.</li></li></ul>
<strong>70154 Customer Order Edit - Refund Returns an Error - Copy</strong>
<ul><li><li>Fixed problem when multiple add and void lines on POS could result in error: <b>Customer Order cannot be Updated. Changes will be rolled back.</b></li></li></ul>
