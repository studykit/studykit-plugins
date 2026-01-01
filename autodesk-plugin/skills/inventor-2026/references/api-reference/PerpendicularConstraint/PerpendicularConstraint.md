# PerpendicularConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The PerpendicularConstraint object represents a perpendicular constraint within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../PerpendicularConstraint/PerpendicularConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../PerpendicularConstraint/PerpendicularConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PerpendicularConstraint/PerpendicularConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PerpendicularConstraint/PerpendicularConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../PerpendicularConstraint/PerpendicularConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [EntityOne](../PerpendicularConstraint/PerpendicularConstraint_EntityOne.md) | Property that returns the sketch entity being constrained. This will be a line, ellipse, or elliptical arc. In the case where an elliptical entity is returned, the UsesEllipseOneMajorAxis property indicates if the perpendicular constraint is between the major or minor axis of the ellipse. |
| [EntityTwo](../PerpendicularConstraint/PerpendicularConstraint_EntityTwo.md) | Property that returns the sketch entity being constrained. This will be a line, ellipse, or elliptical arc. In the case where an elliptical entity is returned, the UsesEllipseTwoMajorAxis property indicates if the perpendicular constraint is between the major or minor axis of the ellipse. |
| [Parent](../PerpendicularConstraint/PerpendicularConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../PerpendicularConstraint/PerpendicularConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseEllipseOneMajorAxis](../PerpendicularConstraint/PerpendicularConstraint_UseEllipseOneMajorAxis.md) | Property used in the case where the entity returned by the EntityOne property is an ellipse. This property specifies if the major or minor axis of the ellipse is perpendicular to EntityTwo. True if it is the major axis. |
| [UseEllipseTwoMajorAxis](../PerpendicularConstraint/PerpendicularConstraint_UseEllipseTwoMajorAxis.md) | Property used in the case where the entity returned by the EntityTwo property is an ellipse. This property specifies if the major or minor axis of the ellipse is perpendicular to EntityOne. True if it is the major axis. |

## Accessed From

[GeometricConstraints.AddPerpendicular](../GeometricConstraints/GeometricConstraints_AddPerpendicular.md), [PerpendicularConstraintProxy.NativeObject](../PerpendicularConstraintProxy/PerpendicularConstraintProxy_NativeObject.md)

## Derived Classes

[PerpendicularConstraintProxy](../PerpendicularConstraintProxy/PerpendicularConstraintProxy.md)

## Version

Introduced in version 5
