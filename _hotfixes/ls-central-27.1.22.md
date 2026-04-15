---
title: "LS Central hotfixes - 27.1.22, Release date April 10, 2026 - Hotfixes"
product: LS Central
version: "27.1.22"
subproduct: 
minor_version: "27.1"
date: 2026-04-10 00:00:00+00:00
order: 1
guid: aa455d9f74c98b5c3ef04ac11413edfb491396f8
---

<strong>80375 Integration Event for Transfer Order Creation from Planned Stock Demand</strong>
<ul><li>The integration event <b>OnCreateTOFromPlannedStockDemandOnBeforeProcessReplenPlannedStockDem</b> was added to the codeunit <b>LSC Replen. Create Transf. Ord.</b></li></ul>
<strong>80358 AL: Variant Logical Order Not Respected in LS Central and Shopify Sync</strong>
<ul><li>Logical order of Options values (Variants) was fixed in Shopify product.</li></ul>
<strong>80170 AL: Capturing of Payment data</strong>
<ul><li>PaymentId was added to Shopify order graphQL request.</li></ul>
<strong>79935 EventSubscriber needed for LSC POS Transaction Codeunit - procedure ProcessCoupon- LS Central OnPrem Version 27.1</strong>
<ul><li><b>OnAfterFindCouponTenderType_OnProcessCoupon</b> event was added and  coupon tender type handling was updated. </li></ul>
<strong>79934 EventSubscriber needed for LSC POS Transaction Codeunit - procedure TotDiscAmPressed- LS Central OnPrem Version 27.1</strong>
<ul><li>New event <b>OnTotDiscAmPressedOnBeforeTotDiscAmPressCheck</b> was added to <b>LSC POS Transaction Impl</b> codeunit.</li></ul>
<strong>79771 Add Get check before validating Store-to #634</strong>
<ul><li>New event <b>OnBeforeValidateTransferHeaderStoreTo</b> was added to <b>LSC Picking/Receiving - Post</b> codeunit.</li></ul>
<strong>79756 Receipt number for Shipment Customer Orders (follow up from 77144)</strong>
<ul><li>Fix on receipt number generated when posting a CO from web as SO.  Related to 77144.  </li><li><b>Note:</b>  Terminal that handles Sales Orders (Sales Order Terminal No. in Customer Order Setup) should not be used as a regular POS Terminal as the numbers series may collide.</li></ul>
<strong>79731 ECOM 26.1 FactBox & rounding issue</strong>
<ul><li>Incorrect tax amount was fixed in Posted Customer Order FactBox.         │</li><li>Invoice rounding amount on Customer Order returns was fixed. </li></ul>
<strong>79693 Customer Order Details Showing pending Amount</strong>
<ul><li>Calculate Non-Refundable Amount in Posted Customer Order Details Infopanel.</li></ul>
<strong>79553 Mobile Inventory - CheckLicenseStatus error</strong>
<ul><li>Adjustments were made to the <b>GetLicenseUnit webservice process</b> to help with deadlocks.</li></ul>
<strong>79258 Time zone dealing web services</strong>
<ul><li>Time field in Transaction created through CustomerOrderCreate webservice was adjusted to account for Time offset for different Region Timezones.</li><li>Time field in Transaction created through Self Checkout Start Transaction web service was adjusted.</li></ul>
<strong>79255 SCO - Transaction Time Issue</strong>
<ul><li>Details not available.</li></ul>
<strong>78370 Franchise orders breaking in 27.1</strong>
<ul><li>Franchise Module:<ul><li>Franchise document replication counter assignment was migrated from a manual table-locking approach on LSC Franchise Setup to BC's built-in Sequence No. Mgt. codeunit. This resolves concurrency issues that could cause franchise orders to break when multiple outbound franchise documents were created simultaneously.</li><li>An upgrade procedure (<b>UpgradeFranchiseReplicationCounterToMBCSequenceMgt</b>) was added that seeds the BC sequence number to match the highest previously-used replication counter, preventing duplicate counter values after upgrade.</li><li>Purchase Order not deleted when Auto Post option used was fixed.</li><li>OnBeforeInsertEventForSoLine in Franchise process that issued a warning <b>This order is a Franchise order....</b> was removed to help Sales process to add new lines to an order.</li></ul></li><li>Franchise document replication counter assignment was migrated from a manual table-locking approach on LSC Franchise Setup to BC's built-in Sequence No. Mgt. codeunit. This resolves concurrency issues that could cause franchise orders to break when multiple outbound franchise documents were created simultaneously.</li><li>An upgrade procedure (<b>UpgradeFranchiseReplicationCounterToMBCSequenceMgt</b>) was added that seeds the BC sequence number to match the highest previously-used replication counter, preventing duplicate counter values after upgrade.</li><li>Purchase Order not deleted when Auto Post option used was fixed.</li><li>OnBeforeInsertEventForSoLine in Franchise process that issued a warning <b>This order is a Franchise order....</b> was removed to help Sales process to add new lines to an order.</li></ul>
<strong>77910 Kitchen Line Routings-Date Time Started on Station (Standard KDS 25.1)</strong>
<ul><li>Some new calculations were added on the Date Time started and Date Time Finished.</li></ul>
<strong>77089 Refund from another store with Sales Type creates incorrect Item Ledger entry</strong>
<ul><li>The Salestype location will not overwrite the store location when doing a refund at a different store.</li></ul>
<strong>68110 Incorrect Payment Amount on CO Creation fix for LS26.0 and LS26.1</strong>
<ul><li>Details not available.</li></ul>
<strong>68019 Restore Archived Offer Deletes all Periodic Disc Lines</strong>
<ul><li>Details not available.</li></ul>
<strong>67983 POS EFT Card - Client Transaction ID Type</strong>
<ul><li>Configuration <b>Client Transaction ID Type</b> has a new option called <b>POSTerminal+CardEntryNo</b> which creates a Client Transaction ID from the POS Terminal and Card Entry No. </li><li>This option does not have any formatting or extra characters and  works when the POS Terminal for example has only two numbers in it's unique ID or no numbers at all.</li></ul>
<strong>67941 [EVENT PARAMETER] Receive the codeunit instance in the OnBeforeSendWholeTmpTransaction event #519</strong>
<ul><li>Details not available.</li></ul>
<strong>67940 [EVENT PARAMETER] Add DiscPrPerLine as var parameter of OnBeforeRegisterMixMatchLeastExpensive event #518</strong>
<ul><li>Details not available.</li></ul>
<strong>67919 All Day availability calculation causes performance issues when Group Line product is entered.</strong>
<ul><li>A change was made to the group line entry process,  that is, availability for the product is not calculated unless a start time and date has been assigned to the line.</li></ul>
<strong>67897 Booking Archiving changes</strong>
<ul><li>The archiving process was modified to only skip groups and/or reservations, which have a balance.  The internal status or the payment status is ignored.  <b>Note</b>: Closed status  forces archiving regardless of the reservation balance.  Rental reservations with units not returned are not archived.</li></ul>
<strong>67866 SCO - Posting card additional entries and free text. HL</strong>
<ul><li>Details not available.</li></ul>
<strong>67865 Control of print customer slip #515</strong>
<ul><li>Four New events in POS Print Utility:<ul><li>OnBeforePrintCustomerInformation</li><li>OnAfterPrintCustomerInformation</li><li>OnBeforePrintContactInformation</li><li>OnAfterPrintContactInformation.</li></ul></li><li>OnBeforePrintCustomerInformation</li><li>OnAfterPrintCustomerInformation</li><li>OnBeforePrintContactInformation</li><li>OnAfterPrintContactInformation.</li></ul>
<strong>67860 Events for Replen. Item Profiles #512</strong>
<ul><li>The following integration events have been added to the public codeunit <b>LSC ReplenUpdFromProf Public</b>, which are accessible by the codeunit <b>LSC Replen. Upd From Profile:</b><ul><li>OnUpdateFromProfileOnBeforeProcessItemProfile</li><li>OnUpdateFromProfileOnBeforeProcessItemProfileForAllLocations</li><li>OnUpdateFromProfileOnBeforeProcessItemProfileForOthers</li><li>OnBeforeInsertItemStoreRec</li></ul></li><li>OnUpdateFromProfileOnBeforeProcessItemProfile</li><li>OnUpdateFromProfileOnBeforeProcessItemProfileForAllLocations</li><li>OnUpdateFromProfileOnBeforeProcessItemProfileForOthers</li><li>OnBeforeInsertItemStoreRec</li></ul>
<strong>67808 Unable to Scan Booking Codes – DEVICEINPUT Invokes CODEUNIT.Run Before Current-Message Is Populated</strong>
<ul><li>Details not available.</li></ul>
<strong>67787 After upgrade the 26.0.9 hotfix then POS receipt is not going through Email on LIVE POS</strong>
<ul><li>The interface had a <i>not initialized error</i> when  emails were sent via job queue. This was fixed.</li></ul>
<strong>67684 Retail Item Registration No. Series Creation</strong>
<ul><li>The creation of the <b>Item Registration</b><b>No.</b> of the Retail Item Registration is now based on the <b>Create Items No. Series</b> in the Retail Setup.</li></ul>
<strong>67678 Fixed parameter passing in OnBeforeGetOrder procedure to allow modification</strong>
<ul><li>New event <i>OnBeforeGetSHSL</i> in <b>POS Order Connection</b> codeunit.</li></ul>
<strong>67677 New event OnBeforeCheckDiscDiffInPeriodicDiscountLines added</strong>
<ul><li>
<p>New event <i>OnBeforeCheckDiscDiffInPeriodicDiscountLines</i> in <b>POS Price Utility</b> codeunit.</p>
</li></ul>
<strong>67666 Member Point Transfer Journals post generates an error because the batches selected and shown are not 'Transfer' batches</strong>
<ul><li>Details not available.</li></ul>
<strong>67665 Member point journal should not have the 'Transfer' type available for selection</strong>
<ul><li>Details not available.</li></ul>
<strong>67654 Error when Member Contact Popup searches opens</strong>
<ul><li>Details not available.</li></ul>
<strong>67627 SCO : Coupons do not work with Affect = Next Item Line</strong>
<ul><li>Self Checkout Units were enabled to use Coupons activated by next or previous item in a backet.</li></ul>
<strong>67571 Error when applying discount percent on a deal - CRITICAL</strong>
<ul><li>Details not available.</li></ul>
<strong>67567 POS Member Contact Popup - Select Club - Direct</strong>
<ul><li>When selecting Member Club through POS popup, if the user only has one item to choose from code, then it goes directly into processing instead of popping up a selection list of one item.</li></ul>
<strong>67548 When posting a transaction - remove date filter from POS Card Entry section of posting</strong>
<ul><li>If a sale was created before midnight and then paid for after midnight the Card Entry information was not included when updating the sale with the transaction no. in the Posting utility. This was fixed.</li></ul>
<strong>67546 Type Mismatch Member Points Decimal->Integer CU 10016111</strong>
<ul><li>Details not available.</li></ul>
<strong>67524 Add integration events for CalcTotalOffer</strong>
<ul><li>New events added to POS Offer Ext. Utility codeunit - <i>OnCalcTotalOfferAfterInitAmountDiscPerLine</i> and <i>OnCalcTotalOfferBeforeCheckDiscDifference</i></li></ul>
<strong>67514 Event Request</strong>
<ul><li>
<p>Events <i>LSRetailTransferLineItemNoOnAfterValidateOnBeforeGetItemEvent</i> and <i>OnBeforeSaveStoreFromDimSetTransferHeaderGet</i> were added in codeunit Retail Transfer Order Ext.</p>
</li></ul>
<strong>67512 Keyboard shortcuts (POS Key Commands) are not working</strong>
<ul><li>Details not available.</li></ul>
<strong>67483 Complete Reset Button. Adjust comment out code for Instance deactivation</strong>
<ul><li>Reset button was added. It is used, if the instance was deactivated. The action tries to re-activate the instance.</li><li>Check if the table is temporary when deleting records on the Company table.</li></ul>
<strong>67478 Cannot Input Member Attribute Lookups</strong>
<ul><li>Details not available.</li></ul>
<strong>67476 Add Reset button. Temporarily remove deactivate instance</strong>
<ul><li>Add Reset button. Comment out deactivation code.</li></ul>
<strong>67462 LSC - BROKEN - SPLIT BILL WITH A DEAL - CRITICAL</strong>
<ul><li>Details not available.</li></ul>
<strong>67455 Make enum 10012304 "LSC Alloc. Rule Share Type" extensible #504</strong>
<ul><li>Details not available.</li></ul>
<strong>67351 Subscriber addition request for member point calculations</strong>
<ul><li>New events added to PosCalcMemberPointsPublic - OnBeforeGetPointTender and OnBeforeInsertPointEntry. </li><li>New events added to Member Posting Utils - OnAfterTransPointEntryIsEmpty and OnBeforeGetBenefitAndTender_SalePoints.</li></ul>
<strong>67266 New Integration Event for Replenishment Calculation</strong>
<ul><li>An integration event <i>OnAfterCopyDataProfileToItemStore</i> was added to the codeunit <b>LSC Replen. Calculation</b>.</li></ul>
<strong>67265 Add Event to Add New Account Type in Tender Type</strong>
<ul><li>New event <i>OnValidateAccountNameForExtEnumAccountType</i> added to <b>Tender Type</b> table.</li></ul>
<strong>67243 Error on Shopify Order Import</strong>
<ul><li>Fixed handling of shipping line in Shopify order.</li></ul>
<strong>67202 Self checkout connector not storing card payment information</strong>
<ul><li>Details not available.</li></ul>
<strong>67190 feat(SC-1690): New/Update Event for Redemption of GC Barcode #502</strong>
<ul><li>New event added in POS Infocode Utility – OnBeforeCheckZeroInBarcode.</li><li>New event added in POS Transaction Server Utility – OnBeforeGetDataEntry2, replaces OnBeforeGetDataEntry and the second parameter is of type var.</li></ul>
<strong>67189 When “Sale Slip” is set to Email (POS terminal Card) the print option does not print a receipt when the “Print” option is selected at the end of a transaction</strong>
<ul><li>Prints receipt when the  print option at the end of a transaction is selected.</li></ul>
<strong>67188 New event: (OnBeforeProcessMemberEmailInput) request in codeunit 99001574 "LSC POS Transaction Events"</strong>
<ul><li>New event added in POS Transaction Events - OnBeforeProcessMemberEmailInput.</li></ul>
<strong>67187 Giftcard no gets picked up as another barcode mask</strong>
<ul><li>Allows gift cards already created with numbers and letters to be used.</li></ul>
<strong>67105 WebServicesClient instance in POS Member Contact Popup #501</strong>
<ul><li>Details not available.</li></ul>
<strong>67064 Customer Order - Statement Post rounding Error</strong>
<ul><li>Solved statement posting rounding error, for customer orders that were cancelled through Customer Order Edit process. Extra Refund line, if the refund is posted to the Customer Account, was removed. </li></ul>
<strong>67062 Error with Assembly Item Return – Incorrect Item Ledger Entries After Upgrade</strong>
<ul><li>Details not available.</li></ul>
<strong>67054 Ishandled reset missing on several publishers in CU POS Transac… #470 HF</strong>
<ul><li>Added IsHandled = false before the events.</li></ul>
<strong>67024 Event beforeOnBeforePrintingTransfer- transfer table printing</strong>
<ul><li>Event has been added to <i>Send to KDS Transfer codeunit</i> - <i>OnBeforePrintingTransfer</i> - that can be used to skip printing the transfer between dining tables.</li></ul>
<strong>67013 Store Inv Worksheet - All Areas being deleted incorrectly</strong>
<ul><li>When a Store Inventory Worksheet is deleted, all Worksheet Area data was being deleted, if the Store Inventory Worksheet in question was not using Area.</li></ul>
<strong>66997 SC-1037 Adding new event in POS Print utility for barcode printing on</strong>
<ul><li>New event <i>OnBeforePrintBarcodeOnExtraSlip</i> in POS Print Utility codeunit.</li></ul>
<strong>66962 SAAS to OnPrem Azure Web Replication problem not able to insert data in to table</strong>
<ul><li>Details not available.</li></ul>
<strong>66949 Store coupons not working properly after BC environment updated to v.26</strong>
<ul><li>Bugfix - Coupon application returning an error as Coupon was not open when in fact it was.</li></ul>
<strong>66939 Customer Order Shipping Charge Price Change Issue</strong>
<ul><li>
<p>When a <b>Customer Order Shipment</b> item is configured to always ask for price input it overwrites a item price and does not create a new <b>Trans line</b> with the shipment cost. This was fixed.</p>
</li></ul>
<strong>66893 We need possibility to skip CheckRemainingAmount function in LSC POS Transaction Impl. Codeunit</strong>
<ul><li>Details not available.</li></ul>
<strong>66890 AL: HospType missing in Store Repl</strong>
<ul><li>Added missing Sales Type Filter to <i>GetStoreBuffer</i> Replication function.</li></ul>
<strong>66885 Send Transaction from Offline POS to SaaS head office Issues</strong>
<ul><li>Fixed S2S issues on V1 Web Requests.</li></ul>
<strong>66871 Member Point Journal infinit loop</strong>
<ul><li>Details not available.</li></ul>
<strong>66864 Kiosk Analytics and Product Recommendations capabilities</strong>
<ul><li>Two events have been added to the Self Service Functions codeunit: <i>OnBeforeGetInitialSettings</i> and <i>OnBeforeGetCrossSellsInfo</i>. Two procedures have been made public in Self Service Functions codeunit:  <i>CopyDynContentBuffer2Times</i> and <i>AddCrossSellingGroupsToJson</i>. Two procedures in Dynamic Content Mgt. are now accessible through Dyn. Content Mgt. Public codeunit: <i>InsertCrossSellingGrBuffer</i> and <i>AssignInfocodeGrBuffer</i>.</li></ul>
<strong>66863 Duplicate receipt printing on tender declaration and remove tender</strong>
<ul><li>Event was made to adjust number of slips (copies), to print for Float Entry and Remove Tender.</li></ul>
<strong>66846 AL: Inventory with multi Lot No dont show up correctly for Source Loc</strong>
<ul><li>Details not available.</li></ul>
<strong>66835 Test minimum quantity sales prices handled pattern #498</strong>
<ul><li>Event handling for testing Minimum Quantity Sales Price has been added.</li></ul>
<strong>66831 Change No. Series in POS data Entry</strong>
<ul><li>New field <i>No Series Code</i> (code 20) added to <i>POS Data Entry Type</i> table.</li></ul>
<strong>66823 Item modifier- course changing</strong>
<ul><li>Linked lines selected when changing course on an item in the POS (the MTYPE_CHG command).</li></ul>
<strong>66802 AL: Shopify Images Sync</strong>
<ul><li>Details not available.</li></ul>
<strong>66792 realtime stock without Automatic Stock Update</strong>
<ul><li>Running WI Update Inventory now includes quantity sold not posted from POS transactions in Total inventory quantities, also from stores linked to Customer Order Sourcing Locations.</li></ul>
<strong>66772 Unable to add products to the basket / New Codeunit missing in the v26 customer license</strong>
<ul><li>Details not available.</li></ul>
<strong>66758 New Events For Transaction Server #496</strong>
<ul><li>New event OnBeforeTSCheckError and OnBeforeTSSendUnsentTransactions added to <i>LSC POS Transaction Impl</i> codeunit.</li></ul>
<strong>66746 SaaS environments failing to upgrade to v26</strong>
<ul><li>Popup Types upgrade removed. Changes to Insert Default Popup Types function in Pop-up Types page done to prevent overflow in field insertion and inserting same record again (can happen in translation).</li></ul>
<strong>66740 Add integration event for ChangeStaffPressedOnClose procedure #495</strong>
<ul><li>New event OnBeforeChangeStaffPressedOnClose added to <i>LSC Additional POS Commands</i> codeunit.</li></ul>
<strong>66738 AddEventToStoreInvWkshtBufferFilter #494</strong>
<ul><li>New event OnAfterSetInvWrkshFiltersOnBuildPage added to <i>LSC Store Inv. Wrksh. Buffer</i> page.</li></ul>
<strong>66694 Request do add parameter to existing event</strong>
<ul><li>Details not available.</li></ul>
<strong>66673 Select New Card in MEMBERCONTACT POS Command does not return free cards for Member Club</strong>
<ul><li>Details not available.</li></ul>
<strong>66645 LSC NA - PRINT_SL Command - Continued</strong>
<ul><li>Fixed the incorrect tax amount when printing with PRINTBILL, SPLITBILL, and PRINT_SL.</li></ul>
<strong>66615 Image management #491</strong>
<ul><li>
<p>New event OnBeforeSetActiveImage added to <i>LSC Retail Image Link Factbox</i>.</p>
</li></ul>
<strong>66603 Event for preauth amount adjustment dialog</strong>
<ul><li>Details not available.</li></ul>
<strong>66584 EcomCalculateBasket Coupon Error: Interface not initialized</strong>
<ul><li>Details not available.</li></ul>
<strong>66581 Published Event on the Totals functions on activity total and group line total</strong>
<ul><li>
<p>Added published events to the Total() functions on all reservation tables for partners possibility of customization.</p>
</li></ul>
<strong>66578 26.0 Member Create on POS</strong>
<ul><li>Creating a Member through POS registered incorrect values in Account No and Member Club fields. This is fixed.</li></ul>
<strong>66564 Bug: Inventory availability calculations do not include quantities committed on click & collect customer orders</strong>
<ul><li>
<p>Display quantity reserved for Customer Order on three different item information pages.</p>
</li></ul>
<strong>66519 Infocode required no longer works properly with enhanced pop-ups</strong>
<ul><li>Enhanced Popup handling of reason codes with POS actions fixed. Refers to infocodes with no usage category and selection, without trigger functions.</li></ul>
<strong>66441 Tender Type Rounding 0.05 not working</strong>
<ul><li>Fixed Rounding issues on Customer orders.</li></ul>
<strong>66348 COMM_SHOWSALES - Command not working properly.</strong>
<ul><li>Active POS Transaction record set even if the #COMM-TOT comment grid is not in the #POS panel. Then the Comment panel opens up after the #POS panel is opened.</li></ul>
<strong>66331 Request to add an integration event after printing the VAT block in the OnPrintingTotalLineAtBottom procedure to allow custom logic injection before VAT info is printed</strong>
<ul><li>New event OnAfterVATSectionPrinted added to <u>LSC POS Print Utility Impl</u> codeunit.</li></ul>
<strong>66289 Refund Card Payments</strong>
<ul><li>A new configuration was added on POS Terminal card in the EFT section called "Use Refund Payment Selection".</li><li>When refunding multiple card payments in the POS, a list of card payments is displayed for the cashier to select which card payment should be refunded. This happens when "Use Refund Payment Selection" is activated. Information displayed in the dialog is the last four digits of the card number and the payment amount.</li><li>If there is only one card payment to be refunded, this dialog is not displayed. If the card payments that are selected for refund is higher than the remaining balance of the sale, then the POS does not allow the refund to go through.</li></ul>
<strong>66273 OnCreateItemOnBeforeModify and OnUpdateItemOnBeforeModify on LSC Item Import Create Codeunit</strong>
<ul><li>Make events OnCreateItemOnBeforeModify and OnUpdateItemOnBeforeModify public in  Item Import Create Codeunit</li></ul>
<strong>66267 AL: Granted Discount in Shopify Orders is not captured during settlement of Click & Collect transactions</strong>
<ul><li>Details not available.</li></ul>
<strong>66262 Group overbooking not working in version LS 25.3</strong>
<ul><li>Fixed an issue when confirming a group reservation line.  The group confirm process was not executed if the related product was already fully booked.   Now the process checks if the user is allowed to overbook, or if the related product has overbooking options assigned.  <b>Note</b>: On Activity Packages, which include products that have overbooking settings, the user must also set the overbooking setting on the Package base product as well (even though the base product is not having resources).  This is to bypass the overbooking pre-checking during the group confirmation process.</li></ul>
<strong>66213 Unknown error in Transaction Register</strong>
<ul><li>There was an  issue in the POS Lookup functionality where a wrong InterfaceProfileID Filter was created when showing the Lookup (and LookupData) panels. This was fixed. </li></ul>
<strong>66203 Adding events #489</strong>
<ul><li>Two new events OnAfterSetItemPrice and OnAfterProcessInfocodeResult in Codeunit Pos Transaction Events.</li></ul>
<strong>66188 AL: Add ImageId to Node leaf</strong>
<ul><li>ImageId was added to <b>RootGetHierarchyNodeOut</b> in WS Function <b>GetHierarchyNode</b>.</li></ul>
<strong>66167 The length for FixedLocation code needs to be increased from 10 to 20 characters</strong>
<ul><li>The length for FixedLocation code was increased from 10 to 20 characters.</li></ul>
<strong>66078 Prices in Package Offer Lines are displayed as 0.00</strong>
<ul><li>There was an  issue that caused package offer line prices not to display in the package offer card. This was fixed. </li></ul>
<strong>66067 LSC NA (CA) - French Translation to long for field length causing error when closing the day</strong>
<ul><li>Details not available.</li></ul>
<strong>66044 Cannot post sales invoice due to License permission error</strong>
<ul><li>Posting sales invoice issue was fixed due to missing permissions properties.</li></ul>
<strong>65982 Coupon management is coupon valid #485</strong>
<ul><li>New event <i>OnBeforeCheckCouponErrorOnIsCouponValid</i> added to "LSC Coupon Management" codeunit.</li></ul>
<strong>65922 There is an error when deleting device units</strong>
<ul><li>Code was updated that reads API response to match changes done by the API team.</li><li>#65928 was solved by adding missing field.</li><li>File was renamed to fix typo.</li></ul>
<strong>65910 Delete Preaction Preset Fix</strong>
<ul><li>Schedular job action <b>Preset Timestamp</b> was fixed to handle multiple old delete preactions.</li></ul>
<strong>65903 SAAS publishing new apps runs upgrade when it should not</strong>
<ul><li>Details not available.</li></ul>
<strong>65900 Add Function to custom panel in function PopUpInfocodePressed</strong>
<ul><li>Events added to codeunit Popup Controller, OnAfterGetPanelPayloadForShowingPanelModal, and to codeunit Pop-up POS Commands,  OnAfterPopupInfocodePressedGetPanelPayloadForShowingPanelModal, to be able to change the panel payload before showing the pop-up panel.</li></ul>
<strong>65883 Access to interface "LSC IFunctions" about all functions</strong>
<ul><li>Public access to functions <i>SetPosTransDiscEntryBuffer</i>, <i>InsertPosTransDiscEntryBuffer</i>, <i>GetMemberPointBalance</i> from "POS Functions" codeunit. </li><li>New procedures <i>PublicSetPosTransDiscEntryBuffer</i>, <i>PublicInsertPosTransDiscEntryBuffer</i>, and <i>PublicGetMemberPointBalance</i> created.</li><li><i>ClearPosTransDiscEntryBuffer</i> was already public.</li></ul>
<strong>65866 Event in codeunit 10000827 "LSC Send to KDS Interface" about function DeleteKots in codeunit 10001302 "LSC Hosp. Sts and KDS Cleanup"</strong>
<ul><li>Added events: OnAfterDeleteKots, OnBeforeKDSRecordsDeleteAll, OnBeforeRetNextKOTNo and OnBeforeGetOnHoldStatus</li></ul>
<strong>65865 Event in table LSC Hospitality Type at function OnValidate_OrderID</strong>
<ul><li>Details not available.</li></ul>
<strong>65844 Access to function TerminalStartupController in table 99001471 "LSC POS Terminal"</strong>
<ul><li>Access provided to procedure <i>TerminalStartupController</i> in table "LSC POS Terminal".</li></ul>
<strong>65842 Group comments are displayed on other unrelated bookings in the Matrix View</strong>
<ul><li>Fixed an issue which could cause comments to show on group reservations in the Matrix where no comments  were actually registered.</li></ul>
<strong>65837 Table Season - event to skip error in OnModify trigger</strong>
<ul><li>New event <i>OnBeforeModifySeason</i> added to "LSC Season" table.</li></ul>
<strong>65803 WebServiceConnectionFix</strong>
<ul><li>Handling of user name and encoding of secret-text (pwd) was fixed.</li></ul>
<strong>65799 OnBeforeShowMessage(Var "PrepaycustomerOrder": boolean,Var "Is handled": Boolean);</strong>
<ul><li>New event <i>OnBeforeShowMessageOnCheckIfUserWantsToAddExtraPaymentToCO</i> added to "LSC POS Transaction Impl" codeunit.</li></ul>
<strong>65775 POS GIFT_PRINT lookup error</strong>
<ul><li>Details not available.</li></ul>
<strong>65719 Add OnBeforeProcessDiscountPosting event to codeunit "LSC Statement-Post" #484</strong>
<ul><li>New parameters added to <i>OnBeforeUpdLedgerPostingBufferInPostItemSales</i>.</li></ul>
<strong>65706 Changing “No. of Persons” on Activity Group Line does not update the Reservation</strong>
<ul><li>
<p>Changed the approach when the user is changing either quantity or no. of persons on a group line.</p>
<p>Now when changing either quantity or no. of persons on a group reservation line, after the related activities have been created, the user gets a confirmation dialog window asking to delete the related activities (if they exist), if the no. of persons/qty is lower than previous value.  If the user approves the confirmation dialog,  then related activities is deleted and the group members associated with the group line is removed, and the quantity or number of persons change is assigned on the group line itself, and the reservation is drafted.  This because activities will be fewer than before.  <b>Note:</b> When lowering quantity you can always delete the member who is not attending which will only remove the related activity and skip the drafting process.</p>
<p>Previously, the user would get an error message stating that activities already existed, and would have to manually go and delete the activities (see action <b>Delete Activities</b> in the group line), or delete associated group member assignments to affect the quantity, which also still works as before.</p>
<p>This way users are prompted immediately, if they are OK with deleting the activities to continue the quantity/no. of persons changes.</p>
<p><b>Note:</b>  When increasing the value of Quantity/no. of persons, and confirmed activities exist,  the users are prompted if they want to draft the activities before the change is accepted, and then they must manually confirm again. Previously, users had to manually draft the line before changing these values.</p>
</li></ul>
<strong>65704 PreAuth information not copied correctly when doing Update PreAuth</strong>
<ul><li>When doing an update on an existing PreAuth line in the POS (<b>Update Preauth</b>operation) information about the original PreAuth line needs to be copied to the card entry information that is attached to the update preauth operation.</li><li>Some of the required information was not being copied to the update card line and this would mean that Finalize PreAuth operation would not work properly after doing an Update PreAuth. This was fixed.</li></ul>
<strong>65603 When picking and canceling CO lines at the same time, the collection does not return the cancel line amount</strong>
<ul><li>If Prepaid Items are canceled and/or shortaged when picking on POS, they are returned when the Customer Order is collected and finalized on POS.</li></ul>
<strong>65594 Upgrade Fix</strong>
<ul><li>Missing function call in LS Central Upgrade codeunit was fixed.</li></ul>
<strong>65593 Member Point Journal is in error</strong>
<ul><li>Details not available.</li></ul>
<strong>65583 Error while opening Store Card</strong>
<ul><li>Fixed Customer Order Setup error when opening the <b>Store Card</b>.</li></ul>
<strong>65580 Split item line does not check for old quantity handling of modifiers</strong>
<ul><li>Details not available.</li></ul>
<strong>65578 Extend event subscriber to allow better control over PostingBuffer #483</strong>
<ul><li>Event <i>OnBeforePostDiscountLedgerBuffering2</i> added to Statement-Post codeunit to replace <i>OnBeforePostDiscountLedgerBuffering</i>.</li></ul>
<strong>65562 The member attributes filter page, has different filters from previous versions</strong>
<ul><li>Details not available.</li></ul>
<strong>65560 Opening and closing the member account attributes page causes an error</strong>
<ul><li>Details not available.</li></ul>
<strong>65543 Deal pricing gives error if deal price lines are found for same price group in call</strong>
<ul><li>Details not available.</li></ul>
<strong>65536 Member Management: Member Attribute Values not assigned error</strong>
<ul><li>Details not available.</li></ul>
<strong>65512 Upgrade not correct for UpgradeStyleChitDisplay</strong>
<ul><li>UpgradeStyleChitDisplay is missing the ShouldUpgrade and  SetUpgradeTag</li><li>Also, no procedures should be below the helper region.</li></ul>
<strong>65502 Label printing stops using Device Dialog for Printing Labels</strong>
<ul><li>Details not available.</li></ul>
<strong>65466 BackgroundColor hex conversion not working properly on the service</strong>
<ul><li>Color code was fixed using BRG instead of RGB.</li></ul>
<strong>65456 Update Hotels to work with License Manager API v3</strong>
<ul><li>Hotel units (HPP) were updated to support License Manager API v3.</li><li>License validation and error handling was improved. </li></ul>
<strong>65455 Customer Order Shipping Order Posting License issue</strong>
<ul><li>Details not available.</li></ul>
<strong>65454 Update Bookings and Staff to work with License Manager API v3</strong>
<ul><li>Bookings and Staff management units (BPL and SME) were updated to support License Manager API v3.</li><li>License validation and error handling was improved. </li></ul>
<strong>65449 PASI - Wrong Inventory Assignment</strong>
<ul><li>Reserved inventory quantity only applied once in Total Inventory calculations for Item lookup for Items with tracking codes.</li></ul>
<strong>65380 Error when editing duration in the Matrix by clearing the Time To value and inserting a new value as Time From</strong>
<ul><li>Details not available.</li></ul>
<strong>65378 Upgrade error "UpgradeActivityReservationDiningReservCreated" on demo database</strong>
<ul><li>Details not available.</li></ul>
<strong>65353 Build Error Related to ticket 64983</strong>
<ul><li>Details not available.</li></ul>
<strong>65335 LM - /v3/license, Cancellation Status will change from description to code</strong>
<ul><li>Handle the type change of the field <b>cancelationStatus</b> on the response send by the API get License.</li></ul>
<strong>65288 Need a publisher in codeunit 10036988 "LSC BackOffice Ext."</strong>
<ul><li>New publisher event <i>OnBeforeGetCustomerOrders</i> in codeunit BackOffice Ext.</li></ul>
<strong>65255 Integration Events for Allocation Plans</strong>
<ul><li>The below integration events have been added to the following Allocation Plans related objects:<ul style="list-style-type: circle;"><li><p>Table LSC Alloc. Plan Lines</p><ul style="list-style-type: square;"><li>OnBeforeValidateQtytoDistribute</li><li>OnBeforeValidateAllocationRuleCode</li><li>OnBeforeValidateAllocationRuleCalcMethod</li></ul></li><li>Codeunit <b>LSC Alloc. Plan Utils Public</b><ul style="list-style-type: square;"><li>OnBeforeDistributeAllocPlanLine, which is used by the codeunit <b>LSC Alloc. Plan Utils</b>.</li></ul></li></ul></li><li><p>Table LSC Alloc. Plan Lines</p><ul style="list-style-type: square;"><li>OnBeforeValidateQtytoDistribute</li><li>OnBeforeValidateAllocationRuleCode</li><li>OnBeforeValidateAllocationRuleCalcMethod</li></ul></li><li>OnBeforeValidateQtytoDistribute</li><li>OnBeforeValidateAllocationRuleCode</li><li>OnBeforeValidateAllocationRuleCalcMethod</li><li>Codeunit <b>LSC Alloc. Plan Utils Public</b><ul style="list-style-type: square;"><li>OnBeforeDistributeAllocPlanLine, which is used by the codeunit <b>LSC Alloc. Plan Utils</b>.</li></ul></li><li>OnBeforeDistributeAllocPlanLine, which is used by the codeunit <b>LSC Alloc. Plan Utils</b>.</li></ul>
<strong>65207 #LOOKUP not working after an minor update</strong>
<ul><li>Fix for Lookup on POS not working.</li></ul>
<strong>65186 Make coupon functions accessible</strong>
<ul><li>Procedures <i>IsCouponValidForItemLine</i>, <i>ValidateCouponHeader</i>, and <i>ValidateCouponEntry</i> were made externally available through codeunit "LSC Coupon Management Public".</li></ul>
<strong>65184 OnBeforeLoadPanelDataOrLookup</strong>
<ul><li>New event <i>OnBeforeLoadPanelDataOrLookup</i> in codeunit "LSC POS Member Contact Popup".</li></ul>
<strong>65172 Make codeunit "LSC Schedule Batch Posting" accessible</strong>
<ul><li>Details not available.</li></ul>
<strong>65169 Add OnBeforePrintSuspendSlipItemLine event #482</strong>
<ul><li>New event <i>OnBeforePrintSuspendSlipItemLine</i> added to  "LSC POS Print Utility Impl" codeunit.ment-Post" codeunit.</li></ul>
<strong>65168 Added event OnBeforeCreateItemJnlLineDim to Statement-Post codeunit #481</strong>
<ul><li>New event <i>OnBeforeCreateItemJnlLineDim</i> added to "LSC Statement-Post" codeunit.</li></ul>
<strong>65158 Expose SetItem procedure in Dimension Matrix #480</strong>
<ul><li>A public procedure, <i>PublicSetItem</i>, has been added to the LSC <b>Dimension Matrix</b> page, which allows access to the internal procedure <i>SetItem</i>.</li></ul>
<strong>65139 Autotest app build failure on BC 26</strong>
<ul><li>Details not available.</li></ul>
<strong>65122 Realtime stock without Automatic Stock Update</strong>
<ul><li>Running WI Update Inventory now includes quantity sold not posted from POS transactions in Total inventory quantities.</li></ul>
<strong>65101 The Pop-up Group does not exist error when trying to change deals</strong>
<ul><li>Details not available.</li></ul>
<strong>65082 Build failure on release/release with BC 26</strong>
<ul><li>Details not available.</li></ul>
<strong>65046 Products having a default quantity conversion set other than None, always have 1.00 set as the duration during booking, no matter what is selected as default duration</strong>
<ul><li>Details not available.</li></ul>
<strong>65045 CO - Release - synchronize Customer Order Postings</strong>
<ul><li>Statement Postings for Customer Order was synced across versions.</li></ul>
<strong>65041 A logic check needs to be implemented on the product card so that Default Time From and Time to quantity automatically matches with default quantity</strong>
<ul><li>Details not available.</li></ul>
<strong>65017 Functional mistake in rounding for Foreign Currency</strong>
<ul><li>Fixed rounding issue when using currencies.</li></ul>
<strong>65015 Bookings - Empty additional charges for activity cause issue on POS</strong>
<ul><li>Fixed an error that occurred when paying an activity on the POS, which had activity additional charges with a blank product number, and the user either changed the price or discount during the POS payment process.</li></ul>
<strong>64983 NextInfoCode in codeunit 99008905 "LSC POS Infocode Utility" to be public</strong>
<ul><li>Procedure NextInfoCode made public.</li></ul>
<strong>64975 Event required in function TypeCreateDataEntry codeunit 99008905 "LSC POS Infocode Utility"</strong>
<ul><li>Added event <i>OnAfterTSDataEntries</i> in POS Infocode Utility.</li></ul>
<strong>64970 Deactivate all unprocessabe entries on codeunit 99009012 (UPGR/DOWNGR-MEMBER)</strong>
<ul><li>Details not available.</li></ul>
<strong>64967 Tender Declaration</strong>
<ul><li>Added event <i>OnBeforeTD_CommandPressedCallback</i> in "LSC Safe Denom. Panel Commands".</li></ul>
<strong>64958 Added OnBeforeExitOnCancelVoid to VOID #478</strong>
<ul><li>New event <i>OnBeforeExitOnCancelVoid</i> added to POS Transaction codeunit.</li></ul>
<strong>64951 Store Item Card - Vendor Item No. length issue</strong>
<ul><li>Increased variable length to match table field name in the <b>Store Item Card</b> page.</li></ul>
<strong>64934 Dragging and dropping appointments in the Matrix display can leave some cells having colored border</strong>
<ul><li>Details not available.</li></ul>
<strong>64873 CO - remove Co eCommerce Mgt codeunit - prepayment invoice change</strong>
<ul><li>Reduntant code was removed regarding Customer Order Payments in Ecommerce Mgt.</li></ul>
<strong>64866 Fix build error</strong>
<ul><li>Build error was fixed. </li></ul>
<strong>64834 Offers no. series mgt is wrong</strong>
<ul><li>Details not available.</li></ul>
<strong>64831 Need to move logic table pattern objects into new table folders</strong>
<ul><li>Details not available.</li></ul>
<strong>64816 EFT-printer shows error banner on POS</strong>
<ul><li>Details not available.</li></ul>
<strong>64740 Nested infocodes don't come up and have wrong qty handling</strong>
<ul><li>Details not available.</li></ul>
<strong>64739 Quantity of deals should stay not possible for standard popup</strong>
<ul><li>Details not available.</li></ul>
<strong>64706 Date To and Time To are not calculated correctly when creating a reservation in the past and the activity type allows multiple days</strong>
<ul><li>Details not available.</li></ul>
<strong>64696 NewEventRequest-GetDefaultCustomer #476</strong>
<ul><li>New publisher event <b>OnBeforeGetDefaultCustomer</b> was added in codeunit <b>POS Create New Customer.</b></li></ul>
<strong>64541 Adjustable data on Web Service #475</strong>
<ul><li>New publisher event <i>OnBeforeInsertCustomerTemp</i> in GetCustomerUtils codeunit.</li></ul>
<strong>64529 LT language - POS Warmup Active</strong>
<ul><li>Details not available.</li></ul>
<strong>64408 UploadPosPanelRowColumnsRec Inserts into wrong variable</strong>
<ul><li>Details not available.</li></ul>
<strong>64406 Hotfix lsts-37289</strong>
<ul><li>New version of event <i>OnAfterSelectCustomer</i> created, named OnAfterSelectCustomerV2.</li></ul>
<strong>64405 CO Reservation entries</strong>
<ul><li>Details not available.</li></ul>
<strong>64371 End of Day</strong>
<ul><li>New event <i>OnBeforeSetMoveMenuLine</i> in LSC Safe Management Public codeunit.</li></ul>
<strong>64235 GS1 Barcode with Qty and leading zero stopped working</strong>
<ul><li>Avoid removing leading zeros when processing a barcode, if the zero is a part barcodes prefix.</li></ul>
<strong>64187 Error prompt out in POS when user tried to add info code lines</strong>
<ul><li>Details not available.</li></ul>
<strong>64141 Retail receiving Quantity incorrectly in Transfer In</strong>
<ul><li>Information about Total Quantity and Quantity Left have been fixed in the Mobile Inventory App. Retail receiving Quantity has also been fixed in "Transfer In" in Backoffice and in web request for Mobile App.</li></ul>
<strong>64138 Local procedure SaveCustomerInfo_SkipModify()</strong>
<ul><li>New parameter added to event <i>SaveCustomerInfo_OnBeforeModify</i> from "LSC POS Create New Customer" codeunit.</li></ul>
<strong>64103 POS Negative Adjustment Transaction is not reflected in the store stock before EoD</strong>
<ul><li>New event <i>OnAfterQtySoldNotPostedCalculate</i> in <i>BO Utils</i> codeunit to enable partner to add their own logic to availability calculation.</li></ul>
<strong>64019 LSC Spanish Translation</strong>
<ul><li>Details not available.</li></ul>
<strong>63676 LM - Activate units - response successful and failed</strong>
<ul><li>The code was refactored to be able to handle v3 of the activation/unit and deactivation/unit endpoints be able to handle the JSON response where some units failed to be activated.</li></ul>
<strong>63675 /v3/unit/cancelation-status-update  change to /v3/unit/cancelation_status_update</strong>
<ul><li>API call was updated to use the new endpoint.</li><li>Cancelation code is now used instead of description #6367</li><li>New field was added to the Activate endpoint #63673</li></ul>
<strong>63231 Prevent user from being able to move an activity in the Matrix to a different time which configured to be not allowed</strong>
<ul><li>Details not available.</li></ul>
<strong>62369 Giftcard number gets picked up as another barcode mask</strong>
<ul><li>Prevents inserting non-numeric characters into a No. Series that is used to create barcode masks.</li></ul>
<strong>61012 "Min/Max. Amount Allowed" in Tender Type Card after voiding line is still prompted that max has been reached</strong>
<ul><li>Bugfix, <i>Max Amount Allowed</i> for tender type calculation included voided Trans Payment Lines.</li></ul>
<strong>60929 Number of attached documents to a Reservation Card in bookings not updated correctly</strong>
<ul><li>Added the new Document Attachments FactBox to the following pages:<ul><li>Staff Employee List/Card</li><li>Staff Roster List</li><li>Activity Reservation List/Card</li><li>Activity Group List/Card</li><li>Activity List/Card</li><li>Events List/Card</li></ul></li><li>Staff Employee List/Card</li><li>Staff Roster List</li><li>Activity Reservation List/Card</li><li>Activity Group List/Card</li><li>Activity List/Card</li><li>Events List/Card</li></ul>
<strong>59539 Cash Declaration Entry created when when no cash is declared</strong>
<ul><li>Details not available.</li></ul>
<strong>59517 Aggregated Inventory goes SaaS</strong>
<ul><li>Details not available.</li></ul>
<strong>58573 Retail Item Card validate Vendor No.</strong>
<ul><li>Validate Vendor No. in the <b>Retail Item Card</b> now updates Item Distribution entry.</li></ul>
<strong>58222 Cannot see the customer order on the POS when warehouse shipment is used to ship the transfer order</strong>
<ul><li>Fix for Customer Order Transfer Orders not showing up in the POS after shipping from warehouse when <b>Compressed Lines Active</b> is turned off after upgrade.</li></ul>
<strong>56190 Cannot copy base webtemplate code from field</strong>
<ul><li>Improvements were done on the POS Web Template page. Now it is possible to copy code in the code editor for base template.</li><li>The option to download the entire template's source code as a ZIP file was also added.</li></ul>
<strong>54846 Manage Tokens</strong>
<ul><li>It was made possible to enable and disable Member Tokens through page action.</li></ul>
<strong>50787 Adjust RBO cost price</strong>
<ul><li>Details not available.</li></ul>
<strong>50595 Validation Period for Offers: The offer is valid from Start Date and Start Time and will end on a End Date and End Time</strong>
<ul><li>New functionality on Periodic offers to allow offers that are not happy-hour using start and end time. New fields added, <b>Offer Starting Time</b> and <b>Offer Ending Time</b>.</li></ul>
<strong>40208 Return (Refund) Qty in correct</strong>
<ul><li>Details not available.</li></ul>
