# HorizontalConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The HorizontalConstraint object represents a horizontal constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../HorizontalConstraint/HorizontalConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../HorizontalConstraint/HorizontalConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HorizontalConstraint/HorizontalConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../HorizontalConstraint/HorizontalConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../HorizontalConstraint/HorizontalConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [Entity](../HorizontalConstraint/HorizontalConstraint_Entity.md) | Property that returns the sketch entity being constrained. This can be a sketch line, ellipse, or elliptical arc. |
| [Parent](../HorizontalConstraint/HorizontalConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../HorizontalConstraint/HorizontalConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseMajorAxis](../HorizontalConstraint/HorizontalConstraint_UseEllipseMajorAxis.md) | Property used in the case where the entity returned by the Entity property is an ellipse. This property specifies if the major or minor axis of the ellipse is horizontal. True if it is the major axis. |

## Accessed From

[GeometricConstraints.AddHorizontal](../GeometricConstraints/GeometricConstraints_AddHorizontal.md), [HorizontalConstraintProxy.NativeObject](../HorizontalConstraintProxy/HorizontalConstraintProxy_NativeObject.md)

## Derived Classes

[HorizontalConstraintProxy](../HorizontalConstraintProxy/HorizontalConstraintProxy.md)

## Version

Introduced in version 5
