# MidpointConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The MidpointConstraint3D object represents a constraint that connects a sketch point to the midpoint of a sketch line.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MidpointConstraint3D/MidpointConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../MidpointConstraint3D/MidpointConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MidpointConstraint3D/MidpointConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../MidpointConstraint3D/MidpointConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../MidpointConstraint3D/MidpointConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [Line](../MidpointConstraint3D/MidpointConstraint3D_Line.md) | Property that returns the sketch line being constrained. |
| [Parent](../MidpointConstraint3D/MidpointConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Point](../MidpointConstraint3D/MidpointConstraint3D_Point.md) | Property that returns the sketch point being constrained. |
| [Type](../MidpointConstraint3D/MidpointConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints3D.AddMidpoint](../GeometricConstraints3D/GeometricConstraints3D_AddMidpoint.md), [MidpointConstraint3DProxy.NativeObject](../MidpointConstraint3DProxy/MidpointConstraint3DProxy_NativeObject.md)

## Derived Classes

[MidpointConstraint3DProxy](../MidpointConstraint3DProxy/MidpointConstraint3DProxy.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |