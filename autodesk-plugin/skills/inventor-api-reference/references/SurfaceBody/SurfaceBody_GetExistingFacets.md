# SurfaceBody.GetExistingFacets Method

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Obtain the faceted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing/

## Remarks

Note that CalculateFacets and GetExistingFacets (or GetExistingTolerances) are completely unrelated other than they both deal in facet data. CalculateFacets facets the model and returns that result. It does not effect any information held by Inventor. It is just direct access to the internal facet generator. The GetExistingFacets/Tolerances methods access the existing facet data held by the internal scene, if any. They access the set of existing tolerances and facets currently being held. Therefore it is quite possible that existing facets at a given tolerance may not exactly match calculated facets at the same tolerance.

## Syntax

SurfaceBody.**GetExistingFacets**( ***ToleranceIndex*** As Double, ***VertexCount*** As Long, ***FacetCount*** As Long, ***VertexCoordinates***() As Double, ***NormalVectors***() As Double, ***VertexIndices***() As Long )

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

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |

## Version

Introduced in version 5.3
