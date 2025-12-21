# ThreePointAngleDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The ThreePointAngleDimConstraint object represents a constraint that controls the angle defined by three points.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Parameter](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [PointOne](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_PointOne.md) | Property that returns the first sketch point being constrained. |
| [PointThree](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_PointThree.md) | Property that returns the third sketch point being constrained. |
| [PointTwo](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_PointTwo.md) | Property that returns the second sketch point being constrained. |
| [TextPoint](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints.AddThreePointAngle](../DimensionConstraints/DimensionConstraints_AddThreePointAngle.md), [ThreePointAngleDimConstraintProxy.NativeObject](../ThreePointAngleDimConstraintProxy/ThreePointAngleDimConstraintProxy_NativeObject.md)

## Derived Classes

[ThreePointAngleDimConstraintProxy](../ThreePointAngleDimConstraintProxy/ThreePointAngleDimConstraintProxy.md)

## Version

Introduced in version 5
