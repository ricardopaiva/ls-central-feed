---
title: "Autotests hotfixes - 29.0.5 Autotests, Release date November 12, 2026 - Hotfixes"
product: Autotests
version: "29.0.5"
subproduct: Autotests
minor_version: "29.0"
date: 2026-11-12 00:00:00+00:00
order: 10
guid: 77a6eda6a8aba1b8c8d6019611a3cf8f61c409ce
---

<strong>88175 Bug Report: Statement-Post fails on return with "You cannot return more than the X units..." when the same item appears twice on the original receipt</strong>
<ul><li>Refunding a receipt where the same item was rung up twice, at different quantities, no longer blocks the whole day's statement. Refunds like this used to fail with an error naming the wrong shipped quantity – now the return posts correctly, even when we cannot pin it to one exact original sale line.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
