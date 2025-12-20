# DimensionConstraints.AddTwoLineAngle Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new angular dimension constraint between two lines.

## Remarks

The position of the text point defines which of the four quadrants the constraint is placed within. The picture below illustrates the result of adding a two-line angle dimension constraint.

![](../images/TwoLineAngleDimConstraint.png)

## Syntax

DimensionConstraints.**AddTwoLineAngle**( ***LineOne*** As [SketchLine](../SketchLine/SketchLine.md), ***LineTwo*** As [SketchLine](../SketchLine/SketchLine.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), [***Driven***] As Boolean ) As [TwoLineAngleDimConstraint](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LineOne | [SketchLine](../SketchLine/SketchLine.md) | Input sketch line. |
| LineTwo | [SketchLine](../SketchLine/SketchLine.md) | Input sketch line. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input object that defines the position of the dimension text and which of the four possible quadrants to place the dimension within. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |