# BrowserPanesEvents.OnBrowserNodeDeleteEntry Event

Parent Object: [BrowserPanesEvents](../BrowserPanesEvents/BrowserPanesEvents.md)

## Description

Event that is fired whenever the user requests that a node be deleted.

## Syntax

BrowserPanesEvents.**OnBrowserNodeDeleteEntry**( ***BrowserNodeDefinition*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BrowserNodeDefinition | Object | The ClientBrowserNodeDefinition associated with the node the end-user has right-clicked on. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | When this value is kBefore you are able to control whether the Delete command is available in the context menu or not by setting the appropriate handling code. When this value is kAfter it signals that the end-user has requested that this node and associated objects be deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | When the BeforeOrAfter argument is kBefore you can set the HandlingCode argument to kEventCanceled to disable the Delete command from being displayed in the context menu. Any other value for this argument will allow Delete command to be displayed. This argument has no meaning when the BeforeOrAfter argument is kAfter. |

## Version

Introduced in version 10
