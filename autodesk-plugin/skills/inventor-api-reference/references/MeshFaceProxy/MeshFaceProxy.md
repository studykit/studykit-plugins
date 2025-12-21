# MeshFaceProxy Object

Derived from: [MeshFace](../MeshFace/MeshFace.md) Object

## Description

MeshFaceProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../MeshFaceProxy/MeshFaceProxy_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeshFaceProxy/MeshFaceProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [ContainingOccurrence](../MeshFaceProxy/MeshFaceProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Evaluator](../MeshFaceProxy/MeshFaceProxy_Evaluator.md) | Read-only property that returns the surface evaluator for this MeshFace.This evaluator differs from the one that could be obtained from the surface geometry definition in that this evaluator accounts for the topological orientation. |
| [Face](../MeshFaceProxy/MeshFaceProxy_Face.md) | Read-only property that returns the transient Brep Face for the MeshFace. |
| [Geometry](../MeshFaceProxy/MeshFaceProxy_Geometry.md) | Read-only property that returns the underlying geometry of the MeshFace. |
| [MeshFeature](../MeshFaceProxy/MeshFaceProxy_MeshFeature.md) | Read-only property that returns the MeshFeature this MeshFace is located on. |
| [MeshFeatureEntity](../MeshFaceProxy/MeshFaceProxy_MeshFeatureEntity.md) | Read-only property that returns the MeshFeatureEntity this MeshFace is located on. |
| [NativeObject](../MeshFaceProxy/MeshFaceProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [SurfaceType](../MeshFaceProxy/MeshFaceProxy_SurfaceType.md) | Read-only property that returns a SurfaceTypeEnum that specifies the surface type for this MeshFace. |
| [Type](../MeshFaceProxy/MeshFaceProxy_Type.md) | Gets the constant that indicates the type of this object. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |