# AssemblyEvents.OnLoadStateChange Event

Parent Object: [AssemblyEvents](../AssemblyEvents/AssemblyEvents.md)

## Description

Fires when an assembly document goes from lite to full or full to lite loading.

## Syntax

AssemblyEvents.**OnLoadStateChange**( ***DocumentObject*** As [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md), ***NewLoadState*** As [DocumentLoadStateEnum](../DocumentLoadStateEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md) | The AssemblyDocument object whose load state is changing. When the state is changing from Lite to Full the document object returned will be the same for both the before and after firings of this event. When going from Full to Lite, the document object will be difference since the document is actually closed and reopened. |
| NewLoadState | [DocumentLoadStateEnum](../DocumentLoadStateEnum.md) | Input DocumentLoadStateEnum value indicating the state the document is changing to when the timing kBefore and the current state when the timing is kAfter. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the load state has changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is currently provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. By setting this argument to kEventCanceled when the BeforeOrAfter argument is kBefore, Inventor will abort the state change. When the save is cancelled, this event is fired again but the BeforeOrAfter argument will have a value of kAbort. |

## Version

Introduced in version 2014
