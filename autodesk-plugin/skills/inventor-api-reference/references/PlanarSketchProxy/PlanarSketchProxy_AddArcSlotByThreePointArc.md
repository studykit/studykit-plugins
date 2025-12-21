# PlanarSketchProxy.AddArcSlotByThreePointArc Method

Parent Object: [PlanarSketchProxy](../PlanarSketchProxy/PlanarSketchProxy.md)

## Description

Method that creates an arc slot. The sketch entities represent the sketch slot are returned.

## Syntax

PlanarSketchProxy.**AddArcSlotByThreePointArc**( ***StartPoint*** As Object, ***MidPoint*** As Object, ***EndPoint*** As Object, ***Width*** As Double ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | Object | Input Point2d or SketchPoint object that defines the starting point of the slot’s center-line. |
| MidPoint | Object | Input Point2d or SketchPoint object that defines a point along the slot’s center-line. |
| EndPoint | Object | Input Point2d or SketchPoint object that defines the end point of the slot’s center-line. |
| Width | Double | Input a Double that specifies the width of the arc slot in centimeters. |

## Version

Introduced in version 2014
