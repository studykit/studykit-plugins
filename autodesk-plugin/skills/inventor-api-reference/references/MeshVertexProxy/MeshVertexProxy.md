# MeshVertexProxy Object

Derived from: [MeshVertex](../MeshVertex/MeshVertex.md) Object

## Description

MeshVertexProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../MeshVertexProxy/MeshVertexProxy_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeshVertexProxy/MeshVertexProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [ContainingOccurrence](../MeshVertexProxy/MeshVertexProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Geometry](../MeshVertexProxy/MeshVertexProxy_Geometry.md) | Read-only property that returns the underlying geometry of the MeshEdge. |
| [MeshFeature](../MeshVertexProxy/MeshVertexProxy_MeshFeature.md) | Read-only property that returns the MeshFeature this MeshVertex is located on. |
| [MeshFeatureEntity](../MeshVertexProxy/MeshVertexProxy_MeshFeatureEntity.md) | Read-only property that returns the MeshFeatureEntity this MeshVertex is located on. |
| [NativeObject](../MeshVertexProxy/MeshVertexProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Type](../MeshVertexProxy/MeshVertexProxy_Type.md) | Gets the constant that indicates the type of this object. |

## Version

Introduced in version 2017
