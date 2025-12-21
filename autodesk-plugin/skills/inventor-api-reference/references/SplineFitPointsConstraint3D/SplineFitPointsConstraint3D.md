# SplineFitPointsConstraint3D Object

Derived from: [GeometricConstraint3D](../GeometricConstraint3D/GeometricConstraint3D.md) Object

## Description

The SplineFitPointsConstraint3D object represents a constraint that makes a spline fit through a series of specified sketch points. This constraint is created automatically when a spline is created.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [Parent](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Points](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_Points.md) | Property that returns the sketch points the spline is fit through. |
| [Spline](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_Spline.md) | Property that returns the spline entity being constrained. |
| [Type](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SplineFitPointsConstraint3DProxy.NativeObject](../SplineFitPointsConstraint3DProxy/SplineFitPointsConstraint3DProxy_NativeObject.md)

## Derived Classes

[SplineFitPointsConstraint3DProxy](../SplineFitPointsConstraint3DProxy/SplineFitPointsConstraint3DProxy.md)

## Version

Introduced in version 8
