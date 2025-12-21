# CollinearConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The CollinearConstraint3D object represents a collinear constraint within a 3D sketch. The constraint can be applied between two 3D sketch lines, or between a 3D sketch line and a work axis.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CollinearConstraint3D/CollinearConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../CollinearConstraint3D/CollinearConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CollinearConstraint3D/CollinearConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CollinearConstraint3D/CollinearConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../CollinearConstraint3D/CollinearConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../CollinearConstraint3D/CollinearConstraint3D_EntityOne.md) | Property that returns the first entity being constrained. This can either be a SketchLine3D or a WorkAxis. |
| [EntityTwo](../CollinearConstraint3D/CollinearConstraint3D_EntityTwo.md) | Property that returns the second entity being constrained. This can either be a SketchLine3D or a WorkAxis. |
| [Parent](../CollinearConstraint3D/CollinearConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../CollinearConstraint3D/CollinearConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CollinearConstraint3DProxy.NativeObject](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_NativeObject.md), [GeometricConstraints3D.AddCollinear](../GeometricConstraints3D/GeometricConstraints3D_AddCollinear.md)

## Derived Classes

[CollinearConstraint3DProxy](../CollinearConstraint3DProxy/CollinearConstraint3DProxy.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |