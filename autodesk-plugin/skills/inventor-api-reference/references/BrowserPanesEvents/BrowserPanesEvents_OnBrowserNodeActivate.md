# BrowserPanesEvents.OnBrowserNodeActivate Event

Parent Object: [BrowserPanesEvents](../BrowserPanesEvents/BrowserPanesEvents.md)

## Description

Event that is fired whenever a node is activated by the user.

## Syntax

BrowserPanesEvents.**OnBrowserNodeActivate**( ***BrowserNodeDefinition*** As Object, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BrowserNodeDefinition | Object | The ClientBrowserNodeDefinition associated with the node just activated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | This event provides additional information through the Context argument as described below: Name = “Browser Node”, Value = The BrowserNode object that the end-user double-clicked on. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | This argument is ignored for this event. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |