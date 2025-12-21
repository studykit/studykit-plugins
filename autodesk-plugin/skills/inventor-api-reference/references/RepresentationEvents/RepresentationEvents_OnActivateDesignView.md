# RepresentationEvents.OnActivateDesignView Event

Parent Object: [RepresentationEvents](../RepresentationEvents/RepresentationEvents.md)

## Description

Event that is fired whenever a DesignViewRepresentation changes.

## Syntax

RepresentationEvents.**OnActivateDesignView**( ***DocumentObject*** As [Document](../Document/Document.md), ***Representation*** As [DesignViewRepresentation](../DesignViewRepresentation/DesignViewRepresentation.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input AssemblyDocument object that indicates the document in which the change occurred. |
| Representation | [DesignViewRepresentation](../DesignViewRepresentation/DesignViewRepresentation.md) | Input DesignViewRepresentation object that was just activated. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the representation is activated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2012
