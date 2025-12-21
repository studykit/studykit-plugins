# DimensionConstraints3D Object

## Description

The DimensionConstraints3D object provides access to all the dimension sketch constraints in a 3D sketch and provides methods to create additional dimension sketch constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddLineLength](../DimensionConstraints3D/DimensionConstraints3D_AddLineLength.md) | Method that creates a new linear dimension constraint that defines the length of a 3D sketch line. This method will fail in the case where a driving dimension is specified and it will overconstrain the sketch. |
| [AddPointAndPlaneDistance](../DimensionConstraints3D/DimensionConstraints3D_AddPointAndPlaneDistance.md) | Method that creates a new linear dimension constraint between a 3D sketch point and a planar face or workplane. This method will fail if the input 3D sketch point lies on the input plane specified by the face or workplane. This method will also fail in the case where a driving dimension is specified and it will overconstrain the sketch. |
| [AddRadius](../DimensionConstraints3D/DimensionConstraints3D_AddRadius.md) | Method that creates a new radius dimension constraint on the input circle or arc. |
| [AddSplineLength](../DimensionConstraints3D/DimensionConstraints3D_AddSplineLength.md) | Method that creates a new spline length dimension constraint that defines the length of a 3D sketch spline. |
| [AddTwoLineAngle](../DimensionConstraints3D/DimensionConstraints3D_AddTwoLineAngle.md) | Method that creates a new angular dimension constraint between two 3D sketch lines. This method will fail if the two input 3D sketch lines that need to be constrained are not co-planar. This method will also fail in the case where a driving dimension is specified and it will overconstrain the sketch. |
| [AddTwoPointDistance](../DimensionConstraints3D/DimensionConstraints3D_AddTwoPointDistance.md) | Method that creates a new linear dimension constraint between a 3D sketch point and another 3D sketch point, vertex or workpoint. This method will fail in the case where a driving dimension is specified and it will overconstrain the sketch. |
| [GetDimensionPlane](../DimensionConstraints3D/DimensionConstraints3D_GetDimensionPlane.md) | Method that gets the transient dimension plane used to place and position the dimension text when a dimension constraint is applied to the specified input entities. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DimensionConstraints3D/DimensionConstraints3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../DimensionConstraints3D/DimensionConstraints3D_Count.md) | Property that specifies the number of items in the collection. |
| [Item](../DimensionConstraints3D/DimensionConstraints3D_Item.md) | Returns the specified 3D sketch dimension constraint object from the collection. |
| [Type](../DimensionConstraints3D/DimensionConstraints3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sketch3D.DimensionConstraints3D](../Sketch3D/Sketch3D_DimensionConstraints3D.md), [Sketch3DProxy.DimensionConstraints3D](../Sketch3DProxy/Sketch3DProxy_DimensionConstraints3D.md)

## Version

Introduced in version 11
