# GeometricConstraints.AddVertical Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new vertical constraint on the input sketch entity. Valid input objects are lines and ellipses. Either the major or minor axis of an ellipse is used depending on the value of the UseEllipseMajorAxis input argument. When an ellipse is used, the specified axis of the ellipse will become vertical. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddVertical**( ***Entity*** As [SketchEntity](../SketchEntity/SketchEntity.md), [***UseEllipseMajorAxis***] As Boolean ) As [VerticalConstraint](../VerticalConstraint/VerticalConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. Must be a line, ellipse, or elliptical arc. |
| UseEllipseMajorAxis | Boolean | Optional Boolean that specifies whether to use the major or minor axis for the ellipse. This argument only applies when the input entity is an ellipse or elliptical arc. Inputting True results in the constraint being applied to the major axis. This value is ignored when a line is supplied for the entity. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |