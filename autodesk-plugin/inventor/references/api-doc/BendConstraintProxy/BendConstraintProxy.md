# BendConstraintProxy Object

Derived from: [BendConstraint](../BendConstraint/BendConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BendConstraintProxy/BendConstraintProxy_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../BendConstraintProxy/BendConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BendConstraintProxy/BendConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Arc](../BendConstraintProxy/BendConstraintProxy_Arc.md) | Property that returns the SketchArc3D object associated with the bend. |
| [AttributeSets](../BendConstraintProxy/BendConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../BendConstraintProxy/BendConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../BendConstraintProxy/BendConstraintProxy_Deletable.md) | Indicates whether this object can be deleted. |
| [LineOne](../BendConstraintProxy/BendConstraintProxy_LineOne.md) | Property that returns the Sketch Line used to construct the bend feature. |
| [LineTwo](../BendConstraintProxy/BendConstraintProxy_LineTwo.md) | Property that returns the Sketch Line used to construct the bend feature. |
| [NativeObject](../BendConstraintProxy/BendConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../BendConstraintProxy/BendConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Radius](../BendConstraintProxy/BendConstraintProxy_Radius.md) | Property that returns the parameter controlling the radius of the bend. |
| [Type](../BendConstraintProxy/BendConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |