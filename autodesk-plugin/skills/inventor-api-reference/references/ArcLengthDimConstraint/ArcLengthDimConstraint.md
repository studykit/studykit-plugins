# ArcLengthDimConstraint Object

Derived from: [DimensionConstraint](../DimensionConstraint/DimensionConstraint.md) Object

## Description

ArcLengthDimConstraint Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ArcLengthDimConstraint/ArcLengthDimConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../ArcLengthDimConstraint/ArcLengthDimConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../ArcLengthDimConstraint/ArcLengthDimConstraint_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../ArcLengthDimConstraint/ArcLengthDimConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ArcLengthDimConstraint/ArcLengthDimConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionCenterPoint](../ArcLengthDimConstraint/ArcLengthDimConstraint_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../ArcLengthDimConstraint/ArcLengthDimConstraint_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../ArcLengthDimConstraint/ArcLengthDimConstraint_Entity.md) | Gets the SketchArc2d object being constrained. |
| [Parameter](../ArcLengthDimConstraint/ArcLengthDimConstraint_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../ArcLengthDimConstraint/ArcLengthDimConstraint_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../ArcLengthDimConstraint/ArcLengthDimConstraint_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../ArcLengthDimConstraint/ArcLengthDimConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ArcLengthDimConstraintProxy.NativeObject](../ArcLengthDimConstraintProxy/ArcLengthDimConstraintProxy_NativeObject.md), [DimensionConstraints.AddArcLength](../DimensionConstraints/DimensionConstraints_AddArcLength.md)

## Derived Classes

[ArcLengthDimConstraintProxy](../ArcLengthDimConstraintProxy/ArcLengthDimConstraintProxy.md)

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |