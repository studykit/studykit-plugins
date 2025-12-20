# BrowserPanesEvents.OnBrowserNodeLabelEdit Event

Parent Object: [BrowserPanesEvents](../BrowserPanesEvents/BrowserPanesEvents.md)

## Description

Event that is fired whenever a node is renamed by the user.

## Syntax

BrowserPanesEvents.**OnBrowserNodeLabelEdit**( ***BrowserNodeDefinition*** As Object, ***NewLabel*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BrowserNodeDefinition | Object | The ClientBrowserNodeDefinition associated with the node being edited. It’s the Label property of this object that will be affected by an edit. |
| NewLabel | String | When BeforeOrAfter is kBefore this is the current label of the node. When BeforeOrAFter is kAfter this is the new label of the node. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Notification is sent before and after the label edit occurs. When the BeforeOrAfter argument is kBefore you can set the HandlingCode argument to kEventCanceled to abort the edit and prohibit the end-user from editing the label. Any other value for this argument will allow the end-user to edit the label.  If the HandlingCode is set to kEventCanceled, this notification is only sent before. For the other cases this notification is also sent after the edit is finished. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | When the BeforeOrAfter argument is kBefore you can set the HandlingCode argument to kEventCanceled to abort the edit and prohibit the end-user from editing the label. Any other value for this argument will allow the end-user to edit the label. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |