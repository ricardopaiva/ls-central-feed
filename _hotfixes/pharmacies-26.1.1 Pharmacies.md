---
title: "Pharmacies hotfixes - 26.1.1 Pharmacies, Release date July 15, 2025 - Hotfixes"
product: Pharmacies
version: "26.1.1 Pharmacies"
date: 2025-07-15 00:00:00+00:00
---

<strong>67397 LS Central for pharmacies: Make procedures global</strong>
<ul><li><li>Procedure <b>InsertDelegateEntry</b> is visible to extensions.</li></li></ul>
<strong>67398 Global access to functions in codeunit 10015311 "LSC PH Item Search Management"</strong>
<ul><li><li>Following functions were made visible to third party extensions:<ul><li>AutoFindSubstitutionItem</li><li>SetQtyFilter</li><li>CreateSubstitutionItem</li></ul></li></li>
<li><li>AutoFindSubstitutionItem</li></li>
<li><li>SetQtyFilter</li></li>
<li><li>CreateSubstitutionItem</li></li></ul>
<strong>67399 Expose functions and Clear Data Permission filters in "LSC PH Session"</strong>
<ul><li><li>Functions <b>InitializeProfile</b> and <b>Logout in PH Session</b> were exposed.</li></li></ul>
<strong>67400 Global access to functions in table 10015301 "LSC PH Item"</strong>
<ul><li><li>Functions in table <b>Pharmacy Item</b> were exposed:<ul><li>QtyInDispense</li><li>SetLocationFilterFromStore</li></ul></li></li>
<li><li>QtyInDispense</li></li>
<li><li>SetLocationFilterFromStore</li></li></ul>
<strong>67401 Global access to functions in codeunit 10015455 "LSC PH Omni Prescr. Service"</strong>
<ul><li><li>Functions were exposed in <b>CU 10015455</b>:<ul><li>CalcSelectedPrescriptions</li><li>GetActivePrescriptions</li></ul></li></li>
<li><li>CalcSelectedPrescriptions</li></li>
<li><li>GetActivePrescriptions</li></li></ul>
<strong>67402 Global access to function GetCurrText in table 10015370 "LSC PH Prescription"</strong>
<ul><li><li>Details not available.</li></li></ul>
<strong>67403 Global access to functions in codeunit 10015300 "LSC PH Utility"</strong>
<ul><li><li>Function <b>GetPrice</b> in Pharmacy Utility was exposed.</li></li></ul>
<strong>67405 Global access to functions in Omni PH-Document tables</strong>
<ul><li><li>Functions exposed:<ul><li>Procedure <b>CreatePHDocumentFromCO</b> in table 10015455 <b>LSC PH Omni PH-Document</b></li><li>Procedure <b>CreatePHDocumentLine</b> in  table 10015456 <b>LSC PH Omni PH-Document Line</b></li></ul></li></li>
<li><li>Procedure <b>CreatePHDocumentFromCO</b> in table 10015455 <b>LSC PH Omni PH-Document</b></li></li>
<li><li>Procedure <b>CreatePHDocumentLine</b> in  table 10015456 <b>LSC PH Omni PH-Document Line</b></li></li></ul>
<strong>67406 Global access to functions in codeunit 10037619 "LSC PH CO Utils"</strong>
<ul><li><li>Function <b>PharmacyCustomerOrderCreatePHDoc</b> was exposed.</li></li></ul>
