# DimensionConstraints.AddTwoPointDistance Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new linear dimension constraint between two points.

## Remarks

The result can be either a vertical, horizontal, or aligned dimension depending on the orientation specified. The picture below illustrates the three possible cases when placing this constraint between two points.

![](../images/TwoPointDistanceDimConstraint.png)

## Syntax

DimensionConstraints.**AddTwoPointDistance**( ***PointOne*** As [SketchPoint](../SketchPoint/SketchPoint.md), ***PointTwo*** As [SketchPoint](../SketchPoint/SketchPoint.md), ***Orientation*** As [DimensionOrientationEnum](../DimensionOrientationEnum.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), [***Driven***] As Boolean ) As [TwoPointDistanceDimConstraint](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointOne | [SketchPoint](../SketchPoint/SketchPoint.md) | Input sketch point. |
| PointTwo | [SketchPoint](../SketchPoint/SketchPoint.md) | Input sketch point. |
| Orientation | [DimensionOrientationEnum](../DimensionOrientationEnum.md) | Input constant that specifies if the dimension is horizontal, vertical, or aligned. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input object that defines the position of the dimension text. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |