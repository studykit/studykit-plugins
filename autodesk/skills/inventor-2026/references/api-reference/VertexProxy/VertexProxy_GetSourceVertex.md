# VertexProxy.GetSourceVertex Method

Parent Object: [VertexProxy](../VertexProxy/VertexProxy.md)

## Description

Method that gets the source vertex that has been overridden by this vertex. The method returns Nothing if this vertex is not an override. An error is returned if this method is called on a vertex in a part.

## Syntax

VertexProxy.**GetSourceVertex**( [***GetLeafSource***] As Boolean ) As [Vertex](../Vertex/Vertex.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GetLeafSource | Boolean | Optional input Boolean that specifies whether to get the 'leaf' source vertex in the case where there are multiple levels of override. If specified to be False, the method returns the next level override vertex. If not specified, the argument defaults to True indicating that the leaf source will be returned. |

## Version

Introduced in version 10
