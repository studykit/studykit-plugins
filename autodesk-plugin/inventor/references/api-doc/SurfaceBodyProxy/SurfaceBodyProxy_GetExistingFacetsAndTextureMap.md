# SurfaceBodyProxy.GetExistingFacetsAndTextureMap Method

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Method that returns the specified set of existing display facets. Existing display facets are stored to single-precision floating point accuracy. This is typically adequate accuracy for display purposes. If a more accurate result is required you can use the CalculateFacets method which will calculate new facets to a given tolerance at double-precision accuracy.

## Syntax

SurfaceBodyProxy.**GetExistingFacetsAndTextureMap**( ***ToleranceIndex*** As Double, ***VertexCount*** As Long, ***FacetCount*** As Long, ***VertexCoordinates***() As Double, ***NormalVectors***() As Double, ***VertexIndices***() As Long, ***TextureCoordinates***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToleranceIndex | Double | Input Double that serves as an index as to which set of existing facets you want to retrieve. If the input tolerance does not match an existing set an error will occur. The tolerances for existing facets can be obtained using the GetExistingFacetTolerances method. |
| VertexCount | Long | Output Long that returns the number of vertices that were generated for the facets. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| FacetCount | Long | Output Long that returns the number of facets that were generated. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinates of the vertices. |
| NormalVectors | Double | Output array of Singles that contains the components of the vertex normals. A normal is returned for each vertex. The normal is the normal of the actual surface at the position of the vertex. |
| VertexIndices | Long | Output array of Longs that are used to index into the vertex coordinates array. These indices provide the information that defines how the vertices are connected to create the triangular facets. |
| TextureCoordinates | Double | Output array of Doubles that contains the coordinates of the texture. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |