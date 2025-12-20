# OffsetSplineDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The OffsetSplineDimConstraint is automatically created when offset spline dimensions are created. The OffsetDimConstraint object represents a constraint that controls the distance between two parallel lines or a line and a point. This constraint cannot be explicitly deleted.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [OffsetSpline](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_OffsetSpline.md) | Gets the SketchOffsetSpline being constrained to. |
| [Parameter](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [Spline](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_Spline.md) | Gets the SketchSpline being constrained. |
| [TextPoint](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints.AddOffsetSpline](../DimensionConstraints/DimensionConstraints_AddOffsetSpline.md), [OffsetSplineDimConstraintProxy.NativeObject](../OffsetSplineDimConstraintProxy/OffsetSplineDimConstraintProxy_NativeObject.md)

## Derived Classes

[OffsetSplineDimConstraintProxy](../OffsetSplineDimConstraintProxy/OffsetSplineDimConstraintProxy.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |