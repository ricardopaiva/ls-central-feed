---
title: "LS Central hotfixes - 28.2.8 Release date September 8, 2026 - Hotfixes"
product: LS Central
version: "28.2.8"
subproduct: 
minor_version: "28.2"
date: 2026-09-08 00:00:00+00:00
order: 4
guid: 8258234cc3aa06c72a438f683812df7e76b4b5c3
---

<strong>87089 Need ability to Skip IsBlockPurchaseCreate in Store Inventory Journal</strong>
<ul><li>New Event, OnBeforeCheckBlockPurchaseCreate added in Store Inventory Line table in <b>Item No.</b> OnValidate.</li><li><b>Note:</b> In hotfix/latest (28.2) the ItemStatusLink parameter is a <b>Item Status Link</b> record. In develop this parameter is a <b>Item Status Link 2</b> record and the <b>Item Status Link</b> table was obsoleted.</li></ul>
<strong>87080 LSC Retail PO Subpage (10000816) not working correctly if Item variant is connecting to item in Purchase Order</strong>
<ul><li>Hook into the Variant Framework purchase order flow from your own extension. Four new publisher events let you act when LS Central creates a variant purchase line, converts a document line into a variant collection header, or validates a quantity on the Retail PO Subpage — without modifying LS Central code.</li><li>The events cover both purchase and sales documents:<ul><li><b>OnBeforeInsertPurchLine</b> — fires before the Variant Framework inserts a new purchase line for a variant.</li><li><b>OnBeforeConvertSalesLineToCollectionHeader</b> and <b>OnBeforeConvertPurchLineToCollectionHeader</b> — fire before a document line is converted into a variant collection header. Set IsHandled to replace that step with your own.</li><li><b>OnBeforeValidateQty</b> — fires before the quantity is validated on the Retail PO Subpage, so you can set a quantity without running validation.</li></ul></li><li><b>Action required by partners:</b>
<ul>
<li>None. Behavior is unchanged unless you subscribe to one of the events.</li>
</ul>
</li><li>If you subscribe to either collection-header event and set IsHandled, your code takes over converting the line into a collection header — zeroing the quantity, clearing the type and number, and storing the collection item number. Skip that step and LS Central adds variant lines beside a line that's still a normal item line, so the quantity is counted twice on the document.</li></ul>
<strong>86833 SAS Token generation issue in Sending Transaction using Storage Queue</strong>
<ul><li>Expiration of SAS access tokens was fixed.</li></ul>
