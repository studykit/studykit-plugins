# AssemblyEvents.OnAssemblyChange Event

Parent Object: [AssemblyEvents](../AssemblyEvents/AssemblyEvents.md)

## Description

Event that is fired after any change occurs that impacts the assembly structure.

## Syntax

AssemblyEvents.**OnAssemblyChange**( ***DocumentObject*** As [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md) | Input AssemblyDocument object that indicates the document in which the change occurred. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the assembly is changed. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |