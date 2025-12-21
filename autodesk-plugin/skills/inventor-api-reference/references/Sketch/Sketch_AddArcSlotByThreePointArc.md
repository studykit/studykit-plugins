# Sketch.AddArcSlotByThreePointArc Method

Parent Object: [Sketch](../Sketch/Sketch.md)

## Description

Method that creates an arc slot. The sketch entities represent the sketch slot are returned.

## Remarks

No dimension constraints are created.

## Syntax

Sketch.**AddArcSlotByThreePointArc**( ***StartPoint*** As Object, ***MidPoint*** As Object, ***EndPoint*** As Object, ***Width*** As Double ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | Object | Input Point2d or SketchPoint object that defines the starting point of the slot’s center-line. |
| MidPoint | Object | Input Point2d or SketchPoint object that defines a point along the slot’s center-line. |
| EndPoint | Object | Input Point2d or SketchPoint object that defines the end point of the slot’s center-line. |
| Width | Double | Input a Double that specifies the width of the arc slot in centimeters. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create slots in sketch.](../../sample-programs/SketchSlots_Sample.md) | This sample demonstrates several new methods to create sketch entities that represent slots. These are the equivalent to new sketch commands that were added in Inventor 2014. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |