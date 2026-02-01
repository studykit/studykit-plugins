# VerticalConstraintProxy Object

Derived from: [VerticalConstraint](../VerticalConstraint/VerticalConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../VerticalConstraintProxy/VerticalConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../VerticalConstraintProxy/VerticalConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../VerticalConstraintProxy/VerticalConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../VerticalConstraintProxy/VerticalConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../VerticalConstraintProxy/VerticalConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../VerticalConstraintProxy/VerticalConstraintProxy_Deletable.md) | Indicates whether this object is deletable. |
| [Entity](../VerticalConstraintProxy/VerticalConstraintProxy_Entity.md) | Property that returns the sketch entity being constrained. This can be a sketch line, ellipse, or elliptical arc. |
| [NativeObject](../VerticalConstraintProxy/VerticalConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../VerticalConstraintProxy/VerticalConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../VerticalConstraintProxy/VerticalConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseMajorAxis](../VerticalConstraintProxy/VerticalConstraintProxy_UseEllipseMajorAxis.md) | Property used in the case where the entity returned by the Entity property is an ellipse. This property specifies if the major or minor axis of the ellipse is vertical. True if it is the major axis. |

## Version

Introduced in version 6
