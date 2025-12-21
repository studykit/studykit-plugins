# ModelSurfaceTextureSymbol.GetFilledAreaFacetsInfo Method

Parent Object: [ModelSurfaceTextureSymbol](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol.md)

## Description

Returns facets’ coordinates of the filled areas of the annotation.

## Syntax

ModelSurfaceTextureSymbol.**GetFilledAreaFacetsInfo**( ***Camera*** As [Camera](../Camera/Camera.md), ***TextVertexCount*** As Long, ***TextFacetCount*** As Long, ***TextVertexCoordinates***() As Double, ***TextVertexIndices***() As Long, ***SymbolVertexCount*** As Long, ***SymbolFacetCount*** As Long, ***SymbolVertexCoordinates***() As Double, ***SymbolVertexIndices***() As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Camera | [Camera](../Camera/Camera.md) | Input Camera object that specifies the view orientation. This can either be a transient Camera object or that got from View object etc.. And the camera properties can be changed but not applied. |
| TextVertexCount | Long | Output Long value that indicates vertex count of filled texts. |
| TextFacetCount | Long | Output Long value that indicates facet count of filled texts. |
| TextVertexCoordinates | Double | Output array of Doubles that indicates the vertices coordinates of the filled texts. The array is a single dimension array containing sequential x, y, z values. |
| TextVertexIndices | Long | Output array of Longs that are used as index values to index into the filled text vertex coordinate list. The first coordinate in the vertex coordinate list is index 1. Using vertex indices allows vertex coordinates to be reused by more than one triangle, thus reducing the overall resources required to define the entire mesh. |
| SymbolVertexCount | Long | Output Long value that indicates vertex count of filled symbols. |
| SymbolFacetCount | Long | Output Long value that indicates facet count of filled symbols. |
| SymbolVertexCoordinates | Double | Output array of Doubles that indicates the vertices coordinates of the filled symbols. The array is a single dimension array containing sequential x, y, z values. |
| SymbolVertexIndices | Long | Output array of Longs that are used as index values to index into the filled symbol vertex coordinate list. The first coordinate in the vertex coordinate list is index 1. Using vertex indices allows vertex coordinates to be reused by more than one triangle, thus reducing the overall resources required to define the entire mesh. |

## Version

Introduced in version 2018
