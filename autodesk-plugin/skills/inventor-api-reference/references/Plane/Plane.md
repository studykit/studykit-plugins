# Plane Object

## Description

The Plane object. A plane object is infinite. The object created is a transient mathematical object and is not displayed graphically. For more information, see the Transient Geometry article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../Plane/Plane_Copy.md) | Creates a copy of this Plane object. The result is entirely independent and can be edited without affecting the original Plane object. |
| [DistanceTo](../Plane/Plane_DistanceTo.md) | Determine the distance between this plane and the specified point. |
| [GetPlaneData](../Plane/Plane_GetPlaneData.md) | Method that gets the data defining this plane. |
| [IntersectWithCurve](../Plane/Plane_IntersectWithCurve.md) | Gets the intersection points of the Plane and the input curve. Note that 3D transient geometry should be supplied. Obtain 3D transient geometry from any sktech entities or 2D geometry before calling this method (for example, by calling the Geometry method of the entity). |
| [IntersectWithLine](../Plane/Plane_IntersectWithLine.md) | Compute the intersection point of this Plane and the specified Line. If the Plane and the Line are parallel, this method will fail. |
| [IntersectWithPlane](../Plane/Plane_IntersectWithPlane.md) | Compute the intersection line of this Plane and the specified Plane. If the two Planes are parallel, this method will fail. |
| [IntersectWithSurface](../Plane/Plane_IntersectWithSurface.md) | Gets the intersection curves and points between the plane and the input surface. |
| [PutPlaneData](../Plane/Plane_PutPlaneData.md) | Method that sets the data defining this plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Evaluator](../Plane/Plane_Evaluator.md) | Gets the surface evaluator for this plane. |
| [IsCoplanarTo](../Plane/Plane_IsCoplanarTo.md) | Property that gets whether this Plane is coplanar with the specified Plane. |
| [IsParallelTo](../Plane/Plane_IsParallelTo.md) | Property that gets whether this Plane is parallel to the specified Line or Plane. |
| [IsPerpendicularTo](../Plane/Plane_IsPerpendicularTo.md) | Determine if this Plane is perpendicular to the specified Line or Plane. |
| [Normal](../Plane/Plane_Normal.md) | Property that indicates the vector for a specific normal in the set. |
| [RootPoint](../Plane/Plane_RootPoint.md) | Gets the root point for this plane. |

## Accessed From

[AnnotationPlaneDefinition.Plane](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Plane.md), [DesignViewRepresentation.GetSectionViewInfo](../DesignViewRepresentation/DesignViewRepresentation_GetSectionViewInfo.md), [DimensionConstraint3D.DimensionPlane](../DimensionConstraint3D/DimensionConstraint3D_DimensionPlane.md), [DimensionConstraints3D.GetDimensionPlane](../DimensionConstraints3D/DimensionConstraints3D_GetDimensionPlane.md), [GroundPlaneSettings.Plane](../GroundPlaneSettings/GroundPlaneSettings_Plane.md), [LineLengthDimConstraint3D.DimensionPlane](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_DimensionPlane.md), [LineLengthDimConstraint3DProxy.DimensionPlane](../LineLengthDimConstraint3DProxy/LineLengthDimConstraint3DProxy_DimensionPlane.md), [PlanarSketch.PlanarEntityGeometry](../PlanarSketch/PlanarSketch_PlanarEntityGeometry.md), [PlanarSketchProxy.PlanarEntityGeometry](../PlanarSketchProxy/PlanarSketchProxy_PlanarEntityGeometry.md), [Plane.Copy](../Plane/Plane_Copy.md), [PointAndPlaneDistanceDimConstraint3D.DimensionPlane](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_DimensionPlane.md), [PointAndPlaneDistanceDimConstraint3DProxy.DimensionPlane](../PointAndPlaneDistanceDimConstraint3DProxy/PointAndPlaneDistanceDimConstraint3DProxy_DimensionPlane.md), [PointCloudPlane.Geometry](../PointCloudPlane/PointCloudPlane_Geometry.md), [PointCloudPlane.GetPlaneRectangle](../PointCloudPlane/PointCloudPlane_GetPlaneRectangle.md), [PointCloudPlaneProxy.Geometry](../PointCloudPlaneProxy/PointCloudPlaneProxy_Geometry.md), [PointCloudPlaneProxy.GetPlaneRectangle](../PointCloudPlaneProxy/PointCloudPlaneProxy_GetPlaneRectangle.md), [RadiusDimConstraint3D.DimensionPlane](../RadiusDimConstraint3D/RadiusDimConstraint3D_DimensionPlane.md), [RadiusDimConstraint3DProxy.DimensionPlane](../RadiusDimConstraint3DProxy/RadiusDimConstraint3DProxy_DimensionPlane.md), [SketchBlockDefinition.PlanarEntityGeometry](../SketchBlockDefinition/SketchBlockDefinition_PlanarEntityGeometry.md), [SketchBlockDefinitionProxy.PlanarEntityGeometry](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_PlanarEntityGeometry.md), [SplineLengthDimConstraint3D.DimensionPlane](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_DimensionPlane.md), [SplineLengthDimConstraint3DProxy.DimensionPlane](../SplineLengthDimConstraint3DProxy/SplineLengthDimConstraint3DProxy_DimensionPlane.md), [TransientGeometry.CreatePlane](../TransientGeometry/TransientGeometry_CreatePlane.md), [TransientGeometry.CreatePlaneByThreePoints](../TransientGeometry/TransientGeometry_CreatePlaneByThreePoints.md), [TwoLineAngleDimConstraint3D.DimensionPlane](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_DimensionPlane.md), [TwoLineAngleDimConstraint3DProxy.DimensionPlane](../TwoLineAngleDimConstraint3DProxy/TwoLineAngleDimConstraint3DProxy_DimensionPlane.md), [TwoPointDistanceDimConstraint3D.DimensionPlane](../TwoPointDistanceDimConstraint3D/TwoPointDistanceDimConstraint3D_DimensionPlane.md), [TwoPointDistanceDimConstraint3DProxy.DimensionPlane](../TwoPointDistanceDimConstraint3DProxy/TwoPointDistanceDimConstraint3DProxy_DimensionPlane.md), [WorkPlane.Plane](../WorkPlane/WorkPlane_Plane.md), [WorkPlaneProxy.Plane](../WorkPlaneProxy/WorkPlaneProxy_Plane.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Offset a 2D sketch](../../sample-programs/Sketch_OffsetSketchEntitiesUsingDistance_Sample.md) | This sample demonstrates the creation of offsets in 2d sketches. Two ways of creating the offset are shown - one uses a distance and the other uses the input point. |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |