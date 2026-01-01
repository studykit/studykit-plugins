# TangentConstraint3DProxy Object

Derived from: [TangentConstraint3D](../TangentConstraint3D/TangentConstraint3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TangentConstraint3DProxy/TangentConstraint3DProxy_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [FlipDirection](../TangentConstraint3DProxy/TangentConstraint3DProxy_FlipDirection.md) | Flips the direction of the tangency between the two 3D entities. |
| [GetReferenceKey](../TangentConstraint3DProxy/TangentConstraint3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TangentConstraint3DProxy/TangentConstraint3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TangentConstraint3DProxy/TangentConstraint3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../TangentConstraint3DProxy/TangentConstraint3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../TangentConstraint3DProxy/TangentConstraint3DProxy_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../TangentConstraint3DProxy/TangentConstraint3DProxy_EntityOne.md) | Property that returns the sketch entity that is constrained to be tangent to entity two. |
| [EntityTwo](../TangentConstraint3DProxy/TangentConstraint3DProxy_EntityTwo.md) | Property that returns the sketch entity that is constrained to be tangent to entity one. |
| [NativeObject](../TangentConstraint3DProxy/TangentConstraint3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../TangentConstraint3DProxy/TangentConstraint3DProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../TangentConstraint3DProxy/TangentConstraint3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 8
