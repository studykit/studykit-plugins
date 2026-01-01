# RepresentationEvents.OnNewPositionalRepresentation Event

Parent Object: [RepresentationEvents](../RepresentationEvents/RepresentationEvents.md)

## Description

The OnNewPositionalRepresentation event notifies the client when a new positional representation is created.

## Syntax

RepresentationEvents.**OnNewPositionalRepresentation**( ***DocumentObject*** As [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md), ***Representation*** As [PositionalRepresentation](../PositionalRepresentation/PositionalRepresentation.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md) | The Document object the positional representation is being created within. |
| Representation | [PositionalRepresentation](../PositionalRepresentation/PositionalRepresentation.md) | The new PositionalRepresentation object that has just been created. When the BeforeOrAfter argument is kBefore, this argument is Nothing since the positional representation has not yet been created. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the positional representation has been created. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11
