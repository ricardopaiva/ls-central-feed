---
title: "LS Central hotfixes - 28.0.16, Release date May 26, 2026 - Hotfixes"
product: LS Central
version: "28.0.16"
subproduct: 
minor_version: "28.0"
date: 2026-05-26 00:00:00+00:00
order: 5
guid: 5355ddcfb186d1a823a21bd7003b42ade728a35f
---

<strong>82612 EFT ManualEntry is missing MOTO TenderType</strong>
<ul><li>Details not available.</li></ul>
<strong>82603 Activity type lookup filtering and validation on Activity Reservation</strong>
<ul><li>There was an issue with how activity type product restrictions where not enforced when activity type or activity products were assigned (manually or via lookup of activity type) on the activity reservation entry. This was fixed. </li></ul>
<strong>82498 Store Inventory Worksheet Journal Lines Disapearing/Deleting</strong>
<ul><li>There was an issue where Store Inventory Worksheet journal lines were being deleted unexpectedly, caused by unintended bulk deletions triggered during normal user activity.</li></ul>
<strong>82313 AL: Shopify inventory not replicating to Shopify Site</strong>
<ul><li>Inventory communication with Shopify was updated to API Version 2026-04.</li></ul>
<strong>82146 Trans. Inc/Exp Missing Option</strong>
<ul><li>Details not available.</li></ul>
<strong>82086 Check Endorsement – wrong design string used in the Print Utility</strong>
<ul><li>Details not available.</li></ul>
<strong>81883 LM test units are not synced</strong>
<ul><li>The auth token was reset after the environment was updated.</li></ul>
<strong>81549 Error in Leaver Update IGA|User leaving the company</strong>
<ul><li>There was an error, that was fixed. <b>The length of the string is X, but it must be less than or equal to 100 characters</b> that occurred when removing a user from a user group (leaver process) if the Access Control record's converted key exceeded 100 characters.</li><li>The delete-action cleanup in <b>LSC Actions Management</b> now safely skips the Distribution List filter when the converted key would exceed the Value field length.</li></ul>
<strong>81152 LSCentral Events</strong>
<ul><li>Events that were created:</li><li>
<table cellspacing="0" class="TableStyle-Rows" style="width: 100%;mc-table-style: url('../Resources/Table Styles/Rows.css');">
<col class="Column-Column1"/>
<col class="Column-Column1"/>
<tbody>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1"><b>Event</b>
</td>
<td class="BodyD-Column1-Body1">
<p><![CDATA[ ]]><b>Codeunit</b></p>
</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnAfterMultiplyWith_OnTotalPressed</td>
<td class="BodyD-Column1-Body2">
<p>POS Transaction Events (99001574)</p>
</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnAfterProcessLinePreTotal_OnLineDiscOffer	</td>
<td class="BodyD-Column1-Body1">POS Transaction Events (99001574)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnAfterSetCurrInput_OnProcessMSRInput</td>
<td class="BodyD-Column1-Body2">POS Transaction Events (99001574)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnBeforeProcessCouponV3</td>
<td class="BodyD-Column1-Body1">POS Transaction Events (99001574)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnAfterInsertNewPOSTransLine_OnCopyMarkedLines</td>
<td class="BodyD-Column1-Body2">POS Functions (99008900)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnAfterSetFilters_OnGetPrice</td>
<td class="BodyD-Column1-Body1">POS Price Utility (99008906)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnAfterSetFilters_OnCalcPeriodicOnTotalPressed</td>
<td class="BodyD-Column1-Body2">POS Price Utility (99008906)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnAfterRoundPrice_OnGetPrice</td>
<td class="BodyD-Column1-Body1">POS Price Utility (99008906)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnBeforeAssignTenderDeclEntry_OnInsertTenderDeclTransaction</td>
<td class="BodyD-Column1-Body2">POS Post Utility (99008902)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnBeforeInsertCouponTransaction</td>
<td class="BodyD-Column1-Body1">POS Post Utility (99008902)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnBeforeApplyCouponEntry_OnWriteTransactionToDatabase</td>
<td class="BodyD-Column1-Body2">POS Post Utility (99008902)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnBeforeGetActivePriceGroup_OnUpdateMemberFromPOS</td>
<td class="BodyD-Column1-Body1">POSCalcMemberPointsPublic (10000806)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnBeforeModifyPosCashDecl_OnClearForm</td>
<td class="BodyD-Column1-Body2">Safe Denom. Panel Commands (99001595)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnAfterCaseExpression_OnUpdateCashDecl</td>
<td class="BodyD-Column1-Body1">Tender Declaration (99001577)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnBeforePOSSafeLineTmpInsert_OnTmpSafeTransaction</td>
<td class="BodyD-Column1-Body2">Tender Declaration (99001577)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnBeforeProcessCurrColumn_OnCountedPressed</td>
<td class="BodyD-Column1-Body1">Tender Declaration (99001577)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnBeforeProcessCurrColumn_OnBagNoPressed</td>
<td class="BodyD-Column1-Body2">Tender Declaration (99001577)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnBeforeApplyCouponsToTransaction</td>
<td class="BodyD-Column1-Body1">Coupon Management (99001480)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyE-Column1-Body2">OnBeforeCreateCouponBarcode</td>
<td class="BodyD-Column1-Body2">Coupon Management (99001480)</td>
</tr>
<tr class="Body-Body1">
<td class="BodyE-Column1-Body1">OnBeforeIssueCoupon</td>
<td class="BodyD-Column1-Body1">Coupon Management (99001480)</td>
</tr>
<tr class="Body-Body2">
<td class="BodyB-Column1-Body2">OnBeforeReturnCouponHeader</td>
<td class="BodyA-Column1-Body2">Coupon Management (99001480)</td>
</tr>
</tbody>
</table>
</li><li>Signature Changes:<ul><li>OnAfterCommitPaymentLine (POS Transactions Events)<ul><li>new params var CardEntry: Record "LSC POS Card Entry"; var NewLine: Record "LSC POS Trans. Line"</li><li>OnBeforeRunCodeunit (Statement-Calculate): new param var Handled: Boolean</li></ul></li></ul></li><li>Skipped / Deferred:<ul><li>ApplyFilterforPOSTransLine (POS Refund Mgt.)<ul><li>Skipped, deleted in develop</li></ul></li><li>Retail User "E-mail Address" Text[30]-&gt;Text[250]<ul><li>Deferred, separate change</li></ul></li><li>POS DataSet Utility event<ul><li>Owned by another team</li></ul></li><li>Hospitality (9 files) and Replenishment (2 files)<ul><li>Other teams</li></ul></li></ul></li></ul>
<strong>80455 OrderHospCreate - CurrentAvailability still deducted when orders is not going through</strong>
<ul><li>If a request from ECom fails, it does not decrease the number of Current availability.</li></ul>
