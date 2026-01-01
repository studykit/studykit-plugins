# PresentationEvents.OnStoryboardChange Event

Parent Object: [PresentationEvents](../PresentationEvents/PresentationEvents.md)

## Description

Event that fires just before and after a publication is updated because of modeling data changes.

## Syntax

PresentationEvents.**OnStoryboardChange**( ***PublicationObj*** As [Publication](Publication.md), ***StoryboardObj*** As [Storyboard](Storyboard.md), ***ReasonsForChange*** As [CommandTypesEnum](../CommandTypesEnum.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PublicationObj | [Publication](Publication.md) | Input Publication object indicating the presentation in which a Storyboard is being changed. |
| StoryboardObj | [Storyboard](Storyboard.md) | Input Storyboard object indicating which Storyboard is being changed. |
| ReasonsForChange | [CommandTypesEnum](../CommandTypesEnum.md) | This argument indicates the type of change that occurred. The value is from the CommandTypesEnum list, which represents the different categories of changes that can be made. Typically this will be a single value from the list but it can represent multiple values that have been combined together so you need to use bitwise operations to check for a specific change. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the presentation data update. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. This argument provides additional information as described below: Name = "EarliestAffectedTime", Value = Double value indicates the earliest time when the change will affect the Storyboard. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2017
