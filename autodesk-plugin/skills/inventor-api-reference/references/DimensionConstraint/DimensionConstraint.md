# DimensionConstraint Object

## Description

The DimensionConstraint object represents the base class of all dimension constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DimensionConstraint/DimensionConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../DimensionConstraint/DimensionConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../DimensionConstraint/DimensionConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../DimensionConstraint/DimensionConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DimensionConstraint/DimensionConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../DimensionConstraint/DimensionConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../DimensionConstraint/DimensionConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Parameter](../DimensionConstraint/DimensionConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../DimensionConstraint/DimensionConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../DimensionConstraint/DimensionConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../DimensionConstraint/DimensionConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AngularGeneralDimension.PromoteToSketch](../AngularGeneralDimension/AngularGeneralDimension_PromoteToSketch.md), [DiameterGeneralDimension.PromoteToSketch](../DiameterGeneralDimension/DiameterGeneralDimension_PromoteToSketch.md), [DimensionConstraints.Item](../DimensionConstraints/DimensionConstraints_Item.md), [GeneralDimension.PromoteToSketch](../GeneralDimension/GeneralDimension_PromoteToSketch.md), [HoleThreadNote.PromoteToSketch](../HoleThreadNote/HoleThreadNote_PromoteToSketch.md), [LinearGeneralDimension.PromoteToSketch](../LinearGeneralDimension/LinearGeneralDimension_PromoteToSketch.md), [RadiusGeneralDimension.PromoteToSketch](../RadiusGeneralDimension/RadiusGeneralDimension_PromoteToSketch.md)

## Derived Classes

[ArcLengthDimConstraint](../ArcLengthDimConstraint/ArcLengthDimConstraint.md), [DiameterDimConstraint](../DiameterDimConstraint/DiameterDimConstraint.md), [EllipseRadiusDimConstraint](../EllipseRadiusDimConstraint/EllipseRadiusDimConstraint.md), [OffsetDimConstraint](../OffsetDimConstraint/OffsetDimConstraint.md), [OffsetSplineDimConstraint](../OffsetSplineDimConstraint/OffsetSplineDimConstraint.md), [RadiusDimConstraint](../RadiusDimConstraint/RadiusDimConstraint.md), [TangentDistanceDimConstraint](../TangentDistanceDimConstraint/TangentDistanceDimConstraint.md), [ThreePointAngleDimConstraint](../ThreePointAngleDimConstraint/ThreePointAngleDimConstraint.md), [TwoLineAngleDimConstraint](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint.md), [TwoPointDistanceDimConstraint](../TwoPointDistanceDimConstraint/TwoPointDistanceDimConstraint.md)

## Version

Introduced in version 5
