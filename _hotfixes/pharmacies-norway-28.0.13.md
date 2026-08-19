---
title: "Pharmacies hotfixes - 28.0.13 Norway, Release date August 13, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.13"
subproduct: Norway
minor_version: "28.0"
date: 2026-08-13 00:00:00+00:00
order: 112
guid: 242f7edb40112d76aa96a83454e48f4062531f3c
---

<strong>76787 Changes in Norway Extension: Warning when an undelivered dispatch request is downloaded directly</strong>
<ul><li>When a prescription is downloaded (hentResept) that is a dispatch request (ekspederingsanmodning) and has not yet been dispensed, the user now receives the warning: <b>The prescription must be handled as a dispatch request; keep track of "Ekspederingsanmodning", which is updated regularly.</b></li><li>The prescription is automatically cancelled in Reseptformidleren (kansellerResept) so it can instead be handled through the Ekspederingsanmodning worklist.</li></ul>
<strong>82758 Release NO3.01.69 - 12.08.26</strong>
<ul><li>Details not available.</li></ul>
<strong>82880 Fixed in Norway Extension:</strong>
<ul><li>There was an issue, where downloading a prescription that needs a decision paper (e.g. §3 and §6) incorrectly started the reimbursement calculation right away and showed an error message. This was fixed.</li><li>Since the decision paper is required first, the calculation is now correctly postponed.</li></ul>
<strong>85745 Refresh button in pharma not working</strong>
<ul><li>Pharmacy commands were updated to local procedures, ensuring they are not translated.</li></ul>
