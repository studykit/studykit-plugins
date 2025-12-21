# GeometricConstraints.AddConcentric Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new concentric constraint between the two input sketch entities. The two entities must be circles, arcs, ellipses, or elliptical arcs. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddConcentric**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md) ) As [ConcentricConstraint](../ConcentricConstraint/ConcentricConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. Must be a circle, arc, ellipse, or elliptical arc. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. Must be a circle, arc, ellipse, or elliptical arc. |

## Version

Introduced in version 5
