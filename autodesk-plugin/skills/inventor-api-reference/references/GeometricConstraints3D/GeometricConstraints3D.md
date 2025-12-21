# GeometricConstraints3D Object

## Description

The GeometricConstraints3D object provides access to all the geometric sketch constraints ( objects) in a 3D sketch and provides methods to create additional geometric sketch constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddCoincident](../GeometricConstraints3D/GeometricConstraints3D_AddCoincident.md) | Method that creates a new coincident constraint between two entities. One of the input entities must be a sketch point. The other entity can be any other type of sketch entity (but not a sketch point). Placing a coincident constraint between two points will fail. Use the ConnectTo method on the SketchPoint3D object to merge two points. This method will fail if the constraint overconstrains the sketch. |
| [AddCollinear](../GeometricConstraints3D/GeometricConstraints3D_AddCollinear.md) | Method that creates a new collinear constraint between the two input objects. This method will fail if the constraint overconstrains the sketch. |
| [AddCustom](../GeometricConstraints3D/GeometricConstraints3D_AddCustom.md) | Method that creates a new custom constraint on the input sketch entity. |
| [AddEqual](../GeometricConstraints3D/GeometricConstraints3D_AddEqual.md) | Creates a new equal constraint between the input entities. |
| [AddGround](../GeometricConstraints3D/GeometricConstraints3D_AddGround.md) | Method that creates a new ground constraint on the input sketch entity. This method will fail if the constraint overconstrains the sketch. |
| [AddMidpoint](../GeometricConstraints3D/GeometricConstraints3D_AddMidpoint.md) | Method that creates a new midpoint constraint between the input point and the midpoint of the line. This causes the input sketch point to be positioned at the midpoint of the \input line. This method will fail if the constraint overconstrains the sketch. |
| [AddOnFace](../GeometricConstraints3D/GeometricConstraints3D_AddOnFace.md) | Creates a new on face constraint between the input entity and face. |
| [AddParallel](../GeometricConstraints3D/GeometricConstraints3D_AddParallel.md) | Method that creates a new parallel constraint between the two input entities. This method will fail if the constraint overconstrains the sketch. |
| [AddParallelToXAxis](../GeometricConstraints3D/GeometricConstraints3D_AddParallelToXAxis.md) | Creates a new parallel constraint between the input entity and X-axis. |
| [AddParallelToXYPlane](../GeometricConstraints3D/GeometricConstraints3D_AddParallelToXYPlane.md) | Creates a new parallel constraint between the input entity and XY-plane. |
| [AddParallelToXZPlane](../GeometricConstraints3D/GeometricConstraints3D_AddParallelToXZPlane.md) | Creates a new parallel constraint between the input entity and XZ-plane. |
| [AddParallelToYAxis](../GeometricConstraints3D/GeometricConstraints3D_AddParallelToYAxis.md) | Creates a new parallel constraint between the input entity and Y-axis. |
| [AddParallelToYZPlane](../GeometricConstraints3D/GeometricConstraints3D_AddParallelToYZPlane.md) | Creates a new parallel constraint between the input entity and YZ-plane. |
| [AddParallelToZAxis](../GeometricConstraints3D/GeometricConstraints3D_AddParallelToZAxis.md) | Creates a new parallel constraint between the input entity and Z-axis. |
| [AddPerpendicular](../GeometricConstraints3D/GeometricConstraints3D_AddPerpendicular.md) | Method that creates a new perpendicular constraint between the two input entities. This method will fail if the constraint overconstrains the sketch. |
| [AddSmooth](../GeometricConstraints3D/GeometricConstraints3D_AddSmooth.md) | Method that creates a new smooth (G2-continuous) constraint. This method will fail if the constraint overconstrains the sketch. |
| [AddTangent](../GeometricConstraints3D/GeometricConstraints3D_AddTangent.md) | Method that creates a new tangent constraint. This method will fail if the constraint overconstrains the sketch or if the two input entities do not share at least one common sketch point. In creating the constraint, the method attempts to match the existing orientation between the two curves. If the dot product of the direction vectors for the curves at the tangent point is greater than 0.0 the options for the tangent constraint is set to be outward. That means that if you look at the curves and ignore the parameterization, the curves will be going in opposite directions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GeometricConstraints3D/GeometricConstraints3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../GeometricConstraints3D/GeometricConstraints3D_Count.md) | Property that returns the number of items in the collection. |
| [Item](../GeometricConstraints3D/GeometricConstraints3D_Item.md) | Returns the specified geometric sketch constraint object from the collection. |
| [Type](../GeometricConstraints3D/GeometricConstraints3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sketch3D.GeometricConstraints3D](../Sketch3D/Sketch3D_GeometricConstraints3D.md), [Sketch3DProxy.GeometricConstraints3D](../Sketch3DProxy/Sketch3DProxy_GeometricConstraints3D.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |