# GeometricConstraints3D.AddTangent Method

Parent Object: [GeometricConstraints3D](../GeometricConstraints3D/GeometricConstraints3D.md)

## Description

Method that creates a new tangent constraint. This method will fail if the constraint overconstrains the sketch or if the two input entities do not share at least one common sketch point. In creating the constraint, the method attempts to match the existing orientation between the two curves. If the dot product of the direction vectors for the curves at the tangent point is greater than 0.0 the options for the tangent constraint is set to be outward. That means that if you look at the curves and ignore the parameterization, the curves will be going in opposite directions.

## Syntax

GeometricConstraints3D.**AddTangent**( ***EntityOne*** As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md), ***EntityTwo*** As Object, [***ProximityPoint***] As Variant ) As [TangentConstraint3D](../TangentConstraint3D/TangentConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) | Input sketch object. |
| EntityTwo | Object | Input sketch or edge object. |
| ProximityPoint | Variant | Optional input object that specifies where the tangency should be applied in the case where the input entities share two sketch points. |

## Version

Introduced in version 8
