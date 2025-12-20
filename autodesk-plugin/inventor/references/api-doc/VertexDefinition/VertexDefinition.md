# VertexDefinition Object

## Description

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../VertexDefinition/VertexDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssociativeID](../VertexDefinition/VertexDefinition_AssociativeID.md) | Gets and sets the associate ID of this vertex. This ID will be transferred to the corresponding vertex when this SurfaceBodyDefinition is used to create a SurfaceBody. It is used by Inventor as the identifier for the vertex and is used for tracking this geom. |
| [Position](../VertexDefinition/VertexDefinition_Position.md) | Gets and sets the defined location of the vertex. |
| [Type](../VertexDefinition/VertexDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[EdgeDefinition.EndVertex](../EdgeDefinition/EdgeDefinition_EndVertex.md), [EdgeDefinition.StartVertex](../EdgeDefinition/EdgeDefinition_StartVertex.md), [VertexDefinitions.Add](../VertexDefinitions/VertexDefinitions_Add.md), [VertexDefinitions.Item](../VertexDefinitions/VertexDefinitions_Item.md), [WireEdgeDefinition.EndVertex](../WireEdgeDefinition/WireEdgeDefinition_EndVertex.md), [WireEdgeDefinition.StartVertex](../WireEdgeDefinition/WireEdgeDefinition_StartVertex.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |