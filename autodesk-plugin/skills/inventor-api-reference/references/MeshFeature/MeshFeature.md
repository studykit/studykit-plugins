# MeshFeature Object

## Description

MeshFeature Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MeshFeature/MeshFeature_Delete.md) | Method that deletes this object. |
| [GetReferenceKey](../MeshFeature/MeshFeature_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Appearance](../MeshFeature/MeshFeature_Appearance.md) | Read-write property that gets and sets the appearance of this object. |
| [AppearanceSourceType](../MeshFeature/MeshFeature_AppearanceSourceType.md) | Read-write property that gets and sets the source of the appearance for the object. |
| [Application](../MeshFeature/MeshFeature_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../MeshFeature/MeshFeature_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [Entities](../MeshFeature/MeshFeature_Entities.md) | Read-only property that returns the MeshFeatureEntitiesEnumerator collection object. |
| [HealthStatus](../MeshFeature/MeshFeature_HealthStatus.md) | Read-only property that returns an enum indicating the current state of the object. |
| [Name](../MeshFeature/MeshFeature_Name.md) | Mesh Feature Name. |
| [Parent](../MeshFeature/MeshFeature_Parent.md) | Read-only property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../MeshFeature/MeshFeature_RangeBox.md) | Read-only property that returns the Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Suppressed](../MeshFeature/MeshFeature_Suppressed.md) | Read-write property that gets and sets the whether this object is suppressed or not. |
| [Type](../MeshFeature/MeshFeature_Type.md) | Gets the constant that indicates the type of this object. |
| [Visible](../MeshFeature/MeshFeature_Visible.md) | Read-write property that gets and sets the visiblity of this object. |

## Accessed From

[MeshEdge.MeshFeature](../MeshEdge/MeshEdge_MeshFeature.md), [MeshEdgeProxy.MeshFeature](../MeshEdgeProxy/MeshEdgeProxy_MeshFeature.md), [MeshFace.MeshFeature](../MeshFace/MeshFace_MeshFeature.md), [MeshFaceProxy.MeshFeature](../MeshFaceProxy/MeshFaceProxy_MeshFeature.md), [MeshFeatureEntity.Parent](../MeshFeatureEntity/MeshFeatureEntity_Parent.md), [MeshFeatureEntityProxy.Parent](../MeshFeatureEntityProxy/MeshFeatureEntityProxy_Parent.md), [MeshFeatureProxy.NativeObject](../MeshFeatureProxy/MeshFeatureProxy_NativeObject.md), [MeshFeatureSet.Item](../MeshFeatureSet/MeshFeatureSet_Item.md), [MeshFeatureSetProxy.Item](../MeshFeatureSetProxy/MeshFeatureSetProxy_Item.md), [MeshVertex.MeshFeature](../MeshVertex/MeshVertex_MeshFeature.md), [MeshVertexProxy.MeshFeature](../MeshVertexProxy/MeshVertexProxy_MeshFeature.md)

## Derived Classes

[MeshFeatureProxy](../MeshFeatureProxy/MeshFeatureProxy.md)

## Version

Introduced in version 2017
