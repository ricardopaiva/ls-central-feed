---
title: "Pharmacies hotfixes - 28.0.7 Norway, Release date June 2, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.7"
subproduct: Norway
minor_version: "28.0"
date: 2026-06-02 00:00:00+00:00
order: 104
guid: 5e758268e9a8ef0b89b97e77a7b38b95b81079c2
---

<strong>78140 The pharmacy cannot access PDD details if the delegate has a long name</strong>
<ul><li>Functionality fixed:<ul><li>PDD details opens when the delegate's name exceeds 30 characters.</li></ul></li></ul>
<strong>80341 Approval of water value should trigger YubiKey login</strong>
<ul><li>New pharmacy command PH_NO_ACCEPT_WATER was added.<ul><li>Pharmacy admin tasks needs to be processed, to get this new command;<ul><li>When this new command has the flag <b>"Auth. on Missing Permission" := true</b>, the system is asking for pharmacist login if current user is technician.</li></ul></li></ul></li></ul>
<strong>80594 Missing HentPerson request when identifying a local customer using a name search</strong>
<ul><li>
<p>When searching Pharmacy Customer by Name, HentPersonV2, the request is processed for appropriate NIN and after the user selects the customer and presses Ok button on the <b>Customer Search Page</b>.</p>
</li></ul>
<strong>80711 H-prescription in transitional arrangement give DotNet error in Beregn when item type is 06</strong>
<ul><li>
<p>Checking if BeregnedeRefusjoner.RefusjonsRegel.RefHjemmel and BeregnedeRefusjoner.RefusjonsRegel.RefKode is not empty to prevent creating an impact when mapping reimbursement paragraph info.</p>
</li></ul>
<strong>81435 Get Lines in Credit Orders deletes order when ePrescription is inactive</strong>
<ul><li>Credit orders are not deleted when using the Get Lines action and selecting an inactive prescription.</li></ul>
<strong>81965 Norwegian "Delegate windows GUI"</strong>
<ul><li>The Norwegian translations for the Delegate Window were updated.</li></ul>
<strong>82115 UAT Norwegian: Prescription order window (LSC POS Main JS (99008879, CardPart)) & related windows PART 2</strong>
<ul><li>Translation of <b>Reimbursement Paragraph Text</b> was changed to <b>Issued Reimbursement Paragraph Text</b>.</li></ul>
<strong>82350 In PDD Details - Move buttons for "Initiate PSD" and "Linked PSD Details" from "Related" to main button menu</strong>
<ul><li>Changing the buttons <b>Initiate PSD</b> and <b>Linked PSD Details</b> from the <b>Related</b> section to the <b>New</b> section on the PDD Details Page.</li></ul>
<strong>82477 Decimal amount eprescription error</strong>
<ul><li>Prescriptions with decimal amounts showed as whole numbers. This was fixed. </li></ul>
