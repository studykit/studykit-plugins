# SurfaceGraphicsEdge Object

## Description

The SurfaceGraphicsEdge represents an individual edge displayed by the SurfaceGraphics object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetCustomLineType](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [SetCustomLineType](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Color](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Color.md) | Gets and sets color associated with this primitive. |
| [Edge](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Edge.md) | Property that returns the Edge object associated with the SurfaceGraphicsEdge. |
| [Index](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Index.md) | Property that returns the index of the SurfaceGraphicsEdge object within the SurfaceGraphicsEdgeList. |
| [LineDefinitionSpace](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this surface graphics edge. |
| [LineScale](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_LineScale.md) | Gets and sets the LineScale applied to this surface graphics edge. |
| [LineType](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_LineType.md) | Property that gets and sets the line type override. Setting the property to kDefaultLineType restores the default line type. If the property returns kCustomLineType, the GetCustomLineType method can be used to get further details about the line type. |
| [LineWeight](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_LineWeight.md) | Gets and sets the LineWeight applied to this surface graphice edge. |
| [Parent](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Parent.md) | Property that returns the parent SurfaceGraphics object. |
| [Selectable](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Selectable.md) | Read-write property that specifies whether the surface graphics edge can be selected or not. |
| [Type](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SurfaceGraphicsEdgeList.Item](../SurfaceGraphicsEdgeList/SurfaceGraphicsEdgeList_Item.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |