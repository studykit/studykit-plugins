# BrowserPanesEvents.OnBrowserNodeGetDisplayObjects Event

Parent Object: [BrowserPanesEvents](../BrowserPanesEvents/BrowserPanesEvents.md)

## Description

Event that is fired when a user requests that the objects represented by a browser node be highlighted.

## Syntax

BrowserPanesEvents.**OnBrowserNodeGetDisplayObjects**( ***BrowserNodeDefinition*** As Object, ***Objects*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BrowserNodeDefinition | Object | The ClientBrowserNodeDefinition associated with the node the mouse is over. |
| Objects | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | An Object collection that the client must create and populate with the objects associated with the browser node. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | This event provides additional information through the Context argument as described below: Name = “Browser Node”, Value = The BrowserNode object that the mouse is over. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | This argument is ignored for this event. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |