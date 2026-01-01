# Face.CalculateFacetsAndTextureMap Method

Parent Object: [Face](../Face/Face.md)

## Description

Obtain the facetted representation for the given chord-height tolerance. This also include the texture map coordinates.

## Syntax

Face.**CalculateFacetsAndTextureMap**( ***Tolerance*** As Double, ***VertexCount*** As Long, ***FacetCount*** As Long, ***VertexCoordinates***() As Double, ***NormalVectors***() As Double, ***VertexIndices***() As Long, ***TextureCoordinates***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Tolerance | Double | Input Double that specifies the maximum distance that the facet can deviate from the smooth surface. This value is in centimeters. Smaller values can result in a much greater number of facets being returned and will require more processing time to calculate. The picture below illustrates how the chordal tolerance is used when creating a stroked version of a curve. The chordal tolerance defines the maximum distance a line can be from the actual curve. When calculating facets the same concept applies but it defines the maximum distance between a triangle facet and the smooth surface. ![](../Images/ChordHeight.png) The pictures below illustrate the difference obtained when calculating facets for a model using different chordal tolerances. The overall size of this model is approx. 6x6x4 cm’s. The picture on the left used a chordal tolerance of 0.1 cm and the one on the right used a tolerance of 0.01 cm. ![](../Images/ChordHeightFacetExample.png) |
| VertexCount | Long | Output Long that returns the number of vertices that were generated. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| FacetCount | Long | Output Long that returns the number of facets that were generated. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinates of the vertices. |
| NormalVectors | Double | Output array of Doubles that contains the coordinate locations of the vertices. The values are defined in x, y, z order within the array and represent coordinates within the model space of the faceted object. |
| VertexIndices | Long | Output array of Longs that are used as index values to index into the vertex coordinate list. The first coordinate in the vertex coordinate list is index 1. Using vertex indices allows vertex coordinates to be reused by more than one triangle, thus reducing the overall resources required to define the entire mesh. |
| TextureCoordinates | Double | Output array of Doubles that contains the coordinates of the texture map. |

## Version

Introduced in version 9
