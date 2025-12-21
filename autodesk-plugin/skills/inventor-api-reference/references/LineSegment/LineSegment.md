# LineSegment Object

## Description

The LineSegment object represents a line segment. The object created is a transient mathematical object and is not displayed graphically.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../LineSegment/LineSegment_Copy.md) | Creates a copy of this LineSegment object. The result is entirely independent and can be edited without affecting the original LineSegment object. |
| [DistanceTo](../LineSegment/LineSegment_DistanceTo.md) | Method that returns the distance to the specified point. |
| [GetLineSegmentData](../LineSegment/LineSegment_GetLineSegmentData.md) | Method that returns the data defining this line segment. |
| [IntersectWithCurve](../LineSegment/LineSegment_IntersectWithCurve.md) | Method that returns Point objects that represent the points at the intersection of the Line/LineSegment and the input curve. Returns Nothing if the curves overlap or are parallel. |
| [IntersectWithSurface](../LineSegment/LineSegment_IntersectWithSurface.md) | Method that returns Point objects that represent the points at the intersection of the Line/LineSegment and the input surface. Returns Nothing if the Line/LineSegment lies on the surface or it is parallel to the surface. |
| [PutLineSegmentData](../LineSegment/LineSegment_PutLineSegmentData.md) | Method that sets the data defining this line segment. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Direction](../LineSegment/LineSegment_Direction.md) | Property that returns the direction of the line segment. |
| [EndPoint](../LineSegment/LineSegment_EndPoint.md) | Specifies the end point of the line segment. |
| [Evaluator](../LineSegment/LineSegment_Evaluator.md) | Property that returns the CurveEvaluator for this line segment. |
| [MidPoint](../LineSegment/LineSegment_MidPoint.md) | Property that returns the midpoint of the line segment. |
| [StartPoint](../LineSegment/LineSegment_StartPoint.md) | Specifies the start point of the line segment. |

## Accessed From

[AngularModelDimension.ExtensionLineOne](../AngularModelDimension/AngularModelDimension_ExtensionLineOne.md), [AngularModelDimension.ExtensionLineTwo](../AngularModelDimension/AngularModelDimension_ExtensionLineTwo.md), [AngularModelDimensionProxy.ExtensionLineOne](../AngularModelDimensionProxy/AngularModelDimensionProxy_ExtensionLineOne.md), [AngularModelDimensionProxy.ExtensionLineTwo](../AngularModelDimensionProxy/AngularModelDimensionProxy_ExtensionLineTwo.md), [DWGEntityLineSegment.Geometry](../DWGEntityLineSegment/DWGEntityLineSegment_Geometry.md), [DWGEntityLineSegmentProxy.Geometry](../DWGEntityLineSegmentProxy/DWGEntityLineSegmentProxy_Geometry.md), [LineSegment.Copy](../LineSegment/LineSegment_Copy.md), [SketchLine.Geometry3d](../SketchLine/SketchLine_Geometry3d.md), [SketchLine3D.Geometry](../SketchLine3D/SketchLine3D_Geometry.md), [SketchLine3DProxy.Geometry](../SketchLine3DProxy/SketchLine3DProxy_Geometry.md), [SketchLineProxy.Geometry3d](../SketchLineProxy/SketchLineProxy_Geometry3d.md), [SketchSplineHandle.Geometry3d](../SketchSplineHandle/SketchSplineHandle_Geometry3d.md), [SketchSplineHandle3D.Geometry](../SketchSplineHandle3D/SketchSplineHandle3D_Geometry.md), [SketchSplineHandle3DProxy.Geometry](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Geometry.md), [SketchSplineHandleProxy.Geometry3d](../SketchSplineHandleProxy/SketchSplineHandleProxy_Geometry3d.md), [TransientGeometry.CreateLineSegment](../TransientGeometry/TransientGeometry_CreateLineSegment.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 6
