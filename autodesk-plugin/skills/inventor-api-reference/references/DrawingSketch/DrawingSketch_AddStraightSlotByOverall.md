# DrawingSketch.AddStraightSlotByOverall Method

Parent Object: [DrawingSketch](../DrawingSketch/DrawingSketch.md)

## Description

Method that creates a straight slot. The sketch entities represent the sketch slot are returned.

## Syntax

DrawingSketch.**AddStraightSlotByOverall**( ***StartPoint*** As Object, ***EndPoint*** As Object, ***Width*** As Double ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | Object | Input Point2d or SketchPoint object that defines the overall start point. The overall start point is a midpoint of the first arc of the straight slot. |
| EndPoint | Object | Input Point2d or SketchPoint object that defines the overall end point. The overall end point is a midpoint of the second arc of the straight slot. |
| Width | Double | Input Double that specifies the width of the straight slot in centimeters. |

## Version

Introduced in version 2014
