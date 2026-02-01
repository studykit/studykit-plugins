# PresentationEdge.GetExistingStrokes Method

Parent Object: [PresentationEdge](../PresentationEdge/PresentationEdge.md)

## Description

Obtain the stroked or polygonal representation for the given chord-height tolerance. Fails if the tolerance supplied is not pre-existing.

## Syntax

PresentationEdge.**GetExistingStrokes**( ***ToleranceIndex*** As Double, ***VertexCount*** As Long, ***VertexCoordinates***() As Double, ***PolylineCount*** As Long, ***PolylineLengths***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToleranceIndex | Double | Input Double that serves as an index into which set of existing strokes you want to retrieve. If the input tolerance does not match an existing set an error will occur. The tolerances for existing strokes can be obtained using the GetExistingStrokeTolerances method. |
| VertexCount | Long | Output Long that returns the number of vertices that were generated for the strokes. This is the number of vertices will be returned by the VertexCoordinates argument. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinates of the vertices. |
| PolylineCount | Long | Output Long that specifies the number of polylines that are represented by the strokes. |
| PolylineLengths | Long | Output array of Longs that specifies the number of vertices that are used for each polyline. |

## Version

Introduced in version 2018
