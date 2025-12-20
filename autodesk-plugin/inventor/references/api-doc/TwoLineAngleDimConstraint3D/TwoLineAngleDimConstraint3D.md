# TwoLineAngleDimConstraint3D Object

Derived from: [DimensionConstraint3D](../DimensionConstraint3D/DimensionConstraint3D.md) Object

## Description

The TwoLineAngleDimConstraint3D object represents a constraint that controls the angle between two 3D sketch lines.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionPlane](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_DimensionPlane.md) | Property that returns the transient dimension plane used to place and position the dimension text for this dimension constraint. |
| [Driven](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [LineOne](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_LineOne.md) | Property that returns the first 3D sketch line being constrained. |
| [LineTwo](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_LineTwo.md) | Property that returns the second 3D sketch line being constrained. |
| [Parameter](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints3D.AddTwoLineAngle](../DimensionConstraints3D/DimensionConstraints3D_AddTwoLineAngle.md), [TwoLineAngleDimConstraint3DProxy.NativeObject](../TwoLineAngleDimConstraint3DProxy/TwoLineAngleDimConstraint3DProxy_NativeObject.md)

## Derived Classes

[TwoLineAngleDimConstraint3DProxy](../TwoLineAngleDimConstraint3DProxy/TwoLineAngleDimConstraint3DProxy.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |