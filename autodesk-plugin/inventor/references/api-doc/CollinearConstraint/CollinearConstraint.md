# CollinearConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The CollinearConstraint object represents a collinear constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CollinearConstraint/CollinearConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../CollinearConstraint/CollinearConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CollinearConstraint/CollinearConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CollinearConstraint/CollinearConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../CollinearConstraint/CollinearConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../CollinearConstraint/CollinearConstraint_EntityOne.md) | Property that returns the first sketch entity being constrained. |
| [EntityTwo](../CollinearConstraint/CollinearConstraint_EntityTwo.md) | Property that returns the second sketch entity being constrained. |
| [Parent](../CollinearConstraint/CollinearConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../CollinearConstraint/CollinearConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseOneMajorAxis](../CollinearConstraint/CollinearConstraint_UseEllipseOneMajorAxis.md) | Property used in the case where the entity returned by the EntityOne property is an ellipse. This property specifies if the major or minor axis of the ellipse is collinear to EntityTwo. True if it is the major axis. |
| [UseEllipseTwoMajorAxis](../CollinearConstraint/CollinearConstraint_UseEllipseTwoMajorAxis.md) | Property used in the case where the entity returned by the EntityTwo property is an ellipse. This property specifies if the major or minor axis of the ellipse is collinear to EntityOne. True if it is the major axis. |

## Accessed From

[CollinearConstraintProxy.NativeObject](../CollinearConstraintProxy/CollinearConstraintProxy_NativeObject.md), [GeometricConstraints.AddCollinear](../GeometricConstraints/GeometricConstraints_AddCollinear.md)

## Derived Classes

[CollinearConstraintProxy](../CollinearConstraintProxy/CollinearConstraintProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |