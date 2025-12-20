# CustomConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The CustomConstraint3D object represents a custom constraint for a 3D sketch entity.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CustomConstraint3D/CustomConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../CustomConstraint3D/CustomConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CustomConstraint3D/CustomConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CustomConstraint3D/CustomConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ClientId](../CustomConstraint3D/CustomConstraint3D_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [Deletable](../CustomConstraint3D/CustomConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [Entity](../CustomConstraint3D/CustomConstraint3D_Entity.md) | Property that returns the entity to which this custom constraint has been applied. |
| [Parent](../CustomConstraint3D/CustomConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../CustomConstraint3D/CustomConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CustomConstraint3DProxy.NativeObject](../CustomConstraint3DProxy/CustomConstraint3DProxy_NativeObject.md), [GeometricConstraints3D.AddCustom](../GeometricConstraints3D/GeometricConstraints3D_AddCustom.md)

## Derived Classes

[CustomConstraint3DProxy](../CustomConstraint3DProxy/CustomConstraint3DProxy.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |