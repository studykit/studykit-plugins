# CoincidentConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The CoincidentConstraint3D object represents a coincident constraint within a 3D sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CoincidentConstraint3D/CoincidentConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [Disconnect](../CoincidentConstraint3D/CoincidentConstraint3D_Disconnect.md) | Method that disconnects the input entity from the coincident constraint. Valid inputs are SketchPoint, Vertex or WorkPoint. |
| [GetReferenceKey](../CoincidentConstraint3D/CoincidentConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CoincidentConstraint3D/CoincidentConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CoincidentConstraint3D/CoincidentConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConnectedEntity](../CoincidentConstraint3D/CoincidentConstraint3D_ConnectedEntity.md) | Property that returns the entity connected to this constraint. This can be a SketchPoint, Vertex or a WorkPoint. This property returns Nothing in the case where there isn't a connected entity. |
| [Deletable](../CoincidentConstraint3D/CoincidentConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [EntityOne](../CoincidentConstraint3D/CoincidentConstraint3D_EntityOne.md) | Property that returns the first entity being constrained. This can be a SketchPoint3D, SketchLine3D, WorkPlane or a Face. |
| [EntityTwo](../CoincidentConstraint3D/CoincidentConstraint3D_EntityTwo.md) | Property that returns the second entity being constrained. This can be a SketchPoint3D, SketchLine3D, WorkPlane or a Face. |
| [Parent](../CoincidentConstraint3D/CoincidentConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../CoincidentConstraint3D/CoincidentConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CoincidentConstraint3DProxy.NativeObject](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy_NativeObject.md), [GeometricConstraints3D.AddCoincident](../GeometricConstraints3D/GeometricConstraints3D_AddCoincident.md)

## Derived Classes

[CoincidentConstraint3DProxy](../CoincidentConstraint3DProxy/CoincidentConstraint3DProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |