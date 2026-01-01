# OnFaceConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

OnFaceConstraint3D Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../OnFaceConstraint3D/OnFaceConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../OnFaceConstraint3D/OnFaceConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../OnFaceConstraint3D/OnFaceConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../OnFaceConstraint3D/OnFaceConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../OnFaceConstraint3D/OnFaceConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [Entity](../OnFaceConstraint3D/OnFaceConstraint3D_Entity.md) | Read-only property that returns the 3D sketch entity being constrained. |
| [Face](../OnFaceConstraint3D/OnFaceConstraint3D_Face.md) | Read-only property that returns the Face which the 3D sketch entity is constrained to. |
| [Parent](../OnFaceConstraint3D/OnFaceConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../OnFaceConstraint3D/OnFaceConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints3D.AddOnFace](../GeometricConstraints3D/GeometricConstraints3D_AddOnFace.md), [OnFaceConstraint3DProxy.NativeObject](../OnFaceConstraint3DProxy/OnFaceConstraint3DProxy_NativeObject.md)

## Derived Classes

[OnFaceConstraint3DProxy](../OnFaceConstraint3DProxy/OnFaceConstraint3DProxy.md)

## Version

Introduced in version 2017
