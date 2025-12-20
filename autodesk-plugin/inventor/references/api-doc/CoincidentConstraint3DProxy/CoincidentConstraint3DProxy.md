# CoincidentConstraint3DProxy Object

Derived from: [CoincidentConstraint3D](../CoincidentConstraint3D/CoincidentConstraint3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [Disconnect](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_Disconnect.md) | Method that disconnects the input entity from the coincident constraint. Valid inputs are SketchPoint, Vertex or WorkPoint. |
| [GetReferenceKey](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConnectedEntity](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_ConnectedEntity.md) | Property that returns the entity connected to this constraint. This can be a SketchPoint, Vertex or a WorkPoint. This property returns Nothing in the case where there isn't a connected entity. |
| [ContainingOccurrence](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_EntityOne.md) | Property that returns the first entity being constrained. This can be a SketchPoint3D, SketchLine3D, WorkPlane or a Face. |
| [EntityTwo](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_EntityTwo.md) | Property that returns the second entity being constrained. This can be a SketchPoint3D, SketchLine3D, WorkPlane or a Face. |
| [NativeObject](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |