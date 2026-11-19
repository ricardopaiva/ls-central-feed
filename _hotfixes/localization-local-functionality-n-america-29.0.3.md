---
title: "Localization hotfixes - 29.0.3 Local Functionality N-America, Release date November 18, 2026 - Hotfixes"
product: Localization
version: "29.0.3"
subproduct: Local Functionality N-America
minor_version: "29.0"
date: 2026-11-18 00:00:00+00:00
order: 19
guid: e9bd78d01aaad2e9f28557a95965c6383b692b04
---

<strong>91794 Update EBT Commands to Use Tender Type</strong>
<ul><li>Select a tender type when you set up an EBT balance inquiry command on a POS menu line, instead of typing it.</li><li>This applies to both the balance inquiry and the balance inquiry with dialog commands, and it makes setup less error-prone.</li></ul>
<strong>91787 EBT - Virtual Station</strong>
<ul><li>EBT payments at the POS now handle tax and balances correctly. EBT Card lines are tax exempt and EBT Cash lines aren't. When a customer pays part of a transaction with EBT, tax is split proportionally. The balance check now works per tender type, and receipts print "EBT Balance" for EBT Card payments and "EBT Cash Balance" for EBT Cash payments. EBT balance inquiries now run through the EFT Extension for LS Pay.</li><li><b>Action required by partners:</b></li><li>  ◦ Install EFT Extension for LS Pay 1.3.2.0 or later, and make sure the POS hardware profile has an EFT device.</li><li>  ◦ Set <b>Tax Group Code (Limitation)</b> on the store card to a tax group with no sales tax, such as NONTAXABLE.</li><li>  ◦ After you change a limitation, reselect its code on the tender type so the store limitation lines are rebuilt.</li><li>  ◦ To use the numpad with the combined balance and tender button, turn on <b>Use Numpad</b> on the POS terminal and <b>Numeric Keypad on Tender</b> in the functionality profile.</li></ul>
<strong>87986 Tax not calculated on Customer Orders when Tax Area Code arrives pre-populated via web service</strong>
<ul><li>Customer orders created through the web service now calculate sales tax correctly, even when the incoming request already includes a tax area code.</li><li>Previously, if an external system supplied the tax area code without also resolving tax liability, the resulting sales order posted with no sales tax at all.</li></ul>
<strong>86686 Shopify BC connector for LS Central - Tax Sync Issues in NA Shopify Store</strong>
<ul><li>Customer orders from Shopify and the POS now calculate sales tax and discounts correctly. Discounted lines no longer show an inflated discount percentage, so a 5% discount no longer appears as 5.26316%.</li><li>Tax is now worked out from the amount the customer actually pays, and shipping lines get their tax group.</li></ul>
