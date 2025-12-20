# PresentationFace.CalculateStrokes Method

Parent Object: [PresentationFace](../PresentationFace/PresentationFace.md)

## Description

Obtain the stroked or polygonal representation for the given chord-height tolerance. Client to deallocate pointers with CoTaskMemFree.

## Syntax

PresentationFace.**CalculateStrokes**( ***Tolerance*** As Double, ***VertexCount*** As Long, ***SegmentCount*** As Long, ***VertexCoordinates***() As Double, ***VertexIndices***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Tolerance | Double | Input Double that specifies the maximum distance that the stroke can deviate from the smooth curve. This value is in centimeters. Smaller values can result in a much greater number of strokes being returned and will require more processing time to calculate. |
| VertexCount | Long | Output Long that returns the number of vertices that were generated. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| SegmentCount | Long | Output Long that returns the number of vertices that were generated. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinate locations of the vertices. The values are defined in x, y, z order within the array and represent coordinates within the model space of the faceted object. |
| VertexIndices | Long | Output array of Longs that are used as index values to index into the vertex coordinate list. The first coordinate in the vertex coordinate list is index 1. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |