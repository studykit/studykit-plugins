# SplineLengthDimConstraint3D Object

Derived from: [DimensionConstraint3D](../DimensionConstraint3D/DimensionConstraint3D.md) Object

## Description

SplineLengthDimConstraint3D Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionPlane](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_DimensionPlane.md) | Property that returns the transient dimension plane used to place and position the dimension text for this dimension constraint. |
| [Driven](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Parameter](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Spline](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_Spline.md) | Returns the 3D sketch spline being constrained. |
| [TextPoint](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints3D.AddSplineLength](../DimensionConstraints3D/DimensionConstraints3D_AddSplineLength.md), [SplineLengthDimConstraint3DProxy.NativeObject](../SplineLengthDimConstraint3DProxy/SplineLengthDimConstraint3DProxy_NativeObject.md)

## Derived Classes

[SplineLengthDimConstraint3DProxy](../SplineLengthDimConstraint3DProxy/SplineLengthDimConstraint3DProxy.md)

## Version

Introduced in version 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |