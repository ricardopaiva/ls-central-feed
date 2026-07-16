---
title: "Hotels hotfixes - 28.0.19 Hotels, Release date June 30, 2026 - Hotfixes"
product: Hotels
version: "28.0.19"
subproduct: Hotels
minor_version: "28.0"
date: 2026-06-30 00:00:00+00:00
order: 56
guid: eb80a56721683fe7f246ba519ef24d3498082a86
---

<strong>83778 Move validation from page to table for customer field on hotel reservation table</strong>
<ul><li>When a reservation gets its customer assigned automatically — for example a booking coming in from an online channel or OTA — it now picks up that customer's default rate code and routing rule, just like when you select the customer by hand on the reservation.</li><li>The defaults apply only when the customer actually changes, so a routing rule you have adjusted yourself stays put if the same customer is set again.</li><li><b>Action required by partners</b>:<ul><li>None.</li></ul></li></ul>
<strong>82042 ReservationExtraSave API posts amount 0 when noOfPersons is 0 or omitted - default to 1 / derive from Adults</strong>
<ul><li>When a reservation extra was added through the <b>Hotel API's ReservationExtraSave endpoint</b>, the resulting revenue entry could be posted with an amount of 0 — for example when the request set perGuest = false with noOfPersons = 0, omitted noOfPersons, or sent a quantity of 0. The endpoint now resolves the number of persons the same way the <b>Additional Reservation</b> page does in Business Central, and validates the quantity, so extras are priced and posted correctly:<ul><li>When <b>perGuest = false</b>, the API now defaults No. of Persons to 1 if the client sends 0 or omits the field, so quantity, discount, and amount are calculated as expected.</li><li>When <b>perGuest = true</b>, No. of Persons is taken from the reservation's Adults count and any client-supplied value is ignored — matching the in-product behaviour.</li><li>A request with a <b>quantity of 0</b>, or with <b>no quantity at all</b>, is now rejected with an Invalid quantity error (errorCode: 31) instead of silently posting a zero-amount line — again matching the <b>Additional Reservation</b> page.</li></ul></li><li><b>Action required by partners</b>:<ul><li>If your integration adds extras with a quantity of 0, or without a quantity, update it to send a quantity of 1 or more — those requests now return an Invalid quantity error. Existing valid payloads continue to work unchanged, and previously-incorrect zero-amount results are now calculated correctly.</li></ul></li></ul>
<strong>80412 Consumed deposit that was assigned to a folio is "unconsumed" when collecting deposit after upgrade</strong>
<ul><li>Details not available.</li></ul>
<strong>80411 Unable to collect deposit for PAYMASTER after upgrade</strong>
<ul><li>Details not available.</li></ul>
<strong>79167 Test Upgraded Data Finance</strong>
<ul><li>Details not available.</li></ul>
