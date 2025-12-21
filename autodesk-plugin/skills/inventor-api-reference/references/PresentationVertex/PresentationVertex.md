# PresentationVertex Object

## Description

PresentationVertex Object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PresentationVertex/PresentationVertex_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Edges](../PresentationVertex/PresentationVertex_Edges.md) | Read-only property that returns the PresentationEdge objects that are adjacent to this vertex. |
| [Faces](../PresentationVertex/PresentationVertex_Faces.md) | Read-only property that returns the PresentationFace objects that are adjacent to this vertex. |
| [Parent](../PresentationVertex/PresentationVertex_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../PresentationVertex/PresentationVertex_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[PresentationEdge.StartVertex](../PresentationEdge/PresentationEdge_StartVertex.md), [PresentationEdge.StopVertex](../PresentationEdge/PresentationEdge_StopVertex.md), [PresentationVerticesEnumerator.Item](../PresentationVerticesEnumerator/PresentationVerticesEnumerator_Item.md)

## Version

Introduced in version 2018
