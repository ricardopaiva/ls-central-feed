---
title: "Pharmacies hotfixes - 28.0.8 Norway, Release date June 9, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.8"
subproduct: Norway
minor_version: "28.0"
date: 2026-06-09 00:00:00+00:00
order: 81
guid: 94208c6c6a8605ff408e5217cc4df8d40f67de71
---

<strong>72022 NHN Power of Attorney</strong>
<ul><li>Details not available.</li></ul>
<strong>76985 Use Case - Start POA Process by Searching POA NIN</strong>
<ul><li>Created the possibility of searching POA Givers for a selected POA by NIN using the fullmakts eik integration.</li></ul>
<strong>77127 Use Case - POS - Start POA Process by Searching POA NIN</strong>
<ul><li>Details not available.</li></ul>
<strong>77330 Use Case - Search POA Havers based on the customer</strong>
<ul><li>Details not available.</li></ul>
<strong>77745 Use Case - Check POA used in PDD</strong>
<ul><li>It is now possible to see in PDD Details information retrieved from the PoA (fullmakts) web service.</li></ul>
<strong>77764 Use case - Show POA Limitations</strong>
<ul><li>Details not available.</li></ul>
<strong>77857 Send proof of PoA even when no document posted</strong>
<ul><li>Details not available.</li></ul>
<strong>77965 Use case - Hentdokumentasjon in customer start service</strong>
<ul><li>Details not available.</li></ul>
<strong>79886 Search based on Parental Responsibility for children under 16 years old</strong>
<ul><li>Details not available.</li></ul>
<strong>81323 Water value accepted = FALSE - Error from Kvalitetssjekk Response</strong>
<ul><li>The setup field <b>Water Values Confirm on Approval</b> was deprecated. A new field, <b>Water Value Acceptance Stage</b>, was added instead.</li><li>To perform the Water Value Acceptance Check when confirming a Prescription Order Line, use the <b>Confirm</b> mode.</li><li>To perform the Water Value Acceptance Check before sending to POS, use the <b>To POS</b> mode.</li><li>The EIK error has also been handled. The user  now sees the following message:<ul><li><b>Water values are not accepted. Open the Add Water Qty page to review and accept before confirming the prescription.</b></li><li>This message is similar to the one shown during the check before sending to POS.</li></ul></li></ul>
<strong>81593 Animal prescription (LSC PHNO Paper Prescription (10061657, Card))</strong>
<ul><li>Norwegian translations were updated in Animal Prescription Order.</li></ul>
<strong>82353 "Emergency prescription" LSC PHNO Paper Prescription (10061657, Card)</strong>
<ul><li>Missing/incorrect translations were added. </li></ul>
<strong>82512 Reimbursement §5-22p is not applied on preferred item</strong>
<ul><li>Populating automatically assigned Reimbursement Paragraph §5‑22p when the Pharmacy item is a contraceptive drug and the delivered item is also the preferred item.</li></ul>
<strong>82903 Encoding issue in Object identifiers</strong>
<ul><li>There was an encoding issue in Norwegian strings when creating Object Identifiers. This was fixed. </li></ul>
