# HorizontalConstraintProxy Object

Derived from: [HorizontalConstraint](../HorizontalConstraint/HorizontalConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../HorizontalConstraintProxy/HorizontalConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../HorizontalConstraintProxy/HorizontalConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HorizontalConstraintProxy/HorizontalConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../HorizontalConstraintProxy/HorizontalConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../HorizontalConstraintProxy/HorizontalConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../HorizontalConstraintProxy/HorizontalConstraintProxy_Deletable.md) | Indicates whether this object is deletable. |
| [Entity](../HorizontalConstraintProxy/HorizontalConstraintProxy_Entity.md) | Property that returns the sketch entity being constrained. This can be a sketch line, ellipse, or elliptical arc. |
| [NativeObject](../HorizontalConstraintProxy/HorizontalConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../HorizontalConstraintProxy/HorizontalConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../HorizontalConstraintProxy/HorizontalConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseMajorAxis](../HorizontalConstraintProxy/HorizontalConstraintProxy_UseEllipseMajorAxis.md) | Property used in the case where the entity returned by the Entity property is an ellipse. This property specifies if the major or minor axis of the ellipse is horizontal. True if it is the major axis. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |