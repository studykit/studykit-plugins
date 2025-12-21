# DimensionConstraints.AddArcLength Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new arc length dimension on the input arc. This method will fail in the case where a driving dimension is specified and it will overconstrain the sketch.

## Syntax

DimensionConstraints.**AddArcLength**( ***Entity*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***TextPoint*** As [Point2d](../Point2d/Point2d.md), [***Driven***] As Boolean ) As [ArcLengthDimConstraint](../ArcLengthDimConstraint/ArcLengthDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | [SketchEntity](../SketchEntity/SketchEntity.md) | Input SketchArc object. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the position of the dimension text. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creates an Arc Length Dimension Constraint](../../sample-programs/ArcLengthDimConstraint_Sample.md) | Demonstrates creating an arc length dimension constraint. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |