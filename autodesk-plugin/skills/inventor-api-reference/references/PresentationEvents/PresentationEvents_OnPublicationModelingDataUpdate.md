# PresentationEvents.OnPublicationModelingDataUpdate Event

Parent Object: [PresentationEvents](../PresentationEvents/PresentationEvents.md)

## Description

Event that fires just before and after a publication component is changed.

## Syntax

PresentationEvents.**OnPublicationModelingDataUpdate**( ***Publication*** As [Publication](Publication.md), ***ReasonsForChange*** As [CommandTypesEnum](../CommandTypesEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Publication | [Publication](Publication.md) | Input Publication object indicating which publication is being updated. |
| ReasonsForChange | [CommandTypesEnum](../CommandTypesEnum.md) | This argument indicates the type of change that occurred. The value is from the CommandTypesEnum list, which represents the different categories of changes that can be made. Typically this will be a single value from the list but it can represent multiple values that have been combined together so you need to use bitwise operations to check for a specific change. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the presentation data update. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. This argument provides additional information as described below:  Name = "Restructure", Value = ObjectCollection containing the PresentationComponent objects which are re-structured because of modeling data change. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |