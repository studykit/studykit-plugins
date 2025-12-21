# PresentationBody.CalculateFacetsWithOptions Method

Parent Object: [PresentationBody](../PresentationBody/PresentationBody.md)

## Description

Method that creates a new set of facets within the specified conditions.

## Syntax

PresentationBody.**CalculateFacetsWithOptions**( ***ChordalTolerance*** As Double, ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***VertexCount*** As Long, ***FacetCount*** As Long, ***VertexCoordinates***() As Double, ***NormalVectors***() As Double, ***VertexIndices***() As Long, [***TextureCoordinates***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ChordalTolerance | Double | Input Double that specifies the maximum distance that the facet can deviate from the smooth surface. This value is in centimeters. Smaller values can result in a much greater number of facets being returned and will require more processing time to calculate. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies additional tolerances that can be used to control the output mesh. The supported options are: Name: MaxSideLength, Value: Defines the maximum side of any triangle in the mesh. A value of 0, or not supplying this value indicates that no maximum length is specified. Name: MaxAspectRatio, Value: Defines the maximum length to height ratio that a triangle can have. This helps to avoid long skinny triangles. A value of 0, or not supplying this value indicates that no maximum aspect ratio is specified. Name: MaxNormalDeviation, Value: Defines the maximum deviation between adjacent vertex normals. This value is the maximum angle allows between normals and is input as radians. A value of 0, or not supplying this value indicates that no normal deviation is specified. Name: ConversionMode, Value: Specifies the conversion mode (0 or 2). 0 - Do not convert the display mesh to a Quad-Dominant mesh. This mode instructs the faceter to keep the generated display mesh (i.e., skip the tri-mesh to quad-dominant mesh conversion). 2 - Convert the triangular display mesh to a triangular mesh suitable for STL output, 3D printing or other similar application requiring a slightly higher quality triangular mesh. |
| VertexCount | Long | Output Long that returns the number of vertices that were generated. This is the number of vertices that will be returned by the VertexCoordinates argument. |
| FacetCount | Long | Output Long that returns the number of facets that were generated. |
| VertexCoordinates | Double | Output array of Doubles that contains the coordinate locations of the vertices. The values are defined in x, y, z order within the array and represent coordinates within the model space of the faceted object. |
| NormalVectors | Double | Output array of Doubles that defines the normal for each vertex in the facet mesh. The values are defined in x, y, z order within the array and represent vector components within the model space of the faceted object. |
| VertexIndices | Long | Output array of Longs that are used as index values to index into the vertex coordinate list. The first coordinate in the vertex coordinate list is index 1. Using vertex indices allows vertex coordinates to be reused by more than one triangle, thus reducing the overall resources required to define the entire mesh. |
| TextureCoordinates | Variant | Optional output array of Doubles that contains the coordinates of the texture map. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |