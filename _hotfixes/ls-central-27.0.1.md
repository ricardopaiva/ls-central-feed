---
title: "LS Central hotfixes - 27.0.1, Release date October 18, 2025 - Hotfixes"
product: LS Central
version: "27.0.1"
subproduct: 
minor_version: "27.0"
date: 2025-10-18 00:00:00+00:00
order: 16
guid: 3b9308953cb31bf55d52e01b2dce8074cd8e8a08
---

<strong>73333 Issue with Retail Sales Order Currency Code for Customer Order with Sourcing Location</strong>
<ul><li>The logic was fixed, so the Sales Header currency code is now set based on the Customer Order’s Created Store currency instead of the Sourcing Store’s currency.</li></ul>
<strong>73222 Manually pick Service Items</strong>
<ul><li>Events added to <b>LSC CO POS Functions</b> and <b>LSC CO Picking Panel</b> codeunit.</li></ul>
<strong>73085 Error with Customer Order/Sales Order rounding line - Hotfix</strong>
<ul><li>An issue in the Rounding Line logic was fixed. Creating a Sales Order from an Customer Order could incorrectly flip the sign of negative rounding amounts, causing the Sales Order total to increase instead of decrease.</li></ul>
<strong>72762 Fix UpdateLock</strong>
<ul><li>Ref. to internal variable was changed, when getting last register number.</li></ul>
<strong>72513 OneListCalculate call using 'tender' coupon gives error</strong>
<ul><li>There was an issue where the POS Transaction was not found when the Store coupon Handling was Tender. This was fixed. </li></ul>
<strong>69530 LSC NA CA - Split the bill in 2, and the amount with taxes is not equally split</strong>
<ul><li>Details not available.</li></ul>
