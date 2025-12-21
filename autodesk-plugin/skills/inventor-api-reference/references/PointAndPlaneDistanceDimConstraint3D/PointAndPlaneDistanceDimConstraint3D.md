# PointAndPlaneDistanceDimConstraint3D Object

Derived from: [DimensionConstraint3D](../DimensionConstraint3D/DimensionConstraint3D.md) Object

## Description

The PointAndPlaneDistanceDimConstraint3D object represents a constraint that controls the distance between a 3D sketch point and a planar face or workplane.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionPlane](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_DimensionPlane.md) | Property that returns the transient dimension plane used to place and position the dimension text for this dimension constraint. |
| [Driven](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Parameter](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Plane](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Plane.md) | Property that returns the planar Face or WorkPlane object that defines the distance to the 3D sketch point being constrained. |
| [Point](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Point.md) | Property that returns the 3D sketch point being constrained. |
| [TextPoint](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints3D.AddPointAndPlaneDistance](../DimensionConstraints3D/DimensionConstraints3D_AddPointAndPlaneDistance.md), [PointAndPlaneDistanceDimConstraint3DProxy.NativeObject](../PointAndPlaneDistanceDimConstraint3DProxy/PointAndPlaneDistanceDimConstraint3DProxy_NativeObject.md)

## Derived Classes

[PointAndPlaneDistanceDimConstraint3DProxy](../PointAndPlaneDistanceDimConstraint3DProxy/PointAndPlaneDistanceDimConstraint3DProxy.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |