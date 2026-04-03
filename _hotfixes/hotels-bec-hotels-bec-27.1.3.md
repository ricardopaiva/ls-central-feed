---
title: "Hotels BEC hotfixes - 27.1.3 Hotels BEC, Release date March 17, 2026 - Hotfixes"
product: Hotels BEC
version: "27.1.3"
subproduct: Hotels BEC
minor_version: "27.1"
date: 2026-03-17 00:00:00+00:00
order: 41
guid: e6b6715ca87423bafa5e933691af1ac36519886d
---

<strong>79334 BEC integration events for Channex</strong>
<ul><li>New integration events for BEC were added, <b>MapHotelReservation_OnAfterSetCustomer(var HotelTempRes: Record "LSCHT Hotel Temp Reservation")</b>.</li></ul>
<strong>79346 BEC integration events for Channex 2</strong>
<ul><li>New integration events for BEC were added, <b>MapHotelReservation_OnAfterSetCustomer(BECConfig: Record "LSCHB Config"; JsonRequestObj: JsonObject; var HotelTempRes: Record "LSCHT Hotel Temp Reservation")</b>.</li></ul>
<strong>79369 BEC integration events for Channex 3</strong>
<ul><li>New integration events for BEC were added, <b>PullReservationsData_OnBeforePullReservationDataHttpWrapper(var BecConfig: Record "LSCHB Config"; var HttpWrapper: Codeunit "LSC Http Wrapper"; var Handled: Boolean)</b>.</li></ul>
