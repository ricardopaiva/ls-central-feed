---
title: "Pharmacies hotfixes - 28.0.14 Norway, Release date September 1, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.14"
subproduct: Norway
minor_version: "28.0"
date: 2026-09-01 00:00:00+00:00
order: 116
guid: 424f62169eae3a61f07fed667e50068b5d20ece4
---

<strong>81683 Norwegian "Prescription order" window: LSC PH Prescr. Order (10015351, Document)</strong>
<ul><li>Norwegian translations in Prescription Order and Prescription Order Line were updated. </li></ul>
<strong>82876 Norwegian "E-prescription list"</strong>
<ul><li>Missing/incorrect translations were added. </li></ul>
<strong>83798 ProdGruppe Enhancements</strong>
<ul><li>Product Group Selection has been reworked and converted to a worksheet so the user has a better way to add multiple items.<ul><li>A new check box to select the items was added.</li><li>The user is now able to add Spacebar and tab to select items and switch to quantity selection.</li><li>The selected items page part, now dynamically increases and decreases size depending on the number of items selected.</li></ul></li></ul>
<strong>84252 POA documentation is not stored after viewing customer payment report</strong>
<ul><li>There was an issue where viewing a customer payment report on behalf of a patient (as a delegate with a valid power of attorney) did not record or report the POA usage to EIK. </li><li>This is now captured with the correct date/time, whether the report is viewed or printed.</li></ul>
<strong>84274 Wrong translation in suggested dosetexts</strong>
<ul><li>Wrong translations in suggested dose texts were fixed</li></ul>
<strong>84283 Wrong translations in emergency prescription</strong>
<ul><li> Norwegian translations on the emergency prescription (paper prescription) form were corrected.</li></ul>
<strong>84299 BC27: Not able to approve requisitions due to missing batch ID and expiry date</strong>
<ul><li>This was fixed in the Norwegian Extension:<ul><li><b>Batch ID</b> and <b>Expiry Date</b> are now, marked as mandatory on the <b>Break Pack</b> page for B2B requisition orders.</li><li>The <b>Break Pack</b> page now opens during approval so users can enter the missing values, keeping the previously selected order line in context.</li><li><b>Warning</b> is now shown on closing the Break Pack page if Batch ID or Expiry Date is still missing for a B2B requisition order.</li><li><b>Prescription order</b> line is refreshed after acceptance so newly entered values are applied immediately.</li><li>Quantity validation for Reserved lines and B2B requisition orders to prevent errors that blocked the page from closing are now skipped.</li></ul></li></ul>
<strong>84323 Unable to retreive e-prescriptions linked to old NIN</strong>
<ul><li>Functionality was fixed:<ul><li>It is possible to retrieve e-prescription list both on new and old NIN.</li><li>POS tag, Old NIN is shown in the GUI and button for getting e-prescription for old NIN is active.</li></ul></li></ul>
<strong>85543 AL-NO 27.1 Issuer Details not showing some info</strong>
<ul><li><b>Issuer Detail page</b> shows correct information in the <b>Issuer Prescription Details</b> and <b>Prescriber Organization</b> FactBoxes when retrieved from the e-prescripiton order process.</li><li>No prescription data is available when being viewed from the Issuer list since there is no Prescription Order Line in focus.</li></ul>
<strong>86244 Parenteral responisbility is not shown at first try, need to run the request several times, before the information is mapped</strong>
<ul><li>There was an issue where parental responsibility information did not appear on the first search attempt and required multiple tries to display. This was fixed. </li></ul>
<strong>86252 Paragraphs 101 to 105 should not be listed - controlled by setup</strong>
<ul><li>A new Setup was added in Eik Setup.<ul><li>When active, the import of the Reimbursement paragraphs in that setup is prevented, both from farmalogg and HentKodeverk.</li></ul></li></ul>
<strong>86806 Revert Changes: Beregn error message pops up for paragraph 3 when downloading prescription</strong>
<ul><li>Details not available.</li></ul>
