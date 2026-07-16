---
title: "Pharmacies hotfixes - 28.0.10 Pharmacies, Release date June 9, 2026 - Hotfixes"
product: Pharmacies
version: "28.0.10"
subproduct: Pharmacies
minor_version: "28.0"
date: 2026-06-09 00:00:00+00:00
order: 98
guid: d3614eca3defdc6bd9a630966ab766a42745cfb0
---

<strong>76250 Pharmacy Customer Orders Implementation.</strong>
<ul><li>LS Central removed obsolete components that previously impacted the Pharmacy Customer Orders logic. This epic introduces the necessary changes to restore the existing functionalities so they work correctly under the updated LS Central logic.</li></ul>
<strong>79751 Pharmacy and CO Implementation - Deprecate Status Field on Collect Panel</strong>
<ul><li>The Pharmacy CO Collect Panel is now compliant with the new quantity logic.</li></ul>
<strong>79752 Pharmacy and CO Implementation - Deprecate Status Field on B2B Panel</strong>
<ul><li>Details not available.</li></ul>
<strong>79788 Pharmacy and CO Implementation - Deprecate Status Field on Approval Subscribers</strong>
<ul><li>Approval subscribers should comply with the new logic and set the lines ready to be collected.</li></ul>
<strong>79815 Pharmacy and CO Implementation - Refactor of FinalizeOrderB2BPharmacy</strong>
<ul><li>Refactor of FinalizeOrderB2BPharmacy.</li></ul>
<strong>79909 Pharmacy and CO Implementation - Deprecate Status Field on List Panel</strong>
<ul><li>Details not available.</li></ul>
<strong>79948 Pharmacy and CO Implementation - Pharmacy Update endpoint</strong>
<ul><li>UpdateOrderLine is now complying with the new Quantity logic.</li></ul>
<strong>79953 Pharmacy and CO Implementation - Pharmacy Filtering</strong>
<ul><li>Complying with the new Qty. logic.</li></ul>
<strong>80158 Pharmacy and CO Implementation - Fix Status of CO Header on List Panel</strong>
<ul><li>Details not available.</li></ul>
<strong>80234 Pharmacy and CO Implementation - Fix Approval Flow and Add To RX Button To POS</strong>
<ul><li>Details not available.</li></ul>
<strong>80292 Customer Orders - Refactor Deleting Process Linked Prescription Order Line</strong>
<ul><li>Details not available.</li></ul>
<strong>80301 Display the "ship" Customer Orders in POS</strong>
<ul><li>Details not available.</li></ul>
<strong>80349 Stay in the same panel after creating the prescription order from CO</strong>
<ul><li>A new logic was implemented to keep the panel open. If there are still lines pending to be processed, the panel now remains open instead of closing.</li></ul>
<strong>80350 Go to #COB2CPHLINES panel when closing the prescription panel</strong>
<ul><li>There was an issue in the prescription panel flow: When leaving the prescription panel by completing the pharma flow, and choosing to continue with the customer order, the system now correctly returns the user to the CO panel (#COB2CPHLINES) instead of navigating to the list.</li></ul>
<strong>80351 Pharmacy and CO Implementation - Refactor OnBeforeCustomerOrderFinished</strong>
<ul><li>Details not available.</li></ul>
<strong>80353 Wrong sourcing location for PH CO</strong>
<ul><li>During the Sourcing Location refactor, due to a deprecated XML version, a piece of code was commented out and never undone. That was corrected under this ADO Issue, and the functionality was recovered.</li></ul>
<strong>80354 Confirmation dialog to delete prescription displayed when creating a CO</strong>
<ul><li>Confirmation dialog does not pop up anymore.</li></ul>
<strong>80366 Customer Orders - Deprecate Field Status on ChangeCOLineInternalStatus</strong>
<ul><li>Details not available.</li></ul>
<strong>80381 Customer Orders - Deprecate Status field from CO Codeunits</strong>
<ul><li>Details not available.</li></ul>
<strong>80408 Pharmacy and CO Implementation - Record in table already exists</strong>
<ul><li>RX POS Transaction Lines are being created regardless of whether LS Central creates additional POS Transaction Lines.</li></ul>
<strong>80496 CO Ship orders - the RX flag missing in Sales Line</strong>
<ul><li>Pharmacy fields not populated on Sales Order lines created from Customer Orders<ul><li>The event <b>OnBeforeCreateSalesLineFromCustomerOrderLine</b> on the Customer Order Header table is no longer raised after the LS Central refactoring to interface-based Customer Order Line processing. This caused pharmacy-specific fields (RX flag, Customer Order Line No., VAT Posting Group) to not be set on Sales Order lines.</li></ul></li><li>The subscriber has been migrated to the <b>OnPopulateSalesLineBeforeValidateUnitPrice</b> event from codeunit <b>LSC CustomerOrderLineEvents</b>, which is actively raised during the new Sales Line population flow.</li></ul>
<strong>80499 CO Ship orders - empty sales shipments created</strong>
<ul><li>The Sales Shipment is not being created during the Customer Order Line confirmation anymore.</li></ul>
<strong>80663 Customer Orders - Deprecate Status field from CO Tables</strong>
<ul><li><b>Status</b> Field was obsoleted from current list of tables and also the fields:<ul><li><b>LSC PH Total Amount</b> in Customer Order and Posted Customer Order table were obsoleted</li><li><b>LSC PH Lines to RX</b> in Customer Order and Posted Customer Order table were added</li><li><b>LSC PH Calc. Cust. Order</b> in <b>LSC Inventory Lookup Table</b> were obsoleted ( new procedure was added instead: <b>LSCPH_CalcOpenCustOrderQty</b>).</li></ul></li></ul>
<strong>80935 Customer Orders - Refactor the OnBeforeAddPaymentToCustomerOrder</strong>
<ul><li>The subscriber <b>OnBeforeAddPaymentToCustomerOrder</b> was refactored. </li><li>The subscription was changed to new publisher <b>OnBeforeAddPaymentToCustomerOrderV2</b>.</li><li>Also Calculation of Collected amount was changed regarding to new approach.</li></ul>
<strong>80940 CO not posted after collecting it in POS</strong>
<ul><li>The POS transaction is correctly created without any error and the prescription is correctly sent to the posting queue. Also Customer order is being posted after finalizing the process.</li></ul>
<strong>81593 Animal prescription (LSC PHNO Paper Prescription (10061657, Card))</strong>
<ul><li>Norwegian translations were updated in Animal Prescription Order.</li></ul>
<strong>82353 "Emergency prescription" LSC PHNO Paper Prescription (10061657, Card)</strong>
<ul><li>Missing/incorrect translations were added. </li></ul>
