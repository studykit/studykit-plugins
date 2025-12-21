# DrawingEvents.OnRetrieveDimensions Event

Parent Object: [DrawingEvents](../DrawingEvents/DrawingEvents.md)

## Description

The OnRetrieveDimensions event notifies a client whenever dimensions are retrieved into a drawing using the Retrieve Dimensions command.

## Syntax

DrawingEvents.**OnRetrieveDimensions**( ***SketchDimensions*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***DrawingDimensions*** As [GeneralDimensionsEnumerator](../GeneralDimensionsEnumerator/GeneralDimensionsEnumerator.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchDimensions | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | A collection containing the original dimensions that were retrieved into the drawing. These will be various dimension constraints or feature dimensions that were created in the part or drawing sketch. Feature dimensions are the dimensions created automatically when a feature is created. For example, when you create an extrude feature with a distance extent two feature dimensions are created. One to control the distance and another to control the taper angle. |
| DrawingDimensions | [GeneralDimensionsEnumerator](../GeneralDimensionsEnumerator/GeneralDimensionsEnumerator.md) | A collection containing the drawing dimensions that were created as a result of the retrieve. The items in this collection will match up 1 for 1 with the dimensions provided by the SketchDimensions argument. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. This notification is only provided after the dimensions have been retrieved so the value of this argument will always be kAfter. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |