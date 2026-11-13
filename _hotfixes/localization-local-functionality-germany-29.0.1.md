---
title: "Localization hotfixes - 29.0.1 Local Functionality Germany, Release date November 10, 2026 - Hotfixes"
product: Localization
version: "29.0.1"
subproduct: Local Functionality Germany
minor_version: "29.0"
date: 2026-11-10 00:00:00+00:00
order: 13
guid: 6fdd47f5db0a1d584d7a3b5955c9e8ac021ac57c
---

<strong>89288 CPC export drops Income-account business case (TrinkgeldAG) from business_cases summary</strong>
<ul><li>[Internal use only] Cash Point Closings now report every business case in the DSFinV-K export summary.</li><li>Before, when an Income entry (such as a tip) and an Expense entry (such as a private withdrawal) used the same DSFinV-K export ID, the Income business case was missing from the summary. Its amount was still in the payment total. Statements with several sales transactions now report business cases for all of them too.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
