# TwoPointDistanceDimConstraint3D Object

Derived from: [DimensionConstraint3D](../DimensionConstraint3D/DimensionConstraint3D.md) Object

## Description

The TwoPointDistanceDimConstraint3D object represents a constraint that controls the distance between two 3D sketch points.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionPlane](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_DimensionPlane.md) | Property that returns the transient dimension plane used to place and position the dimension text for this dimension constraint. |
| [Driven](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Parameter](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [PointOne](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_PointOne.md) | Property that returns the SketchPoint3D object that defines the first point being constrained. |
| [PointTwo](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_PointTwo.md) | Property that returns the SketchPoint3D object that defines the second point being constrained. |
| [TextPoint](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints3D.AddTwoPointDistance](../DimensionConstraints3D/DimensionConstraints3D_AddTwoPointDistance.md), [TwoPointDistanceDimConstraint3DProxy.NativeObject](../TwoPointDistanceDimConstraint3DProxy/TwoPointDistanceDimConstraint3DProxy_NativeObject.md)

## Derived Classes

[TwoPointDistanceDimConstraint3DProxy](../TwoPointDistanceDimConstraint3DProxy/TwoPointDistanceDimConstraint3DProxy.md)

## Version

Introduced in version 11
