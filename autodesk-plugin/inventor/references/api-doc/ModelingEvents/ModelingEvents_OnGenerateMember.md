# ModelingEvents.OnGenerateMember Event

Parent Object: [ModelingEvents](../ModelingEvents/ModelingEvents.md)

## Description

Event that fires before and after an iPart or an iAssembly member is being generated or regenerated.

## Syntax

ModelingEvents.**OnGenerateMember**( ***FactoryDocumentObject*** As [Document](../Document/Document.md), ***MemberName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FactoryDocumentObject | [Document](../Document/Document.md) | Name of the factory document. |
| MemberName | String | Name of iPart or iAssembly member. If multiple members are generated this returns the first member name. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the feature is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that, if populated, can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of how the member is generated:  Name = "GenerateMemberReason", Value = String value that indicates the reason, the value can be "Create", "Update" or "Regenerate".  Name = "MemberFileName", Value = String value that indicates the full filename of the member file which is being generated.  Name = "AllGeneratedMembersFiles", Value = String array that indicates the full filename of the member files that are going to be generated. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |