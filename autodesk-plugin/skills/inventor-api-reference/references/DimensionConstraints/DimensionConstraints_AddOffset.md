# DimensionConstraints.AddOffset Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new offset dimension constraint between two entities.

## Remarks

One of the input entities must be a sketch line. The other entity can be either a line or a point. When two lines are input this constraint has the effect of forcing parallelism between the lines. The dimension axis is perpendicular to the sketch line input for the Line argument. The picture below illustrates two cases of the offset dimension constraint. In the dimension with the 0.614 value, the two red vertical lines are constrained. In the second case the line representing the center line and the horizontal red line are constrained. In the second case the LinearDiameter flag was set to True to result in the linear diameter type of dimension.

![](../images/OffsetDimConstraint1.png)

In the picture below, two offset dimension constraints are placed. This illustrates that the input line controls the axis of the dimension. The dimension line is perpendicular to the sketch line. The distance between the line and the other object is controlled by the constraint. The two dimensions below are both between a line and a point. The 0.684 dia. was placed with the LinearDiameter flag set to true.

![](../images/OffsetDimConstraint2.png)

## Syntax

DimensionConstraints.**AddOffset**( ***Line*** As [SketchLine](../SketchLine/SketchLine.md), ***Entity*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), ***LinearDiameter*** As Boolean, [***Driven***] As Boolean ) As [OffsetDimConstraint](../OffsetDimConstraint/OffsetDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | [SketchLine](../SketchLine/SketchLine.md) | Input SketchLine object. |
| Entity | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. This must be either a or SketchPoint object. If creating a linear diameter dimension and Entity is a SketchLine, then Entity is used as the centerline. If Entity is a SketchPoint, then Line is used as the centerline. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input object that defines the position of the dimension text. |
| LinearDiameter | Boolean | Input Boolean that specifies whether the dimension should be a standard distance dimension or be displayed as a linear diameter dimension. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default is False, which will create a driving dimension. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |