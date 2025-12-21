# MeshFace Object

## Description

MeshFace Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../MeshFace/MeshFace_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeshFace/MeshFace_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Evaluator](../MeshFace/MeshFace_Evaluator.md) | Read-only property that returns the surface evaluator for this MeshFace.This evaluator differs from the one that could be obtained from the surface geometry definition in that this evaluator accounts for the topological orientation. |
| [Face](../MeshFace/MeshFace_Face.md) | Read-only property that returns the transient Brep Face for the MeshFace. |
| [Geometry](../MeshFace/MeshFace_Geometry.md) | Read-only property that returns the underlying geometry of the MeshFace. |
| [MeshFeature](../MeshFace/MeshFace_MeshFeature.md) | Read-only property that returns the MeshFeature this MeshFace is located on. |
| [MeshFeatureEntity](../MeshFace/MeshFace_MeshFeatureEntity.md) | Read-only property that returns the MeshFeatureEntity this MeshFace is located on. |
| [SurfaceType](../MeshFace/MeshFace_SurfaceType.md) | Read-only property that returns a SurfaceTypeEnum that specifies the surface type for this MeshFace. |
| [Type](../MeshFace/MeshFace_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[MeshFaceProxy.NativeObject](../MeshFaceProxy/MeshFaceProxy_NativeObject.md)

## Derived Classes

[MeshFaceProxy](../MeshFaceProxy/MeshFaceProxy.md)

## Version

Introduced in version 2017
