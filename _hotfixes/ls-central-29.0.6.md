---
title: "LS Central hotfixes - 29.0.6, Release date November 12, 2026 - Hotfixes"
product: LS Central
version: "29.0.6"
subproduct: 
minor_version: "29.0"
date: 2026-11-12 00:00:00+00:00
order: 4
guid: 34622f993cee788951b92fef4447e056857eabbc
---

<strong>91877 Add OnBeforeDisplayMessageIfNoFilters event</strong>
<ul><li>New event <b>OnBeforeDisplayMessageIfNoFilters</b> was added to <b>LSC POS Member Contact Popup</b> codeunit.</li></ul>
<strong>91876 Some Extra OnBeforeSendLocalRequest events for web services v2</strong>
<ul><li>Multiple events were added.</li></ul>
<strong>91592 Web Templates not exporting with its Group</strong>
<ul><li>Details not available.</li></ul>
<strong>91532 AttribUtilFindItemByAttrOnAfterSetrange(AttributeValue)</strong>
<ul><li>Filtering items by two or more attributes of different types (numeric, date or text) now returns the items that match all selected filters. Previously, filters from the first attribute carried over to the next one, so combining attributes of different types could return no items or the wrong items.</li><li>  ◦ This applies to the item attribute filter in the <b>Retail Item List</b>, <b>Hospitality Item List</b> and <b>Item Distribution Lists</b>.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>91526 OnHandleNewMemberCardOnBeforeInsertFilters(FieldIndexList,FieldIndexValues)</strong>
<ul><li>Add custom filters when looking up new member cards at the POS. A new event lets extensions adjust the lookup filters before the member card list is shown.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>91439 New event for TSInUse function in the ""LSC POS Trans. Server Utility"</strong>
<ul><li>The <b>OnBeforeTSInUse</b> event was added to the <b>POS Trans. Server Utility codeunit</b>.</li><li>It lets extensions mark the Transaction Server as in use, so you can use your own web services without enabling standard LS web services in the functionality profile.</li></ul>
<strong>91374 Price Change Not considering the adidas customization due to abs(value) introduction in LS Base</strong>
<ul><li>New parameters were added to the discount permission events in POS Session:</li><li>  ◦ OnBeforePermissionItemDISC: Value, PermissionGroupRec, ManagerPermRec, KeyLockPermRec</li><li>  ◦ OnBeforePermissionItemTDISC: Value, PermissionGroupRec.</li></ul>
<strong>91024 New extension events request in LS Central 25.3</strong>
<ul><li>DD transaction send events and GetPkgGuid were added:</li><li>  ◦ LSC POS Trans. Server Utility: OnAfterSendTransactionDDRequestPrep and OnAfterSendTransactionRequestSenttoDD in SendWholeTmpTransaction (DD branch)</li><li>  ◦ LSC Data Dir. POS Client Util: public GetPkgGuid().</li></ul>
<strong>88175 Bug Report: Statement-Post fails on return with "You cannot return more than the X units..." when the same item appears twice on the original receipt</strong>
<ul><li>Refunding a receipt where the same item was rung up twice, at different quantities, no longer blocks the whole day's statement. Refunds like this used to fail with an error naming the wrong shipped quantity – now the return posts correctly, even when we cannot pin it to one exact original sale line.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>87593 Bug: RetSuspendedPressedEx – no commit before OnAfterRetSuspendedV2 → silent empty postings</strong>
<ul><li>Retrieving a suspended transaction in the POS is now more reliable. If something fails while the transaction is being retrieved, the POS no longer lets you carry on with a sale that cannot be saved. It tells you the retrieve did not complete, and the suspended transaction stays available to retrieve again.</li><li>Before, a failure at that point could leave a signed receipt with no items and no payments, even though the customer had paid.</li><li><b>Action required by partners:</b></li><li>  ◦ None. If you have extended the retrieve flow with your own code, it now runs after the retrieved transaction is saved.</li></ul>
<strong>87052 Transaction No. of "CARD" Printing not set correctly</strong>
<ul><li>Details not available.</li></ul>
