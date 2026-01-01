# GeometricConstraints3D.AddSmooth Method

Parent Object: [GeometricConstraints3D](../GeometricConstraints3D/GeometricConstraints3D.md)

## Description

Method that creates a new smooth (G2-continuous) constraint. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints3D.**AddSmooth**( ***EntityOne*** As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md), ***EntityTwo*** As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md), [***ProximityPoint***] As Variant ) As [SmoothConstraint3D](../SmoothConstraint3D/SmoothConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) | Input sketch entity. |
| EntityTwo | [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) | Input sketch entity. |
| ProximityPoint | Variant | Optional input Point object that specifies which ends of the curves to make smooth in case there are multiple connections. |

## Version

Introduced in version 11
