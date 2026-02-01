# StyleEvents.OnDelete Event

Parent Object: [StyleEvents](../StyleEvents/StyleEvents.md)

## Description

Event that is fired whenever an object within this events set is deleted in a document.

## Remarks

Style Events are currently under development and are not supported. They are provided as-is and may be used at your own risk.

## Syntax

StyleEvents.**OnDelete**( ***DocumentObject*** As [Document](../Document/Document.md), ***Style*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input Document object that indicates the document in which the change occurred. |
| Style | Object | Object that was just deleted. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the entity is deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11
