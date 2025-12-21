# VerticalConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The VerticalConstraint object represents a vertical constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../VerticalConstraint/VerticalConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../VerticalConstraint/VerticalConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../VerticalConstraint/VerticalConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../VerticalConstraint/VerticalConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../VerticalConstraint/VerticalConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [Entity](../VerticalConstraint/VerticalConstraint_Entity.md) | Property that returns the sketch entity being constrained. This can be a sketch line, ellipse, or elliptical arc. |
| [Parent](../VerticalConstraint/VerticalConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../VerticalConstraint/VerticalConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseMajorAxis](../VerticalConstraint/VerticalConstraint_UseEllipseMajorAxis.md) | Property used in the case where the entity returned by the Entity property is an ellipse. This property specifies if the major or minor axis of the ellipse is vertical. True if it is the major axis. |

## Accessed From

[GeometricConstraints.AddVertical](../GeometricConstraints/GeometricConstraints_AddVertical.md), [VerticalConstraintProxy.NativeObject](../VerticalConstraintProxy/VerticalConstraintProxy_NativeObject.md)

## Derived Classes

[VerticalConstraintProxy](../VerticalConstraintProxy/VerticalConstraintProxy.md)

## Version

Introduced in version 5
