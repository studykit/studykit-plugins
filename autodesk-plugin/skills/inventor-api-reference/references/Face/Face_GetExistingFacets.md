# Face.GetExistingFacets Method

Parent Object: [Face](../Face/Face.md)

## Description

Obtain the facetted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing.

## Syntax

Face.**GetExistingFacets**( ***ToleranceIndex*** As Double, ***VertexCount*** As Long, ***FacetCount*** As Long, ***VertexCoordinates***() As Double, ***NormalVectors***() As Double, ***VertexIndices***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToleranceIndex | Double | Input Double that serves as an index as to which set of existing facets you want to retrieve. If the input tolerance does not match an existing set an error will occur. The tolerances for existing facets can be obtained using the GetExistingFacetTolerances method. |
| VertexCount | Long | Output Long that returns the number of vertices that were generated for the facets. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| FacetCount | Long | Output Long that returns the number of facets that were generated. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinates of the vertices. |
| NormalVectors | Double | Output array of Doubles that contains the components of the vertex normals. A normal is returned for each vertex. The normal is the normal of the actual surface at the position of the vertex. |
| VertexIndices | Long | Output array of Doubles that are used to index into the vertex coordinates array. These indices provide the information that defines how the vertices are connected to create the triangular facets. |

## Version

Introduced in version 5.3
