---
title: "Hotels hotfixes - 26.1.11 Hotels, Release date September 2, 2025 - Hotfixes"
product: Hotels
version: "26.1.11 Hotels"
date: 2025-09-02 00:00:00+00:00
---

<strong>70437 Error Code: 85132273 when doing refund deposit after night audit has been run</strong>
<ul><li><li>Error handling for process deposit payment in BackOffice does now avoid showing error logs that are already handled that does not affect the process.</li></li></ul>
<strong>70148 When deposit is on another folio than "guest" it won't show in POS</strong>
<ul><li><li>Fixed an issue with not getting the deposit correctly inserted in POS journal when folio is another than default Guest on <b>Temp Balance</b> or <b>Blank</b> Accounting (None).</li></li></ul>
<strong>68267 Print preview invoice for folio on POS not working</strong>
<ul><li><li>Improvements to the printing behavior in the POS:<ul><li>If there are no Receipt No. or Sales Invoice for the folio - Print the Preview Sales Invoice.</li><li>If there are Receipt No. and Sales Invoice for the folio - The user is prompted if he wants to print the Receipt or Sales Invoice.</li></ul></li></li>
<li><li>If there are no Receipt No. or Sales Invoice for the folio - Print the Preview Sales Invoice.</li></li>
<li><li>If there are Receipt No. and Sales Invoice for the folio - The user is prompted if he wants to print the Receipt or Sales Invoice.</li></li></ul>
