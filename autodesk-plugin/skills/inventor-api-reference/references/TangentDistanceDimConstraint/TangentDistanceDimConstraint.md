# TangentDistanceDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The TangentDistanceDimConstraint object represents a constraint that controls the distance to a circle or arc at the tangent location.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [EntityOne](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_EntityOne.md) | Property that returns the first circle or line being constrained. |
| [EntityTwo](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_EntityTwo.md) | Property that returns the second circle or line being constrained. |
| [LinearDiameter](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_LinearDiameter.md) | Property that returns whether the dimension is a linear diameter style of dimension. Returns True if it is a linear diameter dimension. |
| [Parameter](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [ProximityPointOne](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_ProximityPointOne.md) | The point supplied by this argument is used when EntityOne is a circle or arc. This point specifies which of the possible two tangent cases is used when creating the constraint. The closest tangent to the input point is used. If EntityOne is a line, this argument is ignored. |
| [ProximityPointTwo](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_ProximityPointTwo.md) | The point supplied by this argument is used when EntityTwo is a circle or arc. This point specifies which of the possible two tangent cases is used when creating the constraint. The closest tangent to the input point is used. If EntityTwo is a line, this argument is ignored. |
| [TextPoint](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../TangentDistanceDimConstraint/TangentDistanceDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints.AddTangentDistance](../DimensionConstraints/DimensionConstraints_AddTangentDistance.md), [TangentDistanceDimConstraintProxy.NativeObject](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy_NativeObject.md)

## Derived Classes

[TangentDistanceDimConstraintProxy](../TangentDistanceDimConstraintProxy/TangentDistanceDimConstraintProxy.md)

## Version

Introduced in version 5
