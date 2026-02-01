# PerpendicularConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The PerpendicularConstraint3D object represents a perpendicular constraint within a 3D sketch. The constraint can be applied between a 3D sketch line and another 3D sketch line, a work axis, linear edge, work plane or a surface (face).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../PerpendicularConstraint3D/PerpendicularConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../PerpendicularConstraint3D/PerpendicularConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PerpendicularConstraint3D/PerpendicularConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PerpendicularConstraint3D/PerpendicularConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../PerpendicularConstraint3D/PerpendicularConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../PerpendicularConstraint3D/PerpendicularConstraint3D_EntityOne.md) | Property that returns the first sketch entity being constrained. |
| [EntityTwo](../PerpendicularConstraint3D/PerpendicularConstraint3D_EntityTwo.md) | Property that returns the second sketch entity being constrained. |
| [Parent](../PerpendicularConstraint3D/PerpendicularConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../PerpendicularConstraint3D/PerpendicularConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints3D.AddPerpendicular](../GeometricConstraints3D/GeometricConstraints3D_AddPerpendicular.md), [PerpendicularConstraint3DProxy.NativeObject](../PerpendicularConstraint3DProxy/PerpendicularConstraint3DProxy_NativeObject.md)

## Derived Classes

[PerpendicularConstraint3DProxy](../PerpendicularConstraint3DProxy/PerpendicularConstraint3DProxy.md)

## Version

Introduced in version 10
