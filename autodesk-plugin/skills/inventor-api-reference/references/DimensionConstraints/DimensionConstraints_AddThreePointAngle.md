# DimensionConstraints.AddThreePointAngle Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new angular dimension constraint between three points.

## Remarks

The position of the text point defines which of the four quadrants the constraint is placed within. The picture below illustrates the result of adding a three-point angle dimension constraint.

![](../images/ThreePointAngleDimConstraint.png)

The General Dimension command allows you to place a dimension controlling the sweep angle of an arc by selecting the arc and the center point. This results in a three point angle dimension constraint being placed between the two sketch points at the end of the arc and the sketch point at the center. This results in a dimension like that shown below.

![](../images/ArcAngleDimConstraint.png)

## Syntax

DimensionConstraints.**AddThreePointAngle**( ***PointOne*** As [SketchPoint](../SketchPoint/SketchPoint.md), ***PointTwo*** As [SketchPoint](../SketchPoint/SketchPoint.md), ***PointThree*** As [SketchPoint](../SketchPoint/SketchPoint.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), [***Driven***] As Boolean ) As [ThreePointAngleDimConstraint](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointOne | [SketchPoint](../SketchPoint/SketchPoint.md) | Input sketch point. |
| PointTwo | [SketchPoint](../SketchPoint/SketchPoint.md) | Input sketch point. This point defines the vertex point of the angle. |
| PointThree | [SketchPoint](../SketchPoint/SketchPoint.md) | Input sketch point. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input object that defines the position of the dimension text and which of the four possible quadrants to place the dimension within. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |