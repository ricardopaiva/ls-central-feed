---
title: "LS Central hotfixes - 27.0.13, Release date November 21, 2025 - Hotfixes"
product: LS Central
version: "27.0.13"
subproduct: 
minor_version: "27.0"
date: 2025-11-21 00:00:00+00:00
order: 12
guid: 520d9c1dd1d435baa00b744097ed5ff64d3fdb55
---

<strong>74868 Orders cannot sync from Shopify</strong>
<ul><li>There was an <b>Order Exist</b> error during Shopify order import to LS Central. This was fixed. </li></ul>
<strong>74438 Deadlocks on Paying for Reservation, procedure calculate balance locking</strong>
<ul><li>Performance was improved in the Balance Calculation for reservations.  </li><li>Possible long running query was fixed in the POS receipt when printing the signature line (during charging to reservation).  Performance improvement in status changes and inserts charges to reservation.  </li><li>A possibility of deadlock was minimized when multiple POS's are paying reservations which are part of the same group reservation.</li><li>An issue was fixed, in the POS posting process, which could cause the process to update payment status on more reservations than was needed.</li></ul>
<strong>74425 Long running time when executing the Periodic Discount Offer on the Retail Item card</strong>
<ul><li>Periodic Discount Offer process performance was improved.</li></ul>
<strong>74312  SC-2964-Trans. date/Time is not coming in susp/Retrieved Transaction</strong>
<ul><li>There was an issue with <b>Trans. date/Time</b> when transaction was suspended or retrieved. This was fixed. </li></ul>
<strong>72761 Changes regarding new Loyalty points usage</strong>
<ul><li>Details not available.</li></ul>
<strong>67884 Line Discount % and Line Amount did not update once user changed Line Amount in Retail Sales Return Order lines.</strong>
<ul><li>Line Discount % updated, when changing line amount on Retail Sales Return Order page.</li></ul>
