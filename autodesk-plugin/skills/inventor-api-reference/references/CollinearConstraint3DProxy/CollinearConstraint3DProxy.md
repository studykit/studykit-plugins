# CollinearConstraint3DProxy Object

Derived from: [CollinearConstraint3D](../CollinearConstraint3D/CollinearConstraint3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_EntityOne.md) | Property that returns the first entity being constrained. This can either be a SketchLine3D or a WorkAxis. |
| [EntityTwo](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_EntityTwo.md) | Property that returns the second entity being constrained. This can either be a SketchLine3D or a WorkAxis. |
| [NativeObject](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../CollinearConstraint3DProxy/CollinearConstraint3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |