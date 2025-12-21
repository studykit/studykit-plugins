# TwoLineAngleDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The TwoLineAngleDimConstraint object represents a constraint that controls the angle between two lines.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [LineOne](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_LineOne.md) | Property that returns the first sketch line being constrained. |
| [LineTwo](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_LineTwo.md) | Property that returns the second sketch line being constrained. |
| [Parameter](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints.AddTwoLineAngle](../DimensionConstraints/DimensionConstraints_AddTwoLineAngle.md), [TwoLineAngleDimConstraintProxy.NativeObject](../TwoLineAngleDimConstraintProxy/TwoLineAngleDimConstraintProxy_NativeObject.md)

## Derived Classes

[TwoLineAngleDimConstraintProxy](../TwoLineAngleDimConstraintProxy/TwoLineAngleDimConstraintProxy.md)

## Version

Introduced in version 5
