# TangentConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The TangentConstraint3D object represents a tangent constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TangentConstraint3D/TangentConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [FlipDirection](../TangentConstraint3D/TangentConstraint3D_FlipDirection.md) | Flips the direction of the tangency between the two 3D entities. |
| [GetReferenceKey](../TangentConstraint3D/TangentConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TangentConstraint3D/TangentConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TangentConstraint3D/TangentConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../TangentConstraint3D/TangentConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../TangentConstraint3D/TangentConstraint3D_EntityOne.md) | Property that returns the sketch entity that is constrained to be tangent to entity two. |
| [EntityTwo](../TangentConstraint3D/TangentConstraint3D_EntityTwo.md) | Property that returns the sketch entity that is constrained to be tangent to entity one. |
| [Parent](../TangentConstraint3D/TangentConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../TangentConstraint3D/TangentConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints3D.AddTangent](../GeometricConstraints3D/GeometricConstraints3D_AddTangent.md), [TangentConstraint3DProxy.NativeObject](../TangentConstraint3DProxy/TangentConstraint3DProxy_NativeObject.md)

## Derived Classes

[TangentConstraint3DProxy](../TangentConstraint3DProxy/TangentConstraint3DProxy.md)

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |