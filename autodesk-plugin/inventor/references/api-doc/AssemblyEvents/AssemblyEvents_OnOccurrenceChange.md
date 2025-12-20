# AssemblyEvents.OnOccurrenceChange Event

Parent Object: [AssemblyEvents](../AssemblyEvents/AssemblyEvents.md)

## Description

Event that is fired whenever an occurrence changes.

## Remarks

The changes reported by this event are if any of the following states of an occurrence change: grounded, adaptive, visible, enabled, suppressed, and repositioned (transformed). The type of change and information related to the change is passed through the context argument.

## Syntax

AssemblyEvents.**OnOccurrenceChange**( ***DocumentObject*** As [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md), ***Occurrence*** As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md) | Input AssemblyDocument object that indicates the document in which the change occurred. |
| Occurrence | [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) | Input ComponentOccurrence object that indicates the occurrence that changed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the occurrence is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Information describing the change is passed through the context argument, as described below: Name = "Grounded", Value = True or False. Indicates the grounded state is changing. The value indicates the new grounded state of the occurrence. Name = "Adaptive", Value = True or False. Indicates the adaptive state is changing. The value indicates the new adaptive state of the occurrence. Name = "Visible", Value = True or False. Indicates the visibility state is changing. The value indicates the new visibility state of the occurrence. Name = "Enabled", Value = True or False. Indicates the enabled state is changing. The value indicates the new enabled state of the occurrence. Name = "Suppressed", Value = True or False. Indicates the suppressed state is changing. The value indicates the new suppressed state of the occurrence. Name = "Transformation", Value = Matrix object. Indicates the occurrence is being transformed. The Matrix object provided specifies the new transformation of the occurrence. If the original transformation is needed, you can obtain it using the Transformation property of the ComponentOccurrence object provided by the Occurrence argument of this event when the timing is kBefore. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |