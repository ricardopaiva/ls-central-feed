---
title: "Autotests hotfixes - 27.0.1 Autotests, Release date October 18, 2025 - Hotfixes"
product: Autotests
version: "27.0.1"
subproduct: Autotests
minor_version: "27.0"
date: 2025-10-18 00:00:00+00:00
order: 43
guid: 5ad892a4e2503a414b1adc06b1d30eb47f7aca73
---

<strong>73333 Issue with Retail Sales Order Currency Code for Customer Order with Sourcing Location</strong>
<ul><li>The logic was fixed, so the Sales Header currency code is now set based on the Customer Order’s Created Store currency instead of the Sourcing Store’s currency.</li></ul>
<strong>73085 Error with Customer Order/Sales Order rounding line - Hotfix</strong>
<ul><li>An issue in the Rounding Line logic was fixed. Creating a Sales Order from an Customer Order could incorrectly flip the sign of negative rounding amounts, causing the Sales Order total to increase instead of decrease.</li></ul>
