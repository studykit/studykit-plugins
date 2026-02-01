# MeshFeatureSet Object

## Description

MeshFeatureSet Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MeshFeatureSet/MeshFeatureSet_Delete.md) | Method that deletes the object. |
| [GetReferenceKey](../MeshFeatureSet/MeshFeatureSet_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |
| [SetEndOfPart](../MeshFeatureSet/MeshFeatureSet_SetEndOfPart.md) | Method that repositions the end of part marker relative to the object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeshFeatureSet/MeshFeatureSet_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../MeshFeatureSet/MeshFeatureSet_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [Count](../MeshFeatureSet/MeshFeatureSet_Count.md) | Gets the number of items in this collection. |
| [HealthStatus](../MeshFeatureSet/MeshFeatureSet_HealthStatus.md) | Read-only property that returns an enum indicating the current state of the object. |
| [Item](../MeshFeatureSet/MeshFeatureSet_Item.md) | Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well. |
| [Name](../MeshFeatureSet/MeshFeatureSet_Name.md) | Read-write property that gets and sets the name of the object. |
| [Parent](../MeshFeatureSet/MeshFeatureSet_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [RangeBox](../MeshFeatureSet/MeshFeatureSet_RangeBox.md) | Read-only property that returns the Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Suppressed](../MeshFeatureSet/MeshFeatureSet_Suppressed.md) | Read-write property that gets and sets the whether all of the mesh features within this set are suppressed or not. |
| [Type](../MeshFeatureSet/MeshFeatureSet_Type.md) | Gets the constant that indicates the type of this object. |
| [Visible](../MeshFeatureSet/MeshFeatureSet_Visible.md) | Read-write property that gets and sets whether all of the mesh features within this set are visible. |

## Accessed From

[MeshFeature.Parent](../MeshFeature/MeshFeature_Parent.md), [MeshFeatureProxy.Parent](../MeshFeatureProxy/MeshFeatureProxy_Parent.md), [MeshFeatureSetProxy.NativeObject](../MeshFeatureSetProxy/MeshFeatureSetProxy_NativeObject.md), [MeshFeatureSets.Add](../MeshFeatureSets/MeshFeatureSets_Add.md), [MeshFeatureSets.Item](../MeshFeatureSets/MeshFeatureSets_Item.md)

## Derived Classes

[MeshFeatureSetProxy](../MeshFeatureSetProxy/MeshFeatureSetProxy.md)

## Version

Introduced in version 2017
