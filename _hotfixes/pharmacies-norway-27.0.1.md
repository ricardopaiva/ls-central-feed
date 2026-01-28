---
title: "Pharmacies hotfixes - 27.0.1 Norway, Release date January 21, 2026 - Hotfixes"
product: Pharmacies
version: "27.0.1"
subproduct: Norway
minor_version: "27.0"
date: 2026-01-21 00:00:00+00:00
order: 93
guid: a72d5f13b3aaa45b0ac4b8f4fc31a39862b41a26
---

<strong>66356 HON-20178 PE should not have to re-open and confirm again when the pharmacy has recivied the ordered item</strong>
<ul><li>When posting a transaction in POS, any errors related to LagrePDD, LagrePSD, or LagreJGD that occur during the posting process are no longer displayed to the user in POS. The errors can be later reviewed and resolved in the back office in the prescription posting queue.</li><li>This improvement ensures a smoother user experience at the point of sale and prevents unnecessary error messages from being shown to pharmacy employees.</li></ul>
<strong>67159 Prescribed Total Quantity wrong in dispensation</strong>
<ul><li>A prescription does not need to be re-opened after  a purchase order for that prescription is finished, and the line can be pre-approved  after the order is done, to reduce the number of steps for the process.</li></ul>
<strong>67319 HON-15968 PRD Intervention Block Alert on a Active Ingredients Prescription</strong>
<ul><li>A fix was implemented to ensure interventions are correctly generated for active ingredient prescriptions when performing generic substitutions. The system now properly checks the delivered item’s <b>Issued Exchange Group ID</b> and automatically creates an intervention when the item falls outside the original group. If the delivered item exchange group, matches the issued, no intervention is created, ensuring correct validation and preventing substitution-related errors.</li></ul>
<strong>67838 HON-20347 Active Ingredient: Chosen pharmacy item jumps to next prescription order Line</strong>
<ul><li>There is a prescription order with two lines, the first being a Brand/Active Prescription and the second being a Pharmacy Item. If in the second line the system  applies the Max Reimbursement Price to the line, when  the item in the first line is chosen, then this item is applied incorrectly to both lines. This was fixed.</li></ul>
<strong>67886 Pharmacy Item Instruction - Dosage - Dose Text - The Expanded Dose Text is wrong</strong>
<ul><li>
<p>Logic was added to handle a new rule on the expand dose text logic.</p>
</li></ul>
<strong>71658 New Beregn</strong>
<ul><li>A new setup is now available in Eik Setup under the V2 group, allowing users to trigger Beregn V2 when working with prescriptions that have reimbursement.</li><li>When this setup is active, the system now calls Eik with the updated Beregn V2 request and processes the Beregn V2 response.</li><li>Changing to Beregn V2 should not affect how reimbursements are processed in the prescription flow. It should behave and calculate the amounts in the same way.</li></ul>
<strong>72082 HON-19683 “NMD-MVQUEUE” should ignore medicines that cause errors in the verification queue</strong>
<ul><li>The Medicines Verification Queue logic was updated so it does not stop on error records and only retries records that failed due to communication exceptions.</li></ul>
<strong>72546 APB-851 Possible to add date in the future when creating a journal note</strong>
<ul><li>Functionality fixed:<ul><li>When doing journaling note system prevents to set future date:<ul><li>when registering Journaling note it is not possible to enter free text into fields Contacted Doctor, Journaling Origin, Initiated by - only choose or input values that are in linked Object Identifier.</li><li>when searching for GJD it is possible to change AKO.</li></ul></li></ul></li><li>When doing journaling note system prevents to set future date:<ul><li>when registering Journaling note it is not possible to enter free text into fields Contacted Doctor, Journaling Origin, Initiated by - only choose or input values that are in linked Object Identifier.</li><li>when searching for GJD it is possible to change AKO.</li></ul></li><li>when registering Journaling note it is not possible to enter free text into fields Contacted Doctor, Journaling Origin, Initiated by - only choose or input values that are in linked Object Identifier.</li><li>when searching for GJD it is possible to change AKO.</li></ul>
<strong>72552 Parental responsibility not displayed correctly when using HentPerson v2</strong>
<ul><li>Display of father and mother NIN already corrected in other issue. The display of parental responsibility was fixed. When the  parental responsibility is shared, the correct code is 1 (Shared), since this is the code that is mapped to status <b>Shared</b>. When both father and mother are in parental responsibility, only the first is displayed.</li></ul>
<strong>72553 APB-868 Address missing information when using HentPerson v2</strong>
<ul><li>The house number and house letter were added to customer address line like that:<b> "&lt;Address&gt;, &lt;house number&gt;&lt;house letter&gt;"</b></li><li>Changed the mapping of County Code: municipalityNumber now is a County Code in the system (previously the countyNumber was as a County Code)</li><li><b>Important note</b>: Lookup field is had for County Description, so it looks in Object Identifier table and finds the description, (does not map from API respond). Make sure you have correct values in Object Identifier table for County Description with current County Code.</li></ul>
<strong>72596 Update script for multiple extended tables in BC14 to single extended table in latest</strong>
<ul><li>The Update scripts were updated, adding support for processing multiple BC14 source tables into a single table in the latest version.</li></ul>
<strong>72977 CS0850155 - Wrong refund</strong>
<ul><li>The logic was updated to get the lowest generic price within the same exchange group.</li></ul>
<strong>72999 It should be possible to delete PRodGruppe Prescriptions after changing item selection multiple times</strong>
<ul><li>
<p>Check and re-order the Prescription order lines for prod group prescription.</p>
</li></ul>
<strong>73018 Make Sales Statistic Report in sync with CAL</strong>
<ul><li>Codeunits Eik Reporting NO and Sales Report Sales Order were synchronized.</li></ul>
<strong>73075 APB-890 Nav Application closes when trying to initiate a PSD</strong>
<ul><li>Review the logic of initiate PSD action in pdd details so the NAV Application does not close on error.</li></ul>
<strong>73198 ,,Group" text in Update PDD</strong>
<ul><li>Page layout for <b>PDD Update page</b> was fixed. </li></ul>
<strong>73371 Public Access to Selected Functions in Codeunit "LSC PH Agent Utility"</strong>
<ul><li>Details not available.</li></ul>
<strong>73383 PSD Details not accessable with V2 = TRUE</strong>
<ul><li>A null-check was added for EikFellesInfoIntern to prevent <b>DotNet variable not instantiated</b> errors when mapping pharmacy fields.</li></ul>
<strong>73690 Error when posting prescription with GJD linked to PSD line</strong>
<ul><li>There was an error when posting GJD document that is linked to a PSD Line. This was fixed. </li></ul>
<strong>73983 Error in Beregn v2 - ReseptUtleveringListeID should be the same for all prescriptions in the same prescription order, but it's not.</strong>
<ul><li>When using beregn v2, the node <b>ReseptUtleveringListeID</b> must be the same for all prescriptions in the same prescription order in the Beregn Request.</li></ul>
<strong>74000 Error found in release 3.01.61.1 - Delivered ticket PCPS-2570 PDD - Active substance prescriptions shows wrong data in PDD</strong>
<ul><li>In the PDD Details the fields Quantity, Packs &amp; Total Quantity show correct information.</li></ul>
<strong>74046 Old NIN not displayed in customer information</strong>
<ul><li>The old NIN was mapped from hentReseptv2.</li></ul>
<strong>74116 Error found in production: No new labels are printed out when user reopens a prescription order line and first changes quantity and then dosage text.</strong>
<ul><li>Make sure that the labels are updated when the Dose texts are updated as well.</li></ul>
<strong>74145 Improvement on water value (DMP audit)</strong>
<ul><li>Made <b>Water Added User</b> editable and blocked prescription confirm until <b>Water Values</b> are accepted by a pharmacist.</li><li>This is enabled according to the setup on the prescription setup profile by the field Water Values Confirm on Approval.</li></ul>
<strong>74255 Field Prescribed Qty were added to Al pages for Brand/Active:</strong>
<ul><li>Edit Prescription Order Line.</li><li>Posted Prescription Order line.</li></ul>
<strong>74256 Add application area to AL NO objects</strong>
<ul><li>Application area was added to AL NO objects.</li></ul>
<strong>74263 Beregn V2 bug fixings</strong>
<ul><li>Bugs in Beregn V2 were fixed, regarding handling of prescriptions coming with reimbursement errors from hentResept.</li></ul>
<strong>74369 Persontjenesten V2.0 - The hentPersonV2_Request is sent twice during customer identification</strong>
<ul><li>Details not available.</li></ul>
<strong>74430 Beregn V2 Order Error Handling when Beregn errors in multiple lines</strong>
<ul><li>Resolved an issue where, in prescription orders containing multiple lines with §3 blocking alerts, adding reimbursement code, decision date, and Helfo office to a line incorrectly triggered a blocking alert from Beregn indicating that the information was still missing for that same line.</li></ul>
<strong>74500 Label barcode position after size increase</strong>
<ul><li>Changed position of the control label barcode to avoid not beeing printed in some printer versions.</li></ul>
<strong>74864 PREG no longer available</strong>
<ul><li>
<p>Fixed issues affecting the following flows:</p>
<ul>
<li>Running Test EIK connection in EIK Setup.</li>
<li>Creating a paper prescription or downloading an e-prescription and adding a paper prescription to the same prescription order (now both can be added correctly to the same order).</li>
</ul>
</li><li>Running Test EIK connection in EIK Setup.</li><li>Creating a paper prescription or downloading an e-prescription and adding a paper prescription to the same prescription order (now both can be added correctly to the same order).</li></ul>
<strong>74869 ,,The value "1forste" can't be evaluated into type integer" error</strong>
<ul><li>A blocking error was fixed, related to expanded dosage text functionality when downloading a prescription for item 094383 Azitromax tab 500mg.</li><li>The mapping of dosage units was fixed, when the dosage is missing a space between the number and the text.</li></ul>
<strong>74889 BLOCKER: Error in Prescription posting queue: "The value "N" can't be evaluated into type Integer" for foreign prescription orders with journal entry</strong>
<ul><li>The Request <b>lagreGeneriskJournalDokument</b> was changed, the Ident node for Foreign customer was skipped, the error was skipped.</li></ul>
<strong>74906 APB-1006 Ensure that the pharmacist approves break pack (DMP requirement)</strong>
<ul><li>Blocked prescription approval until Break Pack values are accepted by a pharmacist.</li><li>This is enabled according to the setup on the prescription setup profile by the field Break Pack Values Confirm on Approval.</li></ul>
<strong>74986 HON-21458 BeregnV2_ error exception when 'vernepliktig' as Exemption Type</strong>
<ul><li>Vernepliktig is assigned a value of True or False in Beregn_Request based on the exemption type specified in the prescription order line. When exemption Type V ‘vernepliktig’ is set to True, otherwise it is False.</li></ul>
<strong>75037 Deviation Scenario Beregn V2 - (AL Only)</strong>
<ul><li><b>ReseptUtleveringsListeID</b>was added to POL and Posted POL to support the new deductible handling model.</li><li>PDD Details were updated to store the new <b>PrescriptionDispensingListId</b>.</li><li>QC was updated, Lagre and Oppdatter endpoints (active only when Beregn V2 is enabled).</li><li>The new API was implemented, DLLs were updated, and CAL code was adjusted to support all changes.</li></ul>
<strong>75104 BLOCKER - Not possible to credit PSD – Error message: "You can not cancel a PSD that was created from another pharmacy"</strong>
<ul><li>Now the user can credit a PSD.</li></ul>
<strong>75472 Beregn: Send HarTidligereBetaltEgenandel should be true  when ReseptutleveringsListeID as changed by the PE</strong>
<ul><li>When a pharmacist manually edits the <b>ReseptutleveringsListeID</b> to match a previous delivery, the system sets <b>HarTidligereBetaltEgenandel</b> to true. The Beregn request is sent taking into account the different <b>ReseptutleveringsListeID</b> values in the order. The <b>HarTidligereBetaltEgenandel</b> field is subsequently determined based on the information in each prescription order line.</li></ul>
<strong>75543 ReseptUtleveringListeID Instanced multiple times if order has more than one line for the same ReseptUtleveringListeID</strong>
<ul><li><b>ReseptUtleveringListeID</b> should be created once for every unique value present in an order. Since an order can contain multiple lines, and those lines may either share the same <b>ReseptUtleveringListeID</b> or differ (for example, when a PE manually adjusts values to match a previous delivery). The request must reflect this.</li><li>When generating the JSON request, include exactly one ReseptUtleveringListeID entry for each distinct ID found in the order.</li></ul>
<strong>75551 ProdGrupe with new beregn missbehavior</strong>
<ul><li>When adding lines to a product group prescription, the reimbursement values and/or alerts are correctly mapped for each line.</li></ul>
<strong>75598 Water value - Added by and approved by in PDD and In Backoffice is not correct</strong>
<ul><li>For this modification to work correctly, the <b>Water Values Confirm on Approval</b> setting must be enabled on the Prescription Setup Profile. Changes:<ul><li>The <b>Accepted By</b> field was added to the <b>Posted Presc. Water Qty NO (10037931)</b> page. The page now displays three key fields: <ul><li>Added By</li><li>Accepted By</li><li>Approved By, since each of these actions can be performed by different users.</li></ul></li><li>The mapping of the <b>Accepted By</b> field was fixed in the <b>PDD Details</b> FactBox so that it now shows the correct value.</li><li>The <b>Added By</b> field was removed from the PDD Details FactBox, because this value is not sent to Eik and is not returned in the Eik response, so it was always empty.</li><li>With the <b>Water Values Confirm on Approval</b> = true, the line can not be confirmed if water quantity is not Accepted.</li><li>Editable property on <b>Page Prescr Order Line Water Qty NO</b> was fixed, during confirming and reopening POL process.</li></ul></li><li>The <b>Accepted By</b> field was added to the <b>Posted Presc. Water Qty NO (10037931)</b> page. The page now displays three key fields: <ul><li>Added By</li><li>Accepted By</li><li>Approved By, since each of these actions can be performed by different users.</li></ul></li><li>Added By</li><li>Accepted By</li><li>Approved By, since each of these actions can be performed by different users.</li><li>The mapping of the <b>Accepted By</b> field was fixed in the <b>PDD Details</b> FactBox so that it now shows the correct value.</li><li>The <b>Added By</b> field was removed from the PDD Details FactBox, because this value is not sent to Eik and is not returned in the Eik response, so it was always empty.</li><li>With the <b>Water Values Confirm on Approval</b> = true, the line can not be confirmed if water quantity is not Accepted.</li><li>Editable property on <b>Page Prescr Order Line Water Qty NO</b> was fixed, during confirming and reopening POL process.</li></ul>
<strong>75631 GJD issues</strong>
<ul><li>Functionality was fixed:<ul><li>It is possible to process prescription with GJD in posting queue for PhCustomer of all types - customer with NIN, customer without NIN, foreigner, animal prescription.</li><li>It is possible to open PDD Details for prescription with ProdGroup line/lines for no NIN customers.</li></ul></li><li>It is possible to process prescription with GJD in posting queue for PhCustomer of all types - customer with NIN, customer without NIN, foreigner, animal prescription.</li><li>It is possible to open PDD Details for prescription with ProdGroup line/lines for no NIN customers.</li></ul>
<strong>75691 Deliveries with reimbursement 605, 606 etc. fail in Eik due to handelsvareAnnen object</strong>
<ul><li>Code was updated to reflect the new Eik changes that expand the product group code intervals.</li><li>The new product group ranges are 500–515 and 600–609.</li><li>In the quality check, all product groups within these ranges must no longer be classified as handlesvareannen. Instead, they should be assigned to their respective classes.</li></ul>
<strong>75773 Implement TODOs missing in AL NO related to beregn v2</strong>
<ul><li>TODOs missing was implemented in AL NO related to beregn v2.</li></ul>
<strong>75824 NavJsonToken Error when confirming eprescription AL Kvalitettssjek V3.0</strong>
<ul><li>An error was fixed, related to NavJsonToken mapping when confirming eprescription AL Kvalitettssjek V3.0.</li></ul>
<strong>75825 Cleanup of Dropped Properties in resept Mapping for Kvalitetssjekk V3</strong>
<ul><li>Mapping was updated in class Resept and related sub-objects  in kvalitettssjek v3 request, to ensure dropped fields are removed from the outgoing JSON, and no errors related to extraneous keys are returned from Eik on confirm.</li></ul>
<strong>75910 Old Session Line Causes Error When Creating New Prescription Orders</strong>
<ul><li>
<p>There was an issue where outdated prescription line data remained in the user session. The logic was updated to ensure that session data is properly instantiated whenever a new prescription workflow begins. New prescriptions are now correctly initialized with new line data, preventing references to previous orders.</p>
</li></ul>
<strong>75999 Not able to check settlement claims because of string length error</strong>
<ul><li>
<p>A fix was applied to ensure that ErrorRecM18 is limited now to 250 characters. If the message exceeds this length, the system automatically trims it.</p>
</li></ul>
<strong>76079 ,,DotNet variable has not been instantiated" - NO.Eik.RFClient.HentUtleveringDokumentV3</strong>
<ul><li>.NET error were fixed, when opening posted prescription order line from posted orders.</li></ul>
<strong>76090 ,,Unable to convert from Microsoft.Dynamics.Nav.Runtime.NavJsonToken to blablabla"</strong>
<ul><li>Errors were fixed on confirm, related to JsonToken handeling.</li></ul>
