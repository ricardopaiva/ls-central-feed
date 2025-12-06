---
title: "Hotels hotfixes - 27.0.4 Hotels, Release date November 11, 2025 - Hotfixes"
product: Hotels
version: "27.0.4"
subproduct: Hotels
minor_version: "27.0"
date: 2025-11-11 00:00:00+00:00
order: 29
guid: c2afbd6d7fb8df3a42e64931fc849b0ee10b92ba
---

<strong>74251 Deadlock on Room Type Block due to Availability Refresh</strong>
<ul><li>There was a deadlock issue, when deleting from Room Type Block table. This was fixed. </li></ul>
<strong>74190 Save values for the DRE and Reservation extras page</strong>
<ul><li>The Reservation Extras and Revenue Entries subpages, now save the last View Mode used, and apply it when the page is opened again. This is saved at the User level.</li></ul>
<strong>73941 Changing routing rule does not update folio no in DRE lines correctly</strong>
<ul><li>An issue was fixed, on changing routing rule in Invoice Management page. It was not routing correctly company lines, even if the folio was deleted.</li></ul>
<strong>73807 Refunding posting does not work if reservation is paid by another res.</strong>
<ul><li>The General Journal was deleted when starting Night Audit, that caused refund entries of Deposit to be lost. Now, refund for Deposit is posted directly after it is created.</li></ul>
<strong>73606 POS does not return to reservation after paying</strong>
<ul><li>Details not available.</li></ul>
<strong>73550 Void transaction deletes Deposit assignment line</strong>
<ul><li>There was an issue with  deposit assignment line was deleted on voiding transaction. Discrepancy between folio balance and Sales Journal was previously fixed recently. This was fixed. </li></ul>
<strong>73477 Refunding entries not posted in Night Audit</strong>
<ul><li>The General Journal was deleted when starting Night Audit causing refund entries of Deposit to be lost. Now, refund for Deposit is posted directly after it is created.</li></ul>
