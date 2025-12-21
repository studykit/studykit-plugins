# TwoPointDistanceDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The TwoPointDistanceDimConstraint object represents a constraint that controls the distance between two points. The vertical, horizontal, or true distance can be controlled.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Orientation](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_Orientation.md) | Property that indicates an enum indicating if the constraint is controlling the horizontal, vertical, or true distance between the points. |
| [Parameter](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [PointOne](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_PointOne.md) | Property that returns the first sketch point being constrained. |
| [PointTwo](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_PointTwo.md) | Property that returns the second sketch point being constrained. |
| [TextPoint](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints.AddTwoPointDistance](../DimensionConstraints/DimensionConstraints_AddTwoPointDistance.md), [TwoPointDistanceDimConstraintProxy.NativeObject](../TwoPointDistanceDimConstraintProxy/TwoPointDistanceDimConstraintProxy_NativeObject.md)

## Derived Classes

[TwoPointDistanceDimConstraintProxy](../TwoPointDistanceDimConstraintProxy/TwoPointDistanceDimConstraintProxy.md)

## Version

Introduced in version 5
