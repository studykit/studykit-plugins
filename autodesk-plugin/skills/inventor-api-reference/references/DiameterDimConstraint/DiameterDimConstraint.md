# DiameterDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The DiameterDimConstraint object represents a constraint that controls the diameter of a circle or arc.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DiameterDimConstraint/DiameterDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../DiameterDimConstraint/DiameterDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../DiameterDimConstraint/DiameterDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../DiameterDimConstraint/DiameterDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DiameterDimConstraint/DiameterDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../DiameterDimConstraint/DiameterDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../DiameterDimConstraint/DiameterDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../DiameterDimConstraint/DiameterDimConstraint_Entity.md) | Property that returns the circle or arc being constrained. |
| [Parameter](../DiameterDimConstraint/DiameterDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../DiameterDimConstraint/DiameterDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../DiameterDimConstraint/DiameterDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../DiameterDimConstraint/DiameterDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DiameterDimConstraintProxy.NativeObject](../DiameterDimConstraintProxy/DiameterDimConstraintProxy_NativeObject.md), [DimensionConstraints.AddDiameter](../DimensionConstraints/DimensionConstraints_AddDiameter.md)

## Derived Classes

[DiameterDimConstraintProxy](../DiameterDimConstraintProxy/DiameterDimConstraintProxy.md)

## Version

Introduced in version 5
