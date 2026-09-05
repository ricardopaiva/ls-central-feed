---
title: "Autotests hotfixes - 28.2.4 Autotests, Release date August 25, 2026 - Hotfixes"
product: Autotests
version: "28.2.4"
subproduct: Autotests
minor_version: "28.2"
date: 2026-08-25 00:00:00+00:00
order: 7
guid: c90a5f361e15b28435de22c669ed6f9e3ad26daf
---

<strong>86952 Add OnClassifyDealLineForPriceReduction event to LSC Deal Pricing Functions</strong>
<ul><li>Adds a new integration event, <b>OnClassifyDealLineForPriceReduction</b>, to codeunit <b>LSC Deal Pricing Functions</b>.</li><li>It is raised once per deal child line during deal registration, letting partners classify a line for potential exclusion from proportional deal-price reduction in a future release.</li><li>No behavior changes in this release - existing deal pricing is unaffected.</li><li><b>Action required by partners:</b> None.</li></ul>
<strong>86874 Membership upgrade/downgrade batch job upgrades members with zero points</strong>
<ul><li>Membership upgrades and downgrades now count only the award points a member earns within the tier calculation period. Points earned outside that period — including points that have expired — no longer push a member into a higher tier.</li><li>Date range filters on member statistics work correctly too, so point totals match the range you set.</li><li><b>Action required by partners</b>:<ul><li>None. Run the Upgrade/Downgrade batch job (or wait for the scheduled run) to re-evaluate members on the corrected logic.</li></ul></li></ul>
<strong>86612 Signature invalid" error on offline POS (v27) after Central upgrade to 28.2.1.3960</strong>
<ul><li>This is a temporary fix.</li></ul>
<strong>86571 KDS crashes when KOT tickets are voided before Web KDS picks them up</strong>
<ul><li>Web KDS order routing is now atomic and crash-resistant.</li><li>Web KDS integration now reliably routes orders to the kitchen without sending duplicate kitchen tickets, even when order submissions overlap during high-volume service.</li><li>Business Central claims each ticket atomically before sending it to Web KDS - if overlapping order events occur at the same time, only one push can claim a given ticket.</li><li>If any ticket fails to send, it is automatically resubmitted on the next push attempt, so no order silently gets lost.</li><li><b>Why it matters:</b> <ul><li>A race condition in the previous push mechanism could send the same kitchen ticket multiple times when concurrent order operations happened at the same store. If the Web KDS endpoint received a duplicate ticket, it would reject the entire batch and crash the kitchen display, requiring manual database recovery. High-volume restaurants were affected most severely.</li></ul></li><li>This fix closes the concurrency window entirely.</li><li><b>Action required by partners:</b>
<ul>
<li> None. This fix is applied automatically on upgrade and requires no configuration or setup. No schema/data changes and no breaking changes.</li>
</ul>
</li></ul>
<strong>86481 Unable to Apply Store Coupon at POS When Zero-Price Item Exists in Transaction</strong>
<ul><li>Tapping Total, rejected the coupon with <b>Entered Coupons but not used</b> and the customer paid full price.</li><li>Coupons with Handling set to Tender, now apply when the transaction includes a line with a zero-price item.</li></ul>
<strong>85193 Member account downgraded with sufficient point balance</strong>
<ul><li>Members are no longer moved to a lower scheme by the upgrade/downgrade job when their points still meet the downgrade limit. The member's scheme now stays unchanged.</li></ul>
