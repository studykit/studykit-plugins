# PresentationBody Object

## Description

PresentationBody Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CalculateFacets](../PresentationBody/PresentationBody_CalculateFacets.md) | Obtain the facetted representation for the given chord-height tolerance. If stored facets available for this tolerance, then those are returned. |
| [CalculateFacetsAndTextureMap](../PresentationBody/PresentationBody_CalculateFacetsAndTextureMap.md) | Obtain the facetted representation for the given chord-height tolerance. If stored facets available for this tolerance, then those are returned. |
| [CalculateFacetsWithOptions](../PresentationBody/PresentationBody_CalculateFacetsWithOptions.md) | Method that creates a new set of facets within the specified conditions. |
| [CalculateStrokes](../PresentationBody/PresentationBody_CalculateStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. Client to deallocate pointers with CoTaskMemFree. |
| [CalculateStrokesWithOptions](../PresentationBody/PresentationBody_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [GetExistingFacets](../PresentationBody/PresentationBody_GetExistingFacets.md) | Obtain the facetted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingFacetsAndTextureMap](../PresentationBody/PresentationBody_GetExistingFacetsAndTextureMap.md) | Obtain the facetted representation for the given chord-height tolerance as. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingFacetTolerances](../PresentationBody/PresentationBody_GetExistingFacetTolerances.md) | Obtain the set of chord-height tolerances for which this object already stores facets. |
| [GetExistingStrokes](../PresentationBody/PresentationBody_GetExistingStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingStrokeTolerances](../PresentationBody/PresentationBody_GetExistingStrokeTolerances.md) | Obtain the set of chord-height tolerances for which this object already stores strokes. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PresentationBody/PresentationBody_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Edges](../PresentationBody/PresentationBody_Edges.md) | Read-only property that returns all the PresentationEdge objects contained within the Presentation body. |
| [Faces](../PresentationBody/PresentationBody_Faces.md) | Read-only property that returns all the PresentationFace objects contained within the presentation body. |
| [Name](../PresentationBody/PresentationBody_Name.md) | Read-only property that gets the presentation body name. |
| [Parent](../PresentationBody/PresentationBody_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [RangeBox](../PresentationBody/PresentationBody_RangeBox.md) | Read-only property that returns the range box that represents the bounds of the presentation body. |
| [Type](../PresentationBody/PresentationBody_Type.md) | Gets the constant that indicates the type of this object. |
| [Vertices](../PresentationBody/PresentationBody_Vertices.md) | Read-only property that returns all the PresentationVertex objects contained within the presentation body. |

## Accessed From

[PresentationBodiesEnumerator.Item](../PresentationBodiesEnumerator/PresentationBodiesEnumerator_Item.md), [PresentationEdge.Parent](../PresentationEdge/PresentationEdge_Parent.md), [PresentationFace.Parent](../PresentationFace/PresentationFace_Parent.md), [PresentationFace.PresentationBody](../PresentationFace/PresentationFace_PresentationBody.md), [PresentationVertex.Parent](../PresentationVertex/PresentationVertex_Parent.md)

## Version

Introduced in version 2018
