# Line Object

## Description

The Line object. The object created is a transient mathematical object and is not displayed graphically. For more information, see the Transient Geometry article in the overview section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../Line/Line_Copy.md) | Creates a copy of this Line object. The result is entirely independent and can be edited without affecting the original Line object. |
| [DistanceTo](../Line/Line_DistanceTo.md) | Method that returns the distance to the specified point. |
| [GetLineData](../Line/Line_GetLineData.md) | Get the data defining this line. |
| [IntersectWithCurve](../Line/Line_IntersectWithCurve.md) | Method that returns Point objects that represent the points at the intersection of the Line/LineSegment and the input curve. Returns Nothing if the curves overlap or are parallel. |
| [IntersectWithSurface](../Line/Line_IntersectWithSurface.md) | Method that returns Point objects that represent the points at the intersection of the Line/LineSegment and the input surface. Returns Nothing if the Line/LineSegment lies on the surface or it is parallel to the surface. |
| [PutLineData](../Line/Line_PutLineData.md) | Method that sets the data defining this line. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Direction](../Line/Line_Direction.md) | Specifies the direction of the line. |
| [Evaluator](../Line/Line_Evaluator.md) | Gets the CurveEvaluator for the line. |
| [IsColinearTo](../Line/Line_IsColinearTo.md) | Property that gets whether this line is colinear to the specified line, within the specified tolerance. |
| [RootPoint](../Line/Line_RootPoint.md) | Specifies the root point of the line. |

## Accessed From

[AnnotationPlaneDefinition.XAxis](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_XAxis.md), [DetailDrawingView.DrawingViewToModelSpace](../DetailDrawingView/DetailDrawingView_DrawingViewToModelSpace.md), [DetailDrawingView.SheetToModelSpace](../DetailDrawingView/DetailDrawingView_SheetToModelSpace.md), [DrawingView.DrawingViewToModelSpace](../DrawingView/DrawingView_DrawingViewToModelSpace.md), [DrawingView.SheetToModelSpace](../DrawingView/DrawingView_SheetToModelSpace.md), [Line.Copy](../Line/Line_Copy.md), [PlanarSketch.AxisEntityGeometry](../PlanarSketch/PlanarSketch_AxisEntityGeometry.md), [PlanarSketchProxy.AxisEntityGeometry](../PlanarSketchProxy/PlanarSketchProxy_AxisEntityGeometry.md), [Plane.IntersectWithPlane](../Plane/Plane_IntersectWithPlane.md), [SectionDrawingView.DrawingViewToModelSpace](../SectionDrawingView/SectionDrawingView_DrawingViewToModelSpace.md), [SectionDrawingView.SheetToModelSpace](../SectionDrawingView/SectionDrawingView_SheetToModelSpace.md), [SketchBlockDefinition.AxisEntityGeometry](../SketchBlockDefinition/SketchBlockDefinition_AxisEntityGeometry.md), [SketchBlockDefinitionProxy.AxisEntityGeometry](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_AxisEntityGeometry.md), [TransientGeometry.CreateLine](../TransientGeometry/TransientGeometry_CreateLine.md), [WorkAxis.Line](../WorkAxis/WorkAxis_Line.md), [WorkAxisProxy.Line](../WorkAxisProxy/WorkAxisProxy_Line.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 4
