# TextBox.GetFacetsInfo Method

Parent Object: [TextBox](../TextBox/TextBox.md)

## Description

Returns facets’ coordinates of the text box.

## Syntax

TextBox.**GetFacetsInfo**( ***VertexCount*** As Long, ***FacetCount*** As Long, ***VertexCoordinates***() As Double, ***VertexIndices***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| VertexCount | Long | Output Long value that indicates vertex count of the facets. |
| FacetCount | Long | Output Long value that indicates facet count of the facets. |
| VertexCoordinates | Double | Output array of Doubles that indicates the vertices coordinates of the facets. The array is a single dimension array containing sequential x, y, z values. |
| VertexIndices | Long | Output array of Longs that are used as index values to index into the facets vertex coordinate list. The first coordinate in the vertex coordinate list is index 1. Using vertex indices allows vertex coordinates to be reused by more than one triangle, thus reducing the overall resources required to define the entire mesh. |

## Version

Introduced in version 2017
