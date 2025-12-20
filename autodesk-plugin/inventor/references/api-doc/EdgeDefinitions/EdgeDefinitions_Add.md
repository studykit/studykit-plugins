# EdgeDefinitions.Add Method

Parent Object: [EdgeDefinitions](../EdgeDefinitions/EdgeDefinitions.md)

## Description

Method that creates a new EdgeDefinition within the associated SurfaceBodyDefinition.

## Remarks

Various combinations of the input arguments can be used to define the edge in different ways. The various valid combinations are described below: \* If you know the geometry of the edge as a 3d curve in model space then just the ModelSpaceCurve argument can be supplied. \* If you know the geometry of the edge in parametric space of one of the faces then you can supply the ParameterSpaceCurveOne that defines the 2d parameter space curve and the FaceOne argument that defines the parameter space that curve is defined within. Optionally you can also supply the ParameterSpaceCurveTwo and FaceTwo arguments to define the edge in parametric space of the second face too. \* You can also define the edge as the intersection of two faces by supplying only the FaceOne and FaceTwo arguments.

## Syntax

EdgeDefinitions.**Add**( ***StartVertex*** As [VertexDefinition](../VertexDefinition/VertexDefinition.md), ***EndVertex*** As [VertexDefinition](../VertexDefinition/VertexDefinition.md), [***ModelSpaceCurve***] As Variant, [***ParameterSpaceCurveOne***] As Variant, [***FaceOne***] As Variant, [***ParameterSpaceCurveTwo***] As Variant, [***FaceTwo***] As Variant ) As [EdgeDefinition](../EdgeDefinition/EdgeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartVertex | [VertexDefinition](../VertexDefinition/VertexDefinition.md) | Optional input VertexDefinition object that defines the start of the edge. |
| EndVertex | [VertexDefinition](../VertexDefinition/VertexDefinition.md) | Optional input VertexDefinition object that defines the end of the edge. |
| ModelSpaceCurve | Variant | Optional input transient geometry curve object that defines the shape of this edge using 3d geometry in model space. Valid input is Arc3d, BsplineCurve, Circle, EllipseFull, EllipticalArc, LineSegment and Polyline3D. |
| ParameterSpaceCurveOne | Variant | Optional input transient geometry curve object that defines the shape of this edge using 2d geometry in the parametric space of the surface defined by the FaceOne argument. Valid input is Arc2d, BsplineCurve2d, Circle2d, EllipseFull2d, EllipticalArc2d, LineSegment2d and Polyline2D.   This is an optional argument whose default value is null. |
| FaceOne | Variant | Optional input FaceDefinition object that either defines the parametric space that the curve provided in ParameterSpaceCurveOne argument is defined within or it defines the first of two faces to be intersected to calculate the edge.   This is an optional argument whose default value is null. |
| ParameterSpaceCurveTwo | Variant | Optional input transient geometry curve object that defines the shape of this edge using 2d geometry in the parametric space of the surface defined by the FaceOne argument. Valid input is Arc2d, BsplineCurve2d, Circle2d, EllipseFull2d, EllipticalArc2d, LineSegment2d and Polyline2D.   This is an optional argument whose default value is null. |
| FaceTwo | Variant | Optional input FaceDefinition object that either defines the parametric space that the curve provided in ParameterSpaceCurveTwo argument is defined within or it defines the second of two faces to be intersected to calculate the edge.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |