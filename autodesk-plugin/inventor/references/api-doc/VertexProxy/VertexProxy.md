# VertexProxy Object

Derived from: [Vertex](../Vertex/Vertex.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetPoint](../VertexProxy/VertexProxy_GetPoint.md) | Method that gets the coordinates of the vertex point. |
| [GetReferenceKey](../VertexProxy/VertexProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSourceVertex](../VertexProxy/VertexProxy_GetSourceVertex.md) | Method that gets the source vertex that has been overridden by this vertex. The method returns Nothing if this vertex is not an override. An error is returned if this method is called on a vertex in a part. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../VertexProxy/VertexProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../VertexProxy/VertexProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../VertexProxy/VertexProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Edges](../VertexProxy/VertexProxy_Edges.md) | Gets the  referenced by this Vertex. |
| [Faces](../VertexProxy/VertexProxy_Faces.md) | Property that returns the  that this Vertex is referenced from. |
| [IsTolerant](../VertexProxy/VertexProxy_IsTolerant.md) | Indicates if this vertex is using tolerant modeling to allow a non-exact model. |
| [NativeObject](../VertexProxy/VertexProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../VertexProxy/VertexProxy_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Point](../VertexProxy/VertexProxy_Point.md) | Property that returns a Point geometry object. The Point object returned provides information about the position of the vertex. |
| [Tolerance](../VertexProxy/VertexProxy_Tolerance.md) | Returns the tolerance being used for modeling calculations and this Vertex. |
| [TransientKey](../VertexProxy/VertexProxy_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview |
| [Type](../VertexProxy/VertexProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |