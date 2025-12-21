# Sketch.AddStraightSlotByCenterToCenter Method

Parent Object: [Sketch](../Sketch/Sketch.md)

## Description

Method that creates a straight slot. The sketch entities represent the sketch slot are returned.

## Remarks

No dimension constraints are created.

## Syntax

Sketch.**AddStraightSlotByCenterToCenter**( ***StartPoint*** As Object, ***EndPoint*** As Object, ***Width*** As Double ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | Object | Input Point2d or SketchPoint object that defines the starting center point of the straight slot. |
| EndPoint | Object | Input Point2d or SketchPoint object that defines the ending center point of the straight slot. |
| Width | Double | Input Double that specifies the width of the straight slot in centimeters. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create slots in sketch.](../../sample-programs/SketchSlots_Sample.md) | This sample demonstrates several new methods to create sketch entities that represent slots. These are the equivalent to new sketch commands that were added in Inventor 2014. |

## Version

Introduced in version 2014
