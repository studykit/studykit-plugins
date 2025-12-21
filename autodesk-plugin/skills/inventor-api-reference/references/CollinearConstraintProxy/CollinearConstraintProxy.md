# CollinearConstraintProxy Object

Derived from: [CollinearConstraint](../CollinearConstraint/CollinearConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CollinearConstraintProxy/CollinearConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../CollinearConstraintProxy/CollinearConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CollinearConstraintProxy/CollinearConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CollinearConstraintProxy/CollinearConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../CollinearConstraintProxy/CollinearConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../CollinearConstraintProxy/CollinearConstraintProxy_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../CollinearConstraintProxy/CollinearConstraintProxy_EntityOne.md) | Property that returns the first sketch entity being constrained. |
| [EntityTwo](../CollinearConstraintProxy/CollinearConstraintProxy_EntityTwo.md) | Property that returns the second sketch entity being constrained. |
| [NativeObject](../CollinearConstraintProxy/CollinearConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../CollinearConstraintProxy/CollinearConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../CollinearConstraintProxy/CollinearConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseOneMajorAxis](../CollinearConstraintProxy/CollinearConstraintProxy_UseEllipseOneMajorAxis.md) | Property used in the case where the entity returned by the EntityOne property is an ellipse. This property specifies if the major or minor axis of the ellipse is collinear to EntityTwo. True if it is the major axis. |
| [UseEllipseTwoMajorAxis](../CollinearConstraintProxy/CollinearConstraintProxy_UseEllipseTwoMajorAxis.md) | Property used in the case where the entity returned by the EntityTwo property is an ellipse. This property specifies if the major or minor axis of the ellipse is collinear to EntityOne. True if it is the major axis. |

## Version

Introduced in version 6
