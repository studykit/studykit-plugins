# GeometricConstraint3D Object

## Description

The GeometricConstraint3D object represents the base class of all 3D geometric constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../GeometricConstraint3D/GeometricConstraint3D_Delete.md) | Method that deletes the constraint. In the case of coincident constraint, all the connected lines are disconnected and the constraint is deleted. |
| [GetReferenceKey](../GeometricConstraint3D/GeometricConstraint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GeometricConstraint3D/GeometricConstraint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../GeometricConstraint3D/GeometricConstraint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Deletable](../GeometricConstraint3D/GeometricConstraint3D_Deletable.md) | Indicates whether this object can be deleted. |
| [Parent](../GeometricConstraint3D/GeometricConstraint3D_Parent.md) | Property that returns the parent sketch of the object. |
| [Type](../GeometricConstraint3D/GeometricConstraint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeometricConstraints3D.Item](../GeometricConstraints3D/GeometricConstraints3D_Item.md)

## Derived Classes

[BendConstraint](../BendConstraint/BendConstraint.md), [CoincidentConstraint3D](../CoincidentConstraint3D/CoincidentConstraint3D.md), [CollinearConstraint3D](../CollinearConstraint3D/CollinearConstraint3D.md), [ConcentricConstraint3D](../ConcentricConstraint3D/ConcentricConstraint3D.md), [ConcentricConstraint3DProxy](../ConcentricConstraint3DProxy/ConcentricConstraint3DProxy.md), [CustomConstraint3D](../CustomConstraint3D/CustomConstraint3D.md), [EqualConstraint3D](../EqualConstraint3D/EqualConstraint3D.md), [GroundConstraint3D](../GroundConstraint3D/GroundConstraint3D.md), [HelicalConstraint3D](../HelicalConstraint3D/HelicalConstraint3D.md), [HelicalConstraint3DProxy](../HelicalConstraint3DProxy/HelicalConstraint3DProxy.md), [MidpointConstraint3D](../MidpointConstraint3D/MidpointConstraint3D.md), [OnFaceConstraint3D](../OnFaceConstraint3D/OnFaceConstraint3D.md), [ParallelConstraint3D](../ParallelConstraint3D/ParallelConstraint3D.md), [ParallelToXAxisConstraint3D](../ParallelToXAxisConstraint3D/ParallelToXAxisConstraint3D.md), [ParallelToXYPlaneConstraint3D](../ParallelToXYPlaneConstraint3D/ParallelToXYPlaneConstraint3D.md), [ParallelToXZPlaneConstraint3D](../ParallelToXZPlaneConstraint3D/ParallelToXZPlaneConstraint3D.md), [ParallelToYAxisConstraint3D](../ParallelToYAxisConstraint3D/ParallelToYAxisConstraint3D.md), [ParallelToYZPlaneConstraint3D](../ParallelToYZPlaneConstraint3D/ParallelToYZPlaneConstraint3D.md), [ParallelToZAxisConstraint3D](../ParallelToZAxisConstraint3D/ParallelToZAxisConstraint3D.md), [PerpendicularConstraint3D](../PerpendicularConstraint3D/PerpendicularConstraint3D.md), [SmoothConstraint3D](../SmoothConstraint3D/SmoothConstraint3D.md), [SplineFitPointsConstraint3D](../SplineFitPointsConstraint3D/SplineFitPointsConstraint3D.md), [TangentConstraint3D](../TangentConstraint3D/TangentConstraint3D.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |