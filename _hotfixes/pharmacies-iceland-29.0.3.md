---
title: "Pharmacies hotfixes - 29.0.3 Iceland, Release date November 24, 2026 - Hotfixes"
product: Pharmacies
version: "29.0.3"
subproduct: Iceland
minor_version: "29.0"
date: 2026-11-24 00:00:00+00:00
order: 39
guid: 76d8fe6bacbae8b3cec833df76e4f2ef9247d004
---

<strong>90353 Request: Supported way to run dispense production for a single card from AL (LS Central for pharmacies)</strong>
<ul><li>Get a clear error when Hekla e-prescription discrepancies stop dispense production that runs without a user present. Previously, a Hekla discrepancy opened a confirmation and a list of unprocessable dispense lines. A background session, such as a job queue entry or web service, cannot show either.</li><li><p>Now, when there is no user interface, production stops with an error that lists the affected lines: dispense order, prescription number, and Hekla status. When a user runs production, you are still asked whether to open the lines, as before.</p></li></ul>
<strong>91853 Issue within printing Insurance Label within "Next Step" in LSC PH Prescr. Order Prescr. (10015591, Card)</strong>
<ul><li>When printing all labels, the INS LABEL would print two copies of it, now it only prints one copy.</li></ul>
