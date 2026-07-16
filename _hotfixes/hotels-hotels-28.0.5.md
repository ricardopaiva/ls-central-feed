---
title: "Hotels hotfixes - 28.0.5 Hotels, Release date May 12, 2026 - Hotfixes"
product: Hotels
version: "28.0.5"
subproduct: Hotels
minor_version: "28.0"
date: 2026-05-12 00:00:00+00:00
order: 70
guid: 6f62e24f0d97ebd62a45eb536f88fe9dc1023b38
---

<strong>81355 Unable to copy reservation in Group Reservations – error “Activity Group Member already exists”</strong>
<ul><li>Copying a reservation inside a group reservation no longer fails with an <b>Activity Group Member already exists</b> error. Guest-list entries on the copied reservation now receive a unique sequence number.</li></ul>
<strong>81264 Different results if customer is added on new reservation page or on the reservation page itself - folio info - group reservations</strong>
<ul><li>There was an issue about folio invoice fields not being updated after setting a <b>Customer No.</b> from Invoice Mgmt Page. This was fixed. </li></ul>
<strong>80359 Enum value translation has commas</strong>
<ul><li>Commas issue was fixed in some translation files.</li></ul>
<strong>79917 Error message after click on Pay button(POS) and wrong behaviour on clicking Total</strong>
<ul><li>Overrided voiding process for IncomeExpense lines on calculating Retail Charge in POS. Requires LSCentral hotfix.</li></ul>
<strong>79883 Unable to apply line discount when DRE lines have been marked as paid</strong>
<ul><li>There was an issue with the DRE line, that locked after being paid and did not allow the setting of a discount for Accrual Accounting or Checkout Accounting. </li><li>Now, the user should be able to change the discount, price or location code.</li></ul>
<strong>78958 HOTELS - Reservation invoice total at 0€</strong>
<ul><li>Added HotelResPrePayment_OnAfterSetupWEBDepositPOSTrans integration event.</li></ul>
