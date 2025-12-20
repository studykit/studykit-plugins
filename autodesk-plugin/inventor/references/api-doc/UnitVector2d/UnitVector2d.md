# UnitVector2d Object

## Description

The UnitVector2d object. For more information, see the [Transient Geometry](TransientGeometry_Overview.md) overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AngleTo](../UnitVector2d/UnitVector2d_AngleTo.md) | Determines the angle between this unit vector2d and the specified unit vector2d. |
| [AsVector](../UnitVector2d/UnitVector2d_AsVector.md) | Get the vector2d equivalent of this unit vector2d. |
| [Copy](../UnitVector2d/UnitVector2d_Copy.md) | Creates a copy of this UnitVector2d object. The result is entirely independent and can be edited without affecting the original UnitVector2d object. |
| [DotProduct](../UnitVector2d/UnitVector2d_DotProduct.md) | Determine the dot product of this unit vector2d to the specified unit vector2d. |
| [GetUnitVectorData](../UnitVector2d/UnitVector2d_GetUnitVectorData.md) | Get the data defining this unit vector. |
| [IsEqualTo](../UnitVector2d/UnitVector2d_IsEqualTo.md) | Compare this unit vector2d for equality to the specified unit vector2d. |
| [IsParallelTo](../UnitVector2d/UnitVector2d_IsParallelTo.md) | Determine if this unit vector2d is parallel to the specified unit vector2d. |
| [IsPerpendicularTo](../UnitVector2d/UnitVector2d_IsPerpendicularTo.md) | Determine if this unit vector2d is perpendicular to the specified unit vector2d. |
| [PutUnitVectorData](../UnitVector2d/UnitVector2d_PutUnitVectorData.md) | Method that sets the data defining this unit vector. |
| [TransformBy](../UnitVector2d/UnitVector2d_TransformBy.md) | Transform this unit vector2d by the specified matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [X](../UnitVector2d/UnitVector2d_X.md) | Gets the X-component for this UnitVector2d. |
| [Y](../UnitVector2d/UnitVector2d_Y.md) | Gets the Y-component for this UnitVector2d. |

## Accessed From

[Centermark.ExtensionPointFourDirection](../Centermark/Centermark_ExtensionPointFourDirection.md), [Centermark.ExtensionPointOneDirection](../Centermark/Centermark_ExtensionPointOneDirection.md), [Centermark.ExtensionPointThreeDirection](../Centermark/Centermark_ExtensionPointThreeDirection.md), [Centermark.ExtensionPointTwoDirection](../Centermark/Centermark_ExtensionPointTwoDirection.md), [EllipticalArc2d.MajorAxis](../EllipticalArc2d/EllipticalArc2d_MajorAxis.md), [Line2d.Direction](../Line2d/Line2d_Direction.md), [LineSegment2d.Direction](../LineSegment2d/LineSegment2d_Direction.md), [SketchEllipse.MajorAxisVector](../SketchEllipse/SketchEllipse_MajorAxisVector.md), [SketchEllipseProxy.MajorAxisVector](../SketchEllipseProxy/SketchEllipseProxy_MajorAxisVector.md), [SketchEllipticalArc.MajorAxisVector](../SketchEllipticalArc/SketchEllipticalArc_MajorAxisVector.md), [SketchEllipticalArcProxy.MajorAxisVector](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_MajorAxisVector.md), [SketchSplineHandle.Tangent](../SketchSplineHandle/SketchSplineHandle_Tangent.md), [SketchSplineHandleProxy.Tangent](../SketchSplineHandleProxy/SketchSplineHandleProxy_Tangent.md), [TransientGeometry.CreateUnitVector2d](../TransientGeometry/TransientGeometry_CreateUnitVector2d.md), [UnitVector2d.Copy](../UnitVector2d/UnitVector2d_Copy.md), [Vector2d.AsUnitVector](../Vector2d/Vector2d_AsUnitVector.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Offset a 2D sketch](../../sample-programs/Sketch_OffsetSketchEntitiesUsingDistance_Sample.md) | This sample demonstrates the creation of offsets in 2d sketches. Two ways of creating the offset are shown - one uses a distance and the other uses the input point. |
| [Create sketch elliptical arc](../../sample-programs/SketchEllipticalArc_Sample.md) | This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |