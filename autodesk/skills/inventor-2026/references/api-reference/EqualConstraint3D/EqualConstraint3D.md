# EqualConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

EqualConstraint3D Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../EqualConstraint3D/EqualConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../EqualConstraint3D/EqualConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EqualConstraint3D/EqualConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../EqualConstraint3D/EqualConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../EqualConstraint3D/EqualConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../EqualConstraint3D/EqualConstraint3D_EntityOne.md) | Read-only property that returns the first 3D sketch entity being constrained. |
| [EntityTwo](../EqualConstraint3D/EqualConstraint3D_EntityTwo.md) | Read-only property that returns the second 3D sketch entity being constrained. |
| [Parent](../EqualConstraint3D/EqualConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../EqualConstraint3D/EqualConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[EqualConstraint3DProxy.NativeObject](../EqualConstraint3DProxy/EqualConstraint3DProxy_NativeObject.md), [GeometricConstraints3D.AddEqual](../GeometricConstraints3D/GeometricConstraints3D_AddEqual.md)

## Derived Classes

[EqualConstraint3DProxy](../EqualConstraint3DProxy/EqualConstraint3DProxy.md)

## Version

Introduced in version 2017
