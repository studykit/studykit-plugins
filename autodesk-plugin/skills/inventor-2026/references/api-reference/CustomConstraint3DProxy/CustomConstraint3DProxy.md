# CustomConstraint3DProxy Object

Derived from: [CustomConstraint3D](../CustomConstraint3D/CustomConstraint3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CustomConstraint3DProxy/CustomConstraint3DProxy_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../CustomConstraint3DProxy/CustomConstraint3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CustomConstraint3DProxy/CustomConstraint3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CustomConstraint3DProxy/CustomConstraint3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ClientId](../CustomConstraint3DProxy/CustomConstraint3DProxy_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [ContainingOccurrence](../CustomConstraint3DProxy/CustomConstraint3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../CustomConstraint3DProxy/CustomConstraint3DProxy_Deletable.md) | Indicates whether this object can be deleted. |
| [Entity](../CustomConstraint3DProxy/CustomConstraint3DProxy_Entity.md) | Property that returns the entity to which this custom constraint has been applied. |
| [NativeObject](../CustomConstraint3DProxy/CustomConstraint3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../CustomConstraint3DProxy/CustomConstraint3DProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../CustomConstraint3DProxy/CustomConstraint3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 11
