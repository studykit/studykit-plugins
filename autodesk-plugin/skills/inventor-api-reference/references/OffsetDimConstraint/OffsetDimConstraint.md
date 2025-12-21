# OffsetDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

The OffsetDimConstraint object represents a constraint that controls the distance between two parallel lines or a line and a point.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../OffsetDimConstraint/OffsetDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../OffsetDimConstraint/OffsetDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../OffsetDimConstraint/OffsetDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../OffsetDimConstraint/OffsetDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../OffsetDimConstraint/OffsetDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../OffsetDimConstraint/OffsetDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../OffsetDimConstraint/OffsetDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../OffsetDimConstraint/OffsetDimConstraint_Entity.md) | Property that returns the circle or arc being constrained. |
| [Line](../OffsetDimConstraint/OffsetDimConstraint_Line.md) | Property that returns the proxy SketchLine being constrained. |
| [LinearDiameter](../OffsetDimConstraint/OffsetDimConstraint_LinearDiameter.md) | Property that returns whether the dimension is a linear diameter style of dimension. |
| [Parameter](../OffsetDimConstraint/OffsetDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../OffsetDimConstraint/OffsetDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../OffsetDimConstraint/OffsetDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../OffsetDimConstraint/OffsetDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints.AddOffset](../DimensionConstraints/DimensionConstraints_AddOffset.md), [OffsetDimConstraintProxy.NativeObject](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_NativeObject.md)

## Derived Classes

[OffsetDimConstraintProxy](../OffsetDimConstraintProxy/OffsetDimConstraintProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |