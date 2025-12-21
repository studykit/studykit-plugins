# RepresentationEvents.OnActivatePositionalRepresentation Event

Parent Object: [RepresentationEvents](../RepresentationEvents/RepresentationEvents.md)

## Description

The OnActivatePositionalRepresentation event notifies the client when a positional representation is being activated.

## Syntax

RepresentationEvents.**OnActivatePositionalRepresentation**( ***DocumentObject*** As [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md), ***Representation*** As [PositionalRepresentation](../PositionalRepresentation/PositionalRepresentation.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md) | The Document object the positional representation is being activated within. |
| Representation | [PositionalRepresentation](../PositionalRepresentation/PositionalRepresentation.md) | The PositionalRepresentation object that is being activated. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the positional representation has been activated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11
