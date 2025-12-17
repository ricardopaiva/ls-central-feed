---
title: "System hotfixes - 27.0.4 System App, Release date December 4, 2025 - Hotfixes"
product: System
version: "27.0.4"
subproduct: System App
minor_version: "27.0"
date: 2025-12-04 00:00:00+00:00
order: 67
guid: d03e0e5e1a4a88037712dea7b406ad2d70fb9401
---

<strong>75179 Do not set the focus to OK in a message</strong>
<ul><li>Custom panels were changed so that they require manually setting focus to them by default.</li><li>For example if you want to use the ENTER key to select an option in a message/error dialog, you first need to put a focus on the dialog (with the tab key or the arrow keys). </li><li><b>Note:</b> that you can always close dialogs with the ESC key.</li><li>To opt-out of this behavior, you can set the URL parameter <b>ls-_shouldentercloseerrors=1</b> (temporarily available).</li></ul>
