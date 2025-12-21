# Edge.GeometryType Property

Parent Object: [Edge](../Edge/Edge.md)

## Description

Get the curve type of the curve that will be returned from the Geometry property.

## Syntax

Edge.**GeometryType**() As [CurveTypeEnum](../CurveTypeEnum.md)

## Property Value

This is a read only property whose value is a [CurveTypeEnum](../CurveTypeEnum.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Window Selection](../../sample-programs/SelectEventsObject_WindowSelectEnabled_Sample.md) | This sample demonstrates using the selection events to window-select multiple edges. Selection is dependent on events and VB only supports events within a class module. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |