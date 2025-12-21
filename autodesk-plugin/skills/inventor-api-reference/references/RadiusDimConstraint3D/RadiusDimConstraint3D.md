# RadiusDimConstraint3D Object

Derived from: [DimensionConstraint3D](../DimensionConstraint3D/DimensionConstraint3D.md) Object

## Description

The RadiusDimConstraint3D object represents a constraint that controls the radius of a circle or an arc. The picture below illustrates the use of this constraint.

![](../images/RadiusDimConstraint.png)

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RadiusDimConstraint3D/RadiusDimConstraint3D_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../RadiusDimConstraint3D/RadiusDimConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../RadiusDimConstraint3D/RadiusDimConstraint3D_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../RadiusDimConstraint3D/RadiusDimConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RadiusDimConstraint3D/RadiusDimConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionPlane](../RadiusDimConstraint3D/RadiusDimConstraint3D_DimensionPlane.md) | Property that returns the transient dimension plane used to place and position the dimension text for this dimension constraint. |
| [Driven](../RadiusDimConstraint3D/RadiusDimConstraint3D_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../RadiusDimConstraint3D/RadiusDimConstraint3D_Entity.md) | Property that returns the circle or arc being constrained. |
| [Parameter](../RadiusDimConstraint3D/RadiusDimConstraint3D_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../RadiusDimConstraint3D/RadiusDimConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../RadiusDimConstraint3D/RadiusDimConstraint3D_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../RadiusDimConstraint3D/RadiusDimConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DimensionConstraints3D.AddRadius](../DimensionConstraints3D/DimensionConstraints3D_AddRadius.md), [RadiusDimConstraint3DProxy.NativeObject](../RadiusDimConstraint3DProxy/RadiusDimConstraint3DProxy_NativeObject.md)

## Derived Classes

[RadiusDimConstraint3DProxy](../RadiusDimConstraint3DProxy/RadiusDimConstraint3DProxy.md)

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |