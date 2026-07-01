---
title: "Autotests hotfixes - 28.0.13 Autotests, Release date June 30, 2026 - Hotfixes"
product: Autotests
version: "28.0.13"
subproduct: Autotests
minor_version: "28.0"
date: 2026-06-30 00:00:00+00:00
order: 23
guid: 27ff7e7bb36d496a382b0c821f1ad042a739b99a
---

<strong>84168 Pipeline Release/hotfixCandidate build failing tests</strong>
<ul><li>The reason for the failure, was not found. However, by slightly adjusting the order in which the license manager perform his checks, the issue was fixed. </li></ul>
<strong>82935 Customer Order - Bank Transfer incorrect message</strong>
<ul><li>Customer Order - Bank Transfer incorrect message.<ul><li>There was an incorrect message when picking Customer Order on POS that had tender type Bank Transfer and was already applied. This was fixed. </li></ul></li></ul>
<strong>82881 Add telemetry to the Authenticat request on License Manager</strong>
<ul><li>License Manager API authentication calls are now traced in Application Insights to support diagnostics and usage analysis.</li></ul>
<strong>81834 Current Availability - Bug with changing quantity</strong>
<ul><li>There was an issue where changing the quantity of a transaction line did not correctly update current availability. This was fixed. </li><li>There was an issue, where ordering a deal in the Self-Service Kiosk left deal lines incorrectly inserted when an ingredient was out of stock. This was fixed. </li></ul>
<strong>79035 SSK - voided deal increases availability</strong>
<ul><li>Void order without increasing availability.</li></ul>
