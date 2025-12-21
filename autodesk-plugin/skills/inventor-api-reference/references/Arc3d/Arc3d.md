# Arc3d Object

## Description

The Arc3d object is a mathematical representation of a 3d arc.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../Arc3d/Arc3d_Copy.md) | Creates a copy of this Arc3d object. The result is entirely independent and can be edited without affecting the original Arc3d object. |
| [GetArcData](../Arc3d/Arc3d_GetArcData.md) | Get the data defining this arc. |
| [PutArcData](../Arc3d/Arc3d_PutArcData.md) | Method that sets the data defining this arc. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Center](../Arc3d/Arc3d_Center.md) | Specifies the center point for this arc. |
| [EndPoint](../Arc3d/Arc3d_EndPoint.md) | Property that returns the end point of the arc. |
| [Evaluator](../Arc3d/Arc3d_Evaluator.md) | Property that gets the CurveEvaluator for this arc. |
| [Normal](../Arc3d/Arc3d_Normal.md) | Specifies the normal for this arc. |
| [Radius](../Arc3d/Arc3d_Radius.md) | Specifies the radius for this arc. |
| [ReferenceVector](../Arc3d/Arc3d_ReferenceVector.md) | Specifies the reference vector for this arc. |
| [StartAngle](../Arc3d/Arc3d_StartAngle.md) | Specifies the starting angle for this arc. |
| [StartPoint](../Arc3d/Arc3d_StartPoint.md) | Property that gets the start point of the arc. |
| [SweepAngle](../Arc3d/Arc3d_SweepAngle.md) | Specifies the sweep angle from the start angle for this arc. |

## Accessed From

[Arc3d.Copy](../Arc3d/Arc3d_Copy.md), [SketchArc.Geometry3d](../SketchArc/SketchArc_Geometry3d.md), [SketchArc3D.Geometry](../SketchArc3D/SketchArc3D_Geometry.md), [SketchArc3DProxy.Geometry](../SketchArc3DProxy/SketchArc3DProxy_Geometry.md), [SketchArcProxy.Geometry3d](../SketchArcProxy/SketchArcProxy_Geometry3d.md), [TransientGeometry.CreateArc3d](../TransientGeometry/TransientGeometry_CreateArc3d.md), [TransientGeometry.CreateArc3dByThreePoints](../TransientGeometry/TransientGeometry_CreateArc3dByThreePoints.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |