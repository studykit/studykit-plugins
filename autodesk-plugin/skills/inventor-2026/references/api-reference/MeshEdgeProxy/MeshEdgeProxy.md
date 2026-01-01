# MeshEdgeProxy Object

Derived from: [MeshEdge](../MeshEdge/MeshEdge.md) Object

## Description

MeshEdgeProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../MeshEdgeProxy/MeshEdgeProxy_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeshEdgeProxy/MeshEdgeProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [ContainingOccurrence](../MeshEdgeProxy/MeshEdgeProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Edge](../MeshEdgeProxy/MeshEdgeProxy_Edge.md) | Read-only property that returns the transient Brep Edge for the MeshEdge. |
| [Evaluator](../MeshEdgeProxy/MeshEdgeProxy_Evaluator.md) | Read-only property that returns the curve evaluator for this MeshEdge. This evaluator differs from the one that could be obtained from the surface geometry definition in that this evaluator accounts for the topological orientation. |
| [Geometry](../MeshEdgeProxy/MeshEdgeProxy_Geometry.md) | Read-only property that returns the underlying geometry of the MeshEdge. |
| [GeometryType](../MeshEdgeProxy/MeshEdgeProxy_GeometryType.md) | Read-only property that returns a curve type of the curve that will be returned from the Geometry property. |
| [MeshFeature](../MeshEdgeProxy/MeshEdgeProxy_MeshFeature.md) | Read-only property that returns the MeshFeature this MeshEdge is located on. |
| [MeshFeatureEntity](../MeshEdgeProxy/MeshEdgeProxy_MeshFeatureEntity.md) | Read-only property that returns the MeshFeatureEntity this MeshEdge is located on. |
| [NativeObject](../MeshEdgeProxy/MeshEdgeProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Type](../MeshEdgeProxy/MeshEdgeProxy_Type.md) | Gets the constant that indicates the type of this object. |

## Version

Introduced in version 2017
