# BrowserPanesEvents.OnBrowserNodesReorder Event

Parent Object: [BrowserPanesEvents](../BrowserPanesEvents/BrowserPanesEvents.md)

## Description

Event that fires just before and after browser nodes are reordered.

## Syntax

BrowserPanesEvents.**OnBrowserNodesReorder**( ***BrowserPane*** As [BrowserPane](../BrowserPane/BrowserPane.md), ***DragNodes*** As [BrowserNodesEnumerator](../BrowserNodesEnumerator/BrowserNodesEnumerator.md), ***TargetNode*** As [BrowserNode](../BrowserNode/BrowserNode.md), ***eInsertionLoactionType*** As [InsertionLocationTypeEnum](../InsertionLocationTypeEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BrowserPane | [BrowserPane](../BrowserPane/BrowserPane.md) | Input BrowserPane object indicating which browser pane has its browser nodes reordered. |
| DragNodes | [BrowserNodesEnumerator](../BrowserNodesEnumerator/BrowserNodesEnumerator.md) | Input the BrowserNodesEnumerator that contains the browser nodes being moved. |
| TargetNode | [BrowserNode](../BrowserNode/BrowserNode.md) | Input the BrowserNode to position the DragNodes next to or under. |
| eInsertionLoactionType | [InsertionLocationTypeEnum](../InsertionLocationTypeEnum.md) | Input the InsertionLocationTypeEnum indicating where to position the DragNodes. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the browser nodes are reordered. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2018
