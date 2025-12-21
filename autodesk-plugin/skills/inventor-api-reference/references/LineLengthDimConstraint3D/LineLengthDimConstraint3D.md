# LineLengthDimConstraint3D Object

Derived from: [DimensionConstraint3D](../DimensionConstraint3D/DimensionConstraint3D.md) Object

## Description

The LineLengthDimConstraint3D object represents a constraint that controls the length of a 3D sketch line.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionPlane](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_DimensionPlane.md) | Property that returns the transient dimension plane used to place and position the dimension text for this dimension constraint. |
| [Driven](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Line](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_Line.md) | Property that returns the 3D sketch line being constrained. |
| [Parameter](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints3D.AddLineLength](../DimensionConstraints3D/DimensionConstraints3D_AddLineLength.md), [LineLengthDimConstraint3DProxy.NativeObject](../LineLengthDimConstraint3DProxy/LineLengthDimConstraint3DProxy_NativeObject.md)

## Derived Classes

[LineLengthDimConstraint3DProxy](../LineLengthDimConstraint3DProxy/LineLengthDimConstraint3DProxy.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |