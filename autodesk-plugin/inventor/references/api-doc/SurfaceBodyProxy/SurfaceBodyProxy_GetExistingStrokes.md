# SurfaceBodyProxy.GetExistingStrokes Method

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Method that returns the specified set of strokes from the SurfaceBody, Face or Edge the method was called from. Existing strokes are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateStrokes method, which will calculate new strokes to a given tolerance at double-precision accuracy. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to strokes. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities.

## Syntax

SurfaceBodyProxy.**GetExistingStrokes**( ***ToleranceIndex*** As Double, ***VertexCount*** As Long, ***VertexCoordinates***() As Double, ***PolylineCount*** As Long, ***PolylineLengths***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToleranceIndex | Double | Input Double that serves as an index into which set of existing strokes you want to retrieve. If the input tolerance does not match an existing set an error will occur. The tolerances for existing strokes can be obtained using the GetExistingStrokeTolerances method. |
| VertexCount | Long | Output Long that returns the number of vertices that were generated for the facets. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinates of the vertices. |
| PolylineCount | Long | Output Long that specifies the number of polylines that are represented by the strokes. |
| PolylineLengths | Long | Output array of Longs that specifies the number of vertices that are used for each polyline. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |