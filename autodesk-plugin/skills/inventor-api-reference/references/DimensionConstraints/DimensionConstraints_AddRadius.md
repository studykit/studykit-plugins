# DimensionConstraints.AddRadius Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new radius dimension constraint on the input circle or arc.

## Remarks

The picture below illustrates the result of adding an arc dimension constraint.

![](../images/RadiusDimConstraint.png)

## Syntax

DimensionConstraints.**AddRadius**( ***Entity*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), [***Driven***] As Boolean ) As [RadiusDimConstraint](../RadiusDimConstraint/RadiusDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | [SketchEntity](../SketchEntity/SketchEntity.md) | Input or SketchArc object. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input object that defines the position of the dimension text. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |