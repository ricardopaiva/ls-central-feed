---
title: "Hotels hotfixes - 28.0.18 Hotels, Release date June 23, 2026 - Hotfixes"
product: Hotels
version: "28.0.18"
subproduct: Hotels
minor_version: "28.0"
date: 2026-06-23 00:00:00+00:00
order: 55
guid: 383b4687c73d16ba6d9730b744ef61762b896e22
---

<strong>83668 Tape Chart enters a loop when moved to a date or room type without a configured Daily Room Rate</strong>
<ul><li>Resolved an issue where moving a reservation in the Tape Chart to a date or room type without a configured Daily Room Rate caused the application to enter a continuous processing loop.</li><li>The Tape Chart now handles this condition gracefully and notifies the user instead of becoming unresponsive.</li></ul>
