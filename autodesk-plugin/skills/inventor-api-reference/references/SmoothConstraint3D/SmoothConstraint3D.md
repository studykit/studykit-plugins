# SmoothConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The SmoothConstraint3D object represents a smooth (G2-continuous) constraint within a 3d sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SmoothConstraint3D/SmoothConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../SmoothConstraint3D/SmoothConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SmoothConstraint3D/SmoothConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SmoothConstraint3D/SmoothConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../SmoothConstraint3D/SmoothConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../SmoothConstraint3D/SmoothConstraint3D_EntityOne.md) | Property that returns the sketch entity that is constrained to be smooth (G2-continuous) to entity two. |
| [EntityTwo](../SmoothConstraint3D/SmoothConstraint3D_EntityTwo.md) | Property that returns the sketch entity that is constrained to be smooth (G2-continuous) to entity one. |
| [Parent](../SmoothConstraint3D/SmoothConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../SmoothConstraint3D/SmoothConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints3D.AddSmooth](../GeometricConstraints3D/GeometricConstraints3D_AddSmooth.md), [SmoothConstraint3DProxy.NativeObject](../SmoothConstraint3DProxy/SmoothConstraint3DProxy_NativeObject.md)

## Derived Classes

[SmoothConstraint3DProxy](../SmoothConstraint3DProxy/SmoothConstraint3DProxy.md)

## Version

Introduced in version 11
