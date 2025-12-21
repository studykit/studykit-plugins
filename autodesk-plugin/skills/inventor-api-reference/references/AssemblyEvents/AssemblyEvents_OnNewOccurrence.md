# AssemblyEvents.OnNewOccurrence Event

Parent Object: [AssemblyEvents](../AssemblyEvents/AssemblyEvents.md)

## Description

Event that is fired whenever an occurrence is created.

## Syntax

AssemblyEvents.**OnNewOccurrence**( ***DocumentObject*** As [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md), ***Occurrence*** As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md) | Input AssemblyDocument object that indicates the document in which the change occurred. |
| Occurrence | [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) | Input ComponentOccurrence object that was just created. Nothing in the kBefore case. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the occurrence is created. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11
