# MeshVertex Object

## Description

MeshVertex Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../MeshVertex/MeshVertex_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeshVertex/MeshVertex_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Geometry](../MeshVertex/MeshVertex_Geometry.md) | Read-only property that returns the underlying geometry of the MeshEdge. |
| [MeshFeature](../MeshVertex/MeshVertex_MeshFeature.md) | Read-only property that returns the MeshFeature this MeshVertex is located on. |
| [MeshFeatureEntity](../MeshVertex/MeshVertex_MeshFeatureEntity.md) | Read-only property that returns the MeshFeatureEntity this MeshVertex is located on. |
| [Type](../MeshVertex/MeshVertex_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[MeshVertexProxy.NativeObject](../MeshVertexProxy/MeshVertexProxy_NativeObject.md)

## Derived Classes

[MeshVertexProxy](../MeshVertexProxy/MeshVertexProxy.md)

## Version

Introduced in version 2017
