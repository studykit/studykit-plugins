# PresentationEdge Object

## Description

PresentationEdge Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CalculateStrokes](../PresentationEdge/PresentationEdge_CalculateStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. Client to deallocate pointers with CoTaskMemFree. |
| [CalculateStrokesWithOptions](../PresentationEdge/PresentationEdge_CalculateStrokesWithOptions.md) | Method that creates a new set of strokes within the specified conditions. |
| [GetExistingStrokes](../PresentationEdge/PresentationEdge_GetExistingStrokes.md) | Obtain the stroked or polygonal representation for the given chord-height tolerance. Fails if the tolerance supplied is not pre-existing. |
| [GetExistingStrokeTolerances](../PresentationEdge/PresentationEdge_GetExistingStrokeTolerances.md) | Obtain the set of chord-height tolerances for which this object already stores strokes. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PresentationEdge/PresentationEdge_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Evaluator](../PresentationEdge/PresentationEdge_Evaluator.md) | Read-only property that returns the CurveEvaluator for this presentation edge. |
| [Faces](../PresentationEdge/PresentationEdge_Faces.md) | Read-only property that returns the PresentationFace objects that are adjacent to this edge. |
| [Geometry](../PresentationEdge/PresentationEdge_Geometry.md) | Read-only property that returns the underlying geometry of the edge (e.g. Arc2D, Circle, Cone etc.). |
| [GeometryForm](../PresentationEdge/PresentationEdge_GeometryForm.md) | Read-only property that returns the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [GeometryType](../PresentationEdge/PresentationEdge_GeometryType.md) | Read-only property that returns the curve type of the curve that will be returned from the Geometry property. |
| [IsParamReversed](../PresentationEdge/PresentationEdge_IsParamReversed.md) | Read-only property that gets whether the parameterization of the geometry obtained from the Geometry property is aligned or opposed to the topological sense of this edge. |
| [Parent](../PresentationEdge/PresentationEdge_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PointOnEdge](../PresentationEdge/PresentationEdge_PointOnEdge.md) | Read-only property that returns a characteristic somewhere in the middle of the edge. |
| [StartVertex](../PresentationEdge/PresentationEdge_StartVertex.md) | Read-only property that returns the PresentationVertex object referenced at the start of this presentation edge. |
| [StopVertex](../PresentationEdge/PresentationEdge_StopVertex.md) | Read-only property that returns the PresentationVertex object referenced at the end of this presentation edge. |
| [Type](../PresentationEdge/PresentationEdge_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[PresentationEdgesEnumerator.Item](../PresentationEdgesEnumerator/PresentationEdgesEnumerator_Item.md)

## Version

Introduced in version 2018
