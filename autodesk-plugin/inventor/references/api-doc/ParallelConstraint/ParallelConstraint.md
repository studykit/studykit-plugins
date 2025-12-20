# ParallelConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The ParallelConstraint object represents a parallel constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ParallelConstraint/ParallelConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../ParallelConstraint/ParallelConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ParallelConstraint/ParallelConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ParallelConstraint/ParallelConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../ParallelConstraint/ParallelConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../ParallelConstraint/ParallelConstraint_EntityOne.md) | Property that returns the sketch entity being constrained. This will be a line, ellipse, or elliptical arc. In the case where an elliptical entity is returned, the UsesEllipseOneMajorAxis property indicates if the parallel constraint is between the major or minor axis of the ellipse. |
| [EntityTwo](../ParallelConstraint/ParallelConstraint_EntityTwo.md) | Property that returns the sketch entity being constrained. This will be a line, ellipse, or elliptical arc. In the case where an elliptical entity is returned, the UsesEllipseTwoMajorAxis property indicates if the parallel constraint is between the major or minor axis of the ellipse. |
| [Parent](../ParallelConstraint/ParallelConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../ParallelConstraint/ParallelConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseOneMajorAxis](../ParallelConstraint/ParallelConstraint_UseEllipseOneMajorAxis.md) | Property used in the case where the entity returned by the EntityOne property is an ellipse. This property specifies if the major or minor axis of the ellipse is parallel to EntityTwo. True if it is the major axis. |
| [UseEllipseTwoMajorAxis](../ParallelConstraint/ParallelConstraint_UseEllipseTwoMajorAxis.md) | Property used in the case where the entity returned by the EntityTwo property is an ellipse. This property specifies if the major or minor axis of the ellipse is parallel to EntityOne. True if it is the major axis. |

## Accessed From

[GeometricConstraints.AddParallel](../GeometricConstraints/GeometricConstraints_AddParallel.md), [ParallelConstraintProxy.NativeObject](../ParallelConstraintProxy/ParallelConstraintProxy_NativeObject.md)

## Derived Classes

[ParallelConstraintProxy](../ParallelConstraintProxy/ParallelConstraintProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |