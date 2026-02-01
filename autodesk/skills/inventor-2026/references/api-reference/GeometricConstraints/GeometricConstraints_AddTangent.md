# GeometricConstraints.AddTangent Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new tangent constraint. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddTangent**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md), [***ProximityPoint***] As Variant ) As [TangentSketchConstraint](../TangentSketchConstraint/TangentSketchConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch object. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch object. |
| ProximityPoint | Variant | Optional input Point object that specifies where the tangency should be applied in the case where the input entities share two sketch points. |

## Version

Introduced in version 5
