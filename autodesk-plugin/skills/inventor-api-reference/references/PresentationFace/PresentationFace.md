# PresentationFace Object

## Description

PresentationFace Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CalculateFacets](../PresentationFace/PresentationFace_CalculateFacets.md) | Obtain the facetted representation for the given chord-height tolerance. If stored facets available for this tolerance, then those are returned. |
| [CalculateFacetsAndTextureMap](../PresentationFace/PresentationFace_CalculateFacetsAndTextureMap.md) | Obtain the facetted representation for the given chord-height tolerance. If stored facets available for this tolerance, then those are returned. |
| [CalculateFacetsWithOptions](../PresentationFace/PresentationFace_CalculateFacetsWithOptions.md) | Method that creates a new set of facets within the specified conditions. |
| [CalculateStrokes](../PresentationFace/PresentationFace_CalculateStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. Client to deallocate pointers with CoTaskMemFree. |
| [CalculateStrokesWithOptions](../PresentationFace/PresentationFace_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [GetExistingFacets](../PresentationFace/PresentationFace_GetExistingFacets.md) | Obtain the facetted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingFacetsAndTextureMap](../PresentationFace/PresentationFace_GetExistingFacetsAndTextureMap.md) | Obtain the facetted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingFacetTolerances](../PresentationFace/PresentationFace_GetExistingFacetTolerances.md) | Obtain the set of chord-height tolerances for which this object already stores facets. |
| [GetExistingStrokes](../PresentationFace/PresentationFace_GetExistingStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingStrokeTolerances](../PresentationFace/PresentationFace_GetExistingStrokeTolerances.md) | Obtain the set of chord-height tolerances for which this object already stores strokes. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PresentationFace/PresentationFace_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Edges](../PresentationFace/PresentationFace_Edges.md) | Read-only property that returns all the PresentationEdge objects contained within the presentation face. |
| [Evaluator](../PresentationFace/PresentationFace_Evaluator.md) | Read-only property that returns the SurfaceEvaluator for this presentation face. |
| [Geometry](../PresentationFace/PresentationFace_Geometry.md) | Read-only property that returns the underlying geometry of the face. |
| [GeometryForm](../PresentationFace/PresentationFace_GeometryForm.md) | Read-only property that returns the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [IsParamReversed](../PresentationFace/PresentationFace_IsParamReversed.md) | Read-only property that gets whether the parameterization of the geometry obtained from the Geometry property is aligned or opposed to the topological sense of this face. |
| [Parent](../PresentationFace/PresentationFace_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PointOnFace](../PresentationFace/PresentationFace_PointOnFace.md) | Read-only property that returns a characteristic somewhere on the interior of the face. |
| [PresentationBody](../PresentationFace/PresentationFace_PresentationBody.md) | Read-only property that returns the presentation body that this face is associative with. |
| [Type](../PresentationFace/PresentationFace_Type.md) | Gets the constant that indicates the type of this object. |
| [Vertices](../PresentationFace/PresentationFace_Vertices.md) | Read-only property that returns all the PresentationVertex objects contained within the presentation face. |

## Accessed From

[PresentationFacesEnumerator.Item](../PresentationFacesEnumerator/PresentationFacesEnumerator_Item.md)

## Version

Introduced in version 2018
