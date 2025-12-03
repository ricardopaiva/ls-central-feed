---
title: "LS Central hotfixes - 27.0.14, Release date November 21, 2025 - Hotfixes"
product: LS Central
version: "27.0.14"
subproduct: 
minor_version: "27.0"
date: 2025-11-21 00:00:00+00:00
order: 4
guid: 0e79dac526037823ce99412279f12dbd5c4cd99c
---

<strong>74438 Deadlocks on Paying for Reservation, procedure calculate balance locking</strong>
<ul><li>Performance was improved in the Balance Calculation for reservations.  </li><li>Possible long running query was fixed in the POS receipt when printing the signature line (during charging to reservation).  Performance improvement in status changes and inserts charges to reservation.  </li><li>A possibility of deadlock was minimized when multiple POS's are paying reservations which are part of the same group reservation.</li><li>An issue was fixed, in the POS posting process, which could cause the process to update payment status on more reservations than was needed.</li></ul>
