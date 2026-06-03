---
title: "Hotels hotfixes - 28.0.14 Hotels, Release date June 2, 2026 - Hotfixes"
product: Hotels
version: "28.0.14"
subproduct: Hotels
minor_version: "28.0"
date: 2026-06-02 00:00:00+00:00
order: 35
guid: a6724caacdf7af68c64a464bc7a9864e663725d3
---

<strong>82917 IntegrationEvent in ModifyRate() in RateManagementCU for BEC - used by RMS system integration (Atomize)</strong>
<ul><li>Integration event <b>OnBeforeDerivedRateModify</b>, was added in codeunit LSCHT Rate Calculation, raised when a base rate code's derived rate codes are about to be updated via DailyRoomRateSave. </li><li>Subscribers (e.g. Booking Engine Connector) can set IsHandled := true to skip the standard recalculation.</li></ul>
