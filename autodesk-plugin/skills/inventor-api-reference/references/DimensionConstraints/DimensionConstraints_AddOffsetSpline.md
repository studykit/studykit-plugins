# DimensionConstraints.AddOffsetSpline Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Creates a new offsetSpline dimension constraint between offset spline and the original spline.

## Syntax

DimensionConstraints.**AddOffsetSpline**( ***Line*** As [SketchOffsetSpline](../SketchOffsetSpline/SketchOffsetSpline.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), [***Driven***] As Boolean ) As [OffsetSplineDimConstraint](../OffsetSplineDimConstraint/OffsetSplineDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | [SketchOffsetSpline](../SketchOffsetSpline/SketchOffsetSpline.md) | Input object. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input object that defines the position of the dimension text. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default is False, which will create a driving dimension. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |