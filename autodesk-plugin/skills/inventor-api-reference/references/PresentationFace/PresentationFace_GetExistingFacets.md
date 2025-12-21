# PresentationFace.GetExistingFacets Method

Parent Object: [PresentationFace](../PresentationFace/PresentationFace.md)

## Description

Obtain the facetted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing.

## Syntax

PresentationFace.**GetExistingFacets**( ***ToleranceIndex*** As Double, ***VertexCount*** As Long, ***FacetCount*** As Long, ***VertexCoordinates***() As Double, ***NormalVectors***() As Double, ***VertexIndices***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToleranceIndex | Double | Input Double that serves as an index as to which set of existing facets you want to retrieve. If the input tolerance does not match an existing set an error will occur. The tolerances for existing facets can be obtained using the GetExistingFacetTolerances method. |
| VertexCount | Long | Output Long that returns the number of vertices that were generated. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| FacetCount | Long | Output Long that returns the number of facets that were generated. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinate locations of the vertices. The values are defined in x, y, z order within the array and represent coordinates within the model space of the faceted object. |
| NormalVectors | Double | Output array of Doubles that defines the normal for each vertex in the facet mesh. The values are defined in x, y, z order within the array and represent vector components within the model space of the faceted object. |
| VertexIndices | Long | Output array of Longs that are used as index values to index into the vertex coordinate list. The first coordinate in the vertex coordinate list is index 1. Using vertex indices allows vertex coordinates to be reused by more than one triangle, thus reducing the overall resources required to define the entire mesh. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |