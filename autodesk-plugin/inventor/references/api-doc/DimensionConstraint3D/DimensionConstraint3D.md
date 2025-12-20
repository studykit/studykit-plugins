# DimensionConstraint3D Object

## Description

The DimensionConstraint3D object represents the base class of all 3D sketch dimension constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DimensionConstraint3D/DimensionConstraint3D_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../DimensionConstraint3D/DimensionConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../DimensionConstraint3D/DimensionConstraint3D_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../DimensionConstraint3D/DimensionConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DimensionConstraint3D/DimensionConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionPlane](../DimensionConstraint3D/DimensionConstraint3D_DimensionPlane.md) | Property that returns the transient dimension plane used to place and position the dimension text for this dimension constraint. |
| [Driven](../DimensionConstraint3D/DimensionConstraint3D_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Parameter](../DimensionConstraint3D/DimensionConstraint3D_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../DimensionConstraint3D/DimensionConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../DimensionConstraint3D/DimensionConstraint3D_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../DimensionConstraint3D/DimensionConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints3D.Item](../DimensionConstraints3D/DimensionConstraints3D_Item.md)

## Derived Classes

[LineLengthDimConstraint3D](../LineLengthDimConstraint3D/LineLengthDimConstraint3D.md), [PointAndPlaneDistanceDimConstraint3D](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D.md), [RadiusDimConstraint3D](../RadiusDimConstraint3D/RadiusDimConstraint3D.md), [SplineLengthDimConstraint3D](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D.md), [TwoLineAngleDimConstraint3D](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D.md), [TwoPointDistanceDimConstraint3D](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |