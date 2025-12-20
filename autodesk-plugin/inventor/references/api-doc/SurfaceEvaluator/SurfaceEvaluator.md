# SurfaceEvaluator Object

## Description

The SurfaceEvaluator object. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Get3dCurveFrom2dCurve](../SurfaceEvaluator/SurfaceEvaluator_Get3dCurveFrom2dCurve.md) | Function that calculates the equivalent 3D curve for a 2D curve defined in the parametric space of the surface associated with the evaluator. The resulting transient geometry 3D curve is returned. The type of curve(s) returned is dependent on the shape of the input curve and the surface. |
| [GetCurvatures](../SurfaceEvaluator/SurfaceEvaluator_GetCurvatures.md) | Calculates the curvature direction and magnitude of the curve at the given parameter values. |
| [GetFirstDerivatives](../SurfaceEvaluator/SurfaceEvaluator_GetFirstDerivatives.md) | Calculates the first order derivatives at the given parameter values on the surface. |
| [GetIsoCurve](../SurfaceEvaluator/SurfaceEvaluator_GetIsoCurve.md) | Function that extracts a curve from the surface that follows a constant u or v parameter along the surface. It will have the same properties of the surface in the direction of the extraction. For example, if a curve is extracted from a periodic surface in the direction where it is periodic, the extracted curve will also be periodic. The type of curve returned is dependent on the shape the surface. |
| [GetNormal](../SurfaceEvaluator/SurfaceEvaluator_GetNormal.md) | Method that gets the surface normal. |
| [GetNormalAtPoint](../SurfaceEvaluator/SurfaceEvaluator_GetNormalAtPoint.md) | Function that returns the normal vectors for the specified points. |
| [GetParamAnomaly](../SurfaceEvaluator/SurfaceEvaluator_GetParamAnomaly.md) | Gets general information about the parameterization of the surface, such as whether or not it is periodic, singular, or unbounded in the parameter domain. |
| [GetParamAtPoint](../SurfaceEvaluator/SurfaceEvaluator_GetParamAtPoint.md) | Calculates the parameter value on the surface that is equal to the specified point. The point must lie on the surface. |
| [GetPointAtParam](../SurfaceEvaluator/SurfaceEvaluator_GetPointAtParam.md) | Calculates the coordinate points at the given parameter values on the surface. |
| [GetSecondDerivatives](../SurfaceEvaluator/SurfaceEvaluator_GetSecondDerivatives.md) | Calculates the second order derivatives at the given parameter values on the surface. |
| [GetTangents](../SurfaceEvaluator/SurfaceEvaluator_GetTangents.md) | Calculates the tangency directions at the given parameter values on the curve. |
| [GetThirdDerivatives](../SurfaceEvaluator/SurfaceEvaluator_GetThirdDerivatives.md) | Calculates the third order derivatives at the given parameter values on the surface. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Area](../SurfaceEvaluator/SurfaceEvaluator_Area.md) | Property that returns the area of the entity. |
| [Continuity](../SurfaceEvaluator/SurfaceEvaluator_Continuity.md) | Gets the level of continuity of the curve. The continuity is the largest order of continuity maintained for the entire curve. |
| [IsExtrudedShape](../SurfaceEvaluator/SurfaceEvaluator_IsExtrudedShape.md) | Read-only property that returns whether the surface resulted from an extrusion. |
| [IsParamOnFace](../SurfaceEvaluator/SurfaceEvaluator_IsParamOnFace.md) | Determines if the parameter is on the face. |
| [IsRevolvedShape](../SurfaceEvaluator/SurfaceEvaluator_IsRevolvedShape.md) | Read-only property that returns whether the surface resulted from a revolution. |
| [ParamRangeRect](../SurfaceEvaluator/SurfaceEvaluator_ParamRangeRect.md) | Property that returns a that defines the parameter range for this surface. |
| [RangeBox](../SurfaceEvaluator/SurfaceEvaluator_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |

## Accessed From

[BSplineSurface.Evaluator](../BSplineSurface/BSplineSurface_Evaluator.md), [Cone.Evaluator](../Cone/Cone_Evaluator.md), [Cylinder.Evaluator](../Cylinder/Cylinder_Evaluator.md), [EllipticalCone.Evaluator](../EllipticalCone/EllipticalCone_Evaluator.md), [EllipticalCylinder.Evaluator](../EllipticalCylinder/EllipticalCylinder_Evaluator.md), [Face.Evaluator](../Face/Face_Evaluator.md), [FaceProxy.Evaluator](../FaceProxy/FaceProxy_Evaluator.md), [MeshFace.Evaluator](../MeshFace/MeshFace_Evaluator.md), [MeshFaceProxy.Evaluator](../MeshFaceProxy/MeshFaceProxy_Evaluator.md), [Plane.Evaluator](../Plane/Plane_Evaluator.md), [PresentationFace.Evaluator](../PresentationFace/PresentationFace_Evaluator.md), [PublicationFace.Evaluator](PublicationFace_Evaluator.md), [PublicationMeshFace.Evaluator](PublicationMeshFace_Evaluator.md), [Sphere.Evaluator](../Sphere/Sphere_Evaluator.md), [Torus.Evaluator](../Torus/Torus_Evaluator.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Is cylindrical face interior or exterior?](../../sample-programs/Line_IsColinearTo_Sample.md) | This sample shows how to determine whether the selected cylindircal face is an exterior face or an interior (hollow) face. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |