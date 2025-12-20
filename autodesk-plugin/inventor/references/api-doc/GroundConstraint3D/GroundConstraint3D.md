# GroundConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The GroundConstraint3D object represents a constraint that grounds an entity.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../GroundConstraint3D/GroundConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../GroundConstraint3D/GroundConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GroundConstraint3D/GroundConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../GroundConstraint3D/GroundConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../GroundConstraint3D/GroundConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [Entity](../GroundConstraint3D/GroundConstraint3D_Entity.md) | Property that returns the entity being grounded. |
| [Parent](../GroundConstraint3D/GroundConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../GroundConstraint3D/GroundConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints3D.AddGround](../GeometricConstraints3D/GeometricConstraints3D_AddGround.md), [GroundConstraint3DProxy.NativeObject](../GroundConstraint3DProxy/GroundConstraint3DProxy_NativeObject.md)

## Derived Classes

[GroundConstraint3DProxy](../GroundConstraint3DProxy/GroundConstraint3DProxy.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |