# Vertex Object

## Description

The Vertex object represents a transient point in boundary representation data.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetPoint](../Vertex/Vertex_GetPoint.md) | Method that gets the coordinates of the vertex point. |
| [GetReferenceKey](../Vertex/Vertex_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSourceVertex](../Vertex/Vertex_GetSourceVertex.md) | Method that gets the source vertex that has been overridden by this vertex. The method returns Nothing if this vertex is not an override. An error is returned if this method is called on a vertex in a part. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Vertex/Vertex_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../Vertex/Vertex_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Edges](../Vertex/Vertex_Edges.md) | Gets the  referenced by this Vertex. |
| [Faces](../Vertex/Vertex_Faces.md) | Property that returns the  that this Vertex is referenced from. |
| [IsTolerant](../Vertex/Vertex_IsTolerant.md) | Indicates if this vertex is using tolerant modeling to allow a non-exact model. |
| [Parent](../Vertex/Vertex_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Point](../Vertex/Vertex_Point.md) | Property that returns a Point geometry object. The Point object returned provides information about the position of the vertex. |
| [Tolerance](../Vertex/Vertex_Tolerance.md) | Returns the tolerance being used for modeling calculations and this Vertex. |
| [TransientKey](../Vertex/Vertex_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview |
| [Type](../Vertex/Vertex_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Edge.StartVertex](../Edge/Edge_StartVertex.md), [Edge.StopVertex](../Edge/Edge_StopVertex.md), [EdgeProxy.StartVertex](../EdgeProxy/EdgeProxy_StartVertex.md), [EdgeProxy.StopVertex](../EdgeProxy/EdgeProxy_StopVertex.md), [FilletSetbackVertex.Vertex](../FilletSetbackVertex/FilletSetbackVertex_Vertex.md), [SurfaceGraphicsVertex.Vertex](../SurfaceGraphicsVertex/SurfaceGraphicsVertex_Vertex.md), [UnwrapDefinition.Origin](../UnwrapDefinition/UnwrapDefinition_Origin.md), [Vertex.GetSourceVertex](../Vertex/Vertex_GetSourceVertex.md), [VertexProxy.GetSourceVertex](../VertexProxy/VertexProxy_GetSourceVertex.md), [VertexProxy.NativeObject](../VertexProxy/VertexProxy_NativeObject.md), [Vertices.Item](../Vertices/Vertices_Item.md)

## Derived Classes

[VertexProxy](../VertexProxy/VertexProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |

## Version

Introduced in version 4
