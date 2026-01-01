# SplineFitPointConstraint Object

Derived from: [GeometricConstraint](../GeometricConstraint/GeometricConstraint.md) Object

## Description

The SplineFitPointConstraint object represents a constraint that makes a spline fit through a specified sketch point. This constraint is created automatically when a spline is created or when new fit points are added to a spline.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SplineFitPointConstraint/SplineFitPointConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../SplineFitPointConstraint/SplineFitPointConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SplineFitPointConstraint/SplineFitPointConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SplineFitPointConstraint/SplineFitPointConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../SplineFitPointConstraint/SplineFitPointConstraint_Deletable.md) | Indicates whether this object is deletable. |
| [Parent](../SplineFitPointConstraint/SplineFitPointConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Point](../SplineFitPointConstraint/SplineFitPointConstraint_Point.md) | Property that returns the sketch point the spline is fit through. |
| [Spline](../SplineFitPointConstraint/SplineFitPointConstraint_Spline.md) | Property that returns the spline entity being constrained. |
| [Type](../SplineFitPointConstraint/SplineFitPointConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SplineFitPointConstraintProxy.NativeObject](../SplineFitPointConstraintProxy/SplineFitPointConstraintProxy_NativeObject.md)

## Derived Classes

[SplineFitPointConstraintProxy](../SplineFitPointConstraintProxy/SplineFitPointConstraintProxy.md)

## Version

Introduced in version 5
