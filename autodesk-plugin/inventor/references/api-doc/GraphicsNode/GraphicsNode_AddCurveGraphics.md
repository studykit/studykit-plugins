# GraphicsNode.AddCurveGraphics Method

Parent Object: [GraphicsNode](../GraphicsNode/GraphicsNode.md)

## Description

Method that creates a new CurveGraphics graphic primitive.

## Syntax

GraphicsNode.**AddCurveGraphics**( ***Curve*** As Object ) As [CurveGraphics](../CurveGraphics/CurveGraphics.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Object | Input object that defines the curve. This can be one of the following: LineSegment, Circle, Arc3d, EllipseFull, EllipticalArc, BSplineCurve and Polyline3d. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |