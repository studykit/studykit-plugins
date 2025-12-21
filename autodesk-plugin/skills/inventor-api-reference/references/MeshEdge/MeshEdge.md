# MeshEdge Object

## Description

MeshEdge Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../MeshEdge/MeshEdge_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeshEdge/MeshEdge_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Edge](../MeshEdge/MeshEdge_Edge.md) | Read-only property that returns the transient Brep Edge for the MeshEdge. |
| [Evaluator](../MeshEdge/MeshEdge_Evaluator.md) | Read-only property that returns the curve evaluator for this MeshEdge. This evaluator differs from the one that could be obtained from the surface geometry definition in that this evaluator accounts for the topological orientation. |
| [Geometry](../MeshEdge/MeshEdge_Geometry.md) | Read-only property that returns the underlying geometry of the MeshEdge. |
| [GeometryType](../MeshEdge/MeshEdge_GeometryType.md) | Read-only property that returns a curve type of the curve that will be returned from the Geometry property. |
| [MeshFeature](../MeshEdge/MeshEdge_MeshFeature.md) | Read-only property that returns the MeshFeature this MeshEdge is located on. |
| [MeshFeatureEntity](../MeshEdge/MeshEdge_MeshFeatureEntity.md) | Read-only property that returns the MeshFeatureEntity this MeshEdge is located on. |
| [Type](../MeshEdge/MeshEdge_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[MeshEdgeProxy.NativeObject](../MeshEdgeProxy/MeshEdgeProxy_NativeObject.md)

## Derived Classes

[MeshEdgeProxy](../MeshEdgeProxy/MeshEdgeProxy.md)

## Version

Introduced in version 2017
