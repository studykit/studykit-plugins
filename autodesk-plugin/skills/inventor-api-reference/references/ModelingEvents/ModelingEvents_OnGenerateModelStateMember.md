# ModelingEvents.OnGenerateModelStateMember Event

Parent Object: [ModelingEvents](../ModelingEvents/ModelingEvents.md)

## Description

Event that fires before and after an model state member document is being generated or regenerated.

## Syntax

ModelingEvents.**OnGenerateModelStateMember**( ***FactoryDocumentObject*** As [Document](../Document/Document.md), ***MemberName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FactoryDocumentObject | [Document](../Document/Document.md) | Model state factory document. |
| MemberName | String | Name of model state member. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the model state member is generated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that, if populated, can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of how the model state member is generated: Name = "GenerateMemberReason", Value = String value that indicates the reason, the value can be "Create", "Update" or "Regenerate". |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |