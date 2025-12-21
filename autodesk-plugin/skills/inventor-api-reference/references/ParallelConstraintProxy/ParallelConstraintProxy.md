# ParallelConstraintProxy Object

Derived from: [ParallelConstraint](../ParallelConstraint/ParallelConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ParallelConstraintProxy/ParallelConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../ParallelConstraintProxy/ParallelConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ParallelConstraintProxy/ParallelConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ParallelConstraintProxy/ParallelConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../ParallelConstraintProxy/ParallelConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Deletable](../ParallelConstraintProxy/ParallelConstraintProxy_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../ParallelConstraintProxy/ParallelConstraintProxy_EntityOne.md) | Property that returns the sketch entity being constrained. This will be a line, ellipse, or elliptical arc. In the case where an elliptical entity is returned, the UsesEllipseOneMajorAxis property indicates if the parallel constraint is between the major or minor axis of the ellipse. |
| [EntityTwo](../ParallelConstraintProxy/ParallelConstraintProxy_EntityTwo.md) | Property that returns the sketch entity being constrained. This will be a line, ellipse, or elliptical arc. In the case where an elliptical entity is returned, the UsesEllipseTwoMajorAxis property indicates if the parallel constraint is between the major or minor axis of the ellipse. |
| [NativeObject](../ParallelConstraintProxy/ParallelConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../ParallelConstraintProxy/ParallelConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../ParallelConstraintProxy/ParallelConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseOneMajorAxis](../ParallelConstraintProxy/ParallelConstraintProxy_UseEllipseOneMajorAxis.md) | Property used in the case where the entity returned by the EntityOne property is an ellipse. This property specifies if the major or minor axis of the ellipse is parallel to EntityTwo. True if it is the major axis. |
| [UseEllipseTwoMajorAxis](../ParallelConstraintProxy/ParallelConstraintProxy_UseEllipseTwoMajorAxis.md) | Property used in the case where the entity returned by the EntityTwo property is an ellipse. This property specifies if the major or minor axis of the ellipse is parallel to EntityOne. True if it is the major axis. |

## Version

Introduced in version 6
