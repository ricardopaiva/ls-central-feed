---
title: "Pharmacies hotfixes - 28.0.1 Norway, Release date April 28, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.1"
subproduct: Norway
minor_version: "28.0"
date: 2026-04-28 00:00:00+00:00
order: 115
guid: d7b8cd42a90564c6beb0718fee822d32aad42020
---

<strong>78857 A blank credit prescription order is created in the background when attempting to credit a prescription order that is currently being dispensed.</strong>
<ul><li>
<p>A blank credit order is no longer created when attempting to credit a prescription order that is currently being dispensed.</p>
</li></ul>
<strong>79653 RESH-ID should not be mandatory</strong>
<ul><li>RESH-ID is not mandatory when the item has a 950 for reimbursement paragraph, and it is inside the transitional arrangement period.</li></ul>
<strong>79901 NMD-UAT | UAT. BO. Prescription Credit in BO Without Barcode Control</strong>
<ul><li>The ability to create a credit order from BO without requiring barcode scanning or pick/reserve steps, matching GUI behavior, was added.</li></ul>
<strong>79941 Dosage Label in veterinary prescriptions does not show "animal category"</strong>
<ul><li>The dose label for veterinary prescriptions should show the animal category (dog, cat, rabbit, etc.).</li></ul>
<strong>80069 Error found in 3.01.65 - SokRekvirentV2 – Prescriber search using name and gender results in a .NET error message</strong>
<ul><li>A bug was fixed, where the Pharmacy User would receive an error message when specifying the gender while searching for prescribers.</li></ul>
<strong>80182 LS Pharmacy - Send M23 Event Publisher for Helfo</strong>
<ul><li>Technical issue, no change for end user experience.</li><li><b>OnAfterSendNedlastM23</b> Event Publisher for Helfo.</li></ul>
<strong>80190 Sales Statistics error message "The Sales Report does not exist" in orders with more than one order line.</strong>
<ul><li>There was an issue when sending Sales Statistics manually for prescriptions with many lines: it sent all prescription lines instead of sending only the current line. This was fixed. </li></ul>
<strong>80227 Technical issue</strong>
<ul><li>Registration was removed of the external command <b>GetEPrescriptionsByReferenceNumberCommand</b> since nowadays it is used as a parameter.</li></ul>
<strong>80426 NMD-UAT| HON-22505 PE not able to open settlement claims</strong>
<ul><li>Settlement claims can now be opened and reviewed as expected.</li></ul>
<strong>80427 NMD-UAT|HON-22507 UAT. Not possible to View PDD List linked to Customer payment report</strong>
<ul><li>It should be possible to open PDD Lines linked to the customer payment report by clicking on the NO. of PDDs.</li></ul>
<strong>80523 Rename Norway, Iceland Demo Data App</strong>
<ul><li>Norway and Iceland Demo Data apps were renamed.</li></ul>
<strong>80660 NMD-UAT | HON-22509 | Beregn Request Missing 'Reseptutleveringsliste' for Emergency prescription</strong>
<ul><li>It should be possible to create emergency prescription with reimbursement and Beregn Request must contain information on ‘reseptutleveringsliste’.</li></ul>
<strong>80755 Dose Labels are incorrectly printed out when removing one/more package</strong>
<ul><li>After decreasing the qty of the same item, only labels are printed with updated qty.</li></ul>
<strong>80797 Schengen certificate with duplicate strength text</strong>
<ul><li>Schengen certificate with duplicate strength text. This was fixed. </li></ul>
<strong>81064 DLL error related to telecom when sending QC V3 Request</strong>
<ul><li>Details not available.</li></ul>
