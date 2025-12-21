# PresentationEdge.CalculateStrokes Method

Parent Object: [PresentationEdge](../PresentationEdge/PresentationEdge.md)

## Description

Obtain the stroked or polygonal representation for the given chord-height tolerance. Client to deallocate pointers with CoTaskMemFree.

## Syntax

PresentationEdge.**CalculateStrokes**( ***Tolerance*** As Double, ***VertexCount*** As Long, ***SegmentCount*** As Long, ***VertexCoordinates***() As Double, ***VertexIndices***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Tolerance | Double | Input Double that defines the accuracy of the strokes. This is a "chord height" tolerance. This is the maximum distance the stroke can be from the actual curve. |
| VertexCount | Long | Output Long that returns the number of vertices that were generated for the strokes. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| SegmentCount | Long | Output Long that returns the number of line segments represented by the strokes. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinates of the vertices. |
| VertexIndices | Long | Output array of Longs that are used to index into the vertex coordinates array. These indices provide the information that defines how the vertices are connected to create the strokes. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |