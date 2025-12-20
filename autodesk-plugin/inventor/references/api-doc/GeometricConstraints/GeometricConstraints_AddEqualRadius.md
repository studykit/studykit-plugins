# GeometricConstraints.AddEqualRadius Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new equal radius constraint between the two input sketch entities. Valid input entities are circles and arcs. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddEqualRadius**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md) ) As [EqualRadiusConstraint](../EqualRadiusConstraint/EqualRadiusConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. Must be a circle or arc. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. Must be a circle or arc. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |