# SurfaceBody.CalculateStrokes Method

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Obtain the stroked or polygonal representation for the given chord-height tolerance. Client to deallocate pointers with CoTaskMemFree.

## Syntax

SurfaceBody.**CalculateStrokes**( ***Tolerance*** As Double, ***VertexCount*** As Long, ***SegmentCount*** As Long, ***VertexCoordinates***() As Double, ***VertexIndices***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Tolerance | Double | Input Double that specifies the maximum distance that the stroke can deviate from the smooth curve. This value is in centimeters. Smaller values can result in a much greater number of strokes being returned and will require more processing time to calculate. The picture below illustrates how the chordal tolerance is used when creating a stroked version of a curve. The chordal tolerance defines the maximum distance a line can be from the actual curve. ![](../Images/ChordHeight.png) |
| VertexCount | Long | Output Long that returns the number of vertices that were generated. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| SegmentCount | Long | Output Long that returns the number of segments that were generated. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinates of the vertices. |
| VertexIndices | Long | Output array of Longs that are used to index into the vertex coordinates array. These indices provide the information that defines how the vertices are connected to create the connected set of strokes. |

## Version

Introduced in version 5.3
