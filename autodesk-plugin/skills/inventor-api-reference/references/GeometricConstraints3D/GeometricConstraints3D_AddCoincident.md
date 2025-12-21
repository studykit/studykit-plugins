# GeometricConstraints3D.AddCoincident Method

Parent Object: [GeometricConstraints3D](../GeometricConstraints3D/GeometricConstraints3D.md)

## Description

Method that creates a new coincident constraint between two entities. One of the input entities must be a sketch point. The other entity can be any other type of sketch entity (but not a sketch point). Placing a coincident constraint between two points will fail. Use the ConnectTo method on the SketchPoint3D object to merge two points. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints3D.**AddCoincident**( ***EntityOne*** As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md), ***EntityTwo*** As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) ) As [CoincidentConstraint3D](../CoincidentConstraint3D/CoincidentConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) | Input sketch entity. |
| EntityTwo | [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) | Input sketch entity. |

## Version

Introduced in version 2009
