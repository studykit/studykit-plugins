# DimensionConstraints.AddEllipseRadius Method

Parent Object: [DimensionConstraints](../DimensionConstraints/DimensionConstraints.md)

## Description

Method that creates a new dimension constraint defining the major or minor radius of the ellipse. This method will fail in the case where a driving dimension is specified and it will overconstrain the sketch.

## Syntax

DimensionConstraints.**AddEllipseRadius**( ***Entity*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***MajorRadius*** As Boolean, ***TextPoint*** As [Point2d](../Point2d/Point2d.md), [***PositiveSide***] As Variant, [***Driven***] As Boolean ) As [EllipseRadiusDimConstraint](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | [SketchEntity](../SketchEntity/SketchEntity.md) | Input SketchEllipse or SketchEllipticalArc object. |
| MajorRadius | Boolean | Boolean that defines if the dimension is for the major or minor radius of the ellipse. |
| TextPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the position of the dimension text. This also defines which side of the ellipse the dimension is placed on if the PositiveSide argument is not specified. |
| PositiveSide | Variant | Optional input Boolean that specifies whether to dimension the positive or the negative side of the major/minor axis. If not specified, the position of the TextPoint defines which side the dimension is placed on. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sketch elliptical arc](../../sample-programs/SketchEllipticalArc_Sample.md) | This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |