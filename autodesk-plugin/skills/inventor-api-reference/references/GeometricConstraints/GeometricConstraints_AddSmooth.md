# GeometricConstraints.AddSmooth Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new smooth (G2-continuous) constraint. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddSmooth**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md), [***ProximityPoint***] As Variant ) As [SmoothConstraint](../SmoothConstraint/SmoothConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. |
| ProximityPoint | Variant | Optional input Point2d object that specifies which ends of the curves to make smooth in case there are multiple connections. |

## Version

Introduced in version 11
