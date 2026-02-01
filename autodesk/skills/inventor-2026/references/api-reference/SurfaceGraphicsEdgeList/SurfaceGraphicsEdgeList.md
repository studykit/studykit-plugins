# SurfaceGraphicsEdgeList Object

## Description

The SurfaceGraphicsEdgeList object contains a list of edges currently displayed by a SurfaceGraphics primitive and allows you to add edges to the list.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SurfaceGraphicsEdgeList/SurfaceGraphicsEdgeList_Add.md) | Method that specifies additional edges to be displayed. |
| [Clear](../SurfaceGraphicsEdgeList/SurfaceGraphicsEdgeList_Clear.md) | Method that removes all the edges from the list. No edges will be displayed after the method is called. |
| [Remove](../SurfaceGraphicsEdgeList/SurfaceGraphicsEdgeList_Remove.md) | Method that removes a edge from the list. The edge will no longer be displayed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SurfaceGraphicsEdgeList/SurfaceGraphicsEdgeList_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SurfaceGraphicsEdgeList/SurfaceGraphicsEdgeList_Count.md) | Property that returns the number of SurfaceGraphicsEdge objects in the list. |
| [Item](../SurfaceGraphicsEdgeList/SurfaceGraphicsEdgeList_Item.md) | Returns a SurfaeGraphicsEdge object. |
| [Type](../SurfaceGraphicsEdgeList/SurfaceGraphicsEdgeList_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ComponentGraphics.DisplayedEdges](../ComponentGraphics/ComponentGraphics_DisplayedEdges.md), [SurfaceGraphics.DisplayedEdges](../SurfaceGraphics/SurfaceGraphics_DisplayedEdges.md)

## Version

Introduced in version 2009
