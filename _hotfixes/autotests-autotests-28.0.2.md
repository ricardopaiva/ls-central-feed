---
title: "Autotests hotfixes - 28.0.2  Autotests, Release date April 15, 2026 - Hotfixes"
product: Autotests
version: "28.0.2"
subproduct: Autotests
minor_version: "28.0"
date: 2026-04-15 00:00:00+00:00
order: 10
guid: 6162df626eb536404a909892ee9975cefa142a45
---

<strong>80633 Unable to create open statement (Document No length more than 10) version 27.1.21.3433</strong>
<ul><li>There was an issue introduced in v27.1.21 that would not allow the user to create an open statement under certain circumstances, when the Statement No. had more than 10 characters. This was fixed. </li></ul>
<strong>80374 Tanweer_31.03.2026 #642 Retail Message Panel Control CU</strong>
<ul><li>Displays an error text when an error occurs on the Retail Message Panel.</li></ul>
<strong>79075 Runtime error in Codeunit 99009601 due to type mismatch between Integer and Decimal fields.</strong>
<ul><li>FBP quantities should always be in whole number. If Quantity sold on POS is 2.4 then it is rounded to 2. 2.5 is rounded to 3. </li><li>FBP quantities should always be displayed as integers as for example Quantity. Quantity to Trigger, Remaining Quantity in FBP Ledger Entry.</li><li><b>Note</b>: <b>Notify Data Row Selected</b> in POS Data Grid Control Card - ##DEFAULT, #MEMBER_FBP_OVERVIEW in demodata must be turned OFF for the Frequent Buyer Program panel to work on POS. Instead turn <b>Notify Marked Count Changed</b> ON.</li></ul>
