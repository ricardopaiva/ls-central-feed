---
title: "Hotels hotfixes - 28.0.11 Hotels, Release date May 26, 2026 - Hotfixes"
product: Hotels
version: "28.0.11"
subproduct: Hotels
minor_version: "28.0"
date: 2026-05-26 00:00:00+00:00
order: 67
guid: 74fceca63a42bd599ba7daa14928fab77a0b94c3
---

<strong>82675 Guest List cannot be closed when primary guest count is not 1 - page becomes non-editable</strong>
<ul><li>The Hotel Reservation Guest List can no longer be left without a primary guest:<ul><li>Reservations whose guest list has no primary guest are automatically repaired the next time the Guest List is opened.</li><li>This resolves the <b>Only one primary guest is allowed</b> error that previously trapped users inside the Guest List page.</li></ul></li></ul>
<strong>80199 POS prepayment balance ignores invoice type and uses full reservation balance</strong>
<ul><li>Issues were fixed on paying prepayment from POS after selecting payer. It was ignoring the Invoice Type balance.</li></ul>
