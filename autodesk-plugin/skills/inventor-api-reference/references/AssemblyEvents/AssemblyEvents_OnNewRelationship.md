# AssemblyEvents.OnNewRelationship Event

Parent Object: [AssemblyEvents](../AssemblyEvents/AssemblyEvents.md)

## Description

The OnNewRelationship event notifies a client when a new constraint or connection is added to an assembly.

## Syntax

AssemblyEvents.**OnNewRelationship**( ***DocumentObject*** As [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md), ***Relationship*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md) | The AssemblyDocument object that represents the assembly the constraint is being added to. |
| Relationship | Object | The new relationship (an AssemblyConstraint, iMateResult, or AssemblyConnection) that was just created. When the value of the BeforeOrAfter argument is kBefore, Nothing is returned for this argument. When the value is kAfter, the new assembly relationship object is returned. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the relationship is created. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is currently provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2014
