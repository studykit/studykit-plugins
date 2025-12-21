# DrawingViewEvents.OnViewUpdate Event

Parent Object: [DrawingViewEvents](../DrawingViewEvents/DrawingViewEvents.md)

## Description

The OnViewUpdate event notifies a client when the document associated with the drawing view has been modified and causes the drawing view to update.

## Remarks

This event in useful in the case where you have created additional sketch geometry or labels referencing that view that may need to be updated to reflect changes in the attached model. Note. Modifying actions should only be performed in the kAfter state. The use of kBefore should be avoided except for query operations.

## Syntax

DrawingViewEvents.**OnViewUpdate**( ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***ReasonsForChange*** As [CommandTypesEnum](../CommandTypesEnum.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Indicates if the notification is being sent before or after the drawing view has been updated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Additional information is provided through this argument to help in understanding the context of the update, as indicated by the value of ReasonsForChange, which is a value from the CommandTypesEnum list, which represents the different categories of changes that can be made. |
| ReasonsForChange | [CommandTypesEnum](../CommandTypesEnum.md) | A value from the CommandTypesEnum list, which represents the different categories of changes that can be made. Typically this will be a single value from the list but it can represent multiple values that have been combined together so you need to use bitwise operations to check for a specific change. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |