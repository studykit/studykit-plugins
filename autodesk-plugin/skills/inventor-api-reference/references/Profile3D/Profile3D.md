# Profile3D Object

## Description

The Profile3D object defines a set of connected curves within a 3D sketch. The Profile3D object is used as input for various features that support 3D sketches as input, such as sweep and loft. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Profile3D/Profile3D_Delete.md) | Method that deletes this Profile3D object. |
| [GetReferenceKey](../Profile3D/Profile3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Profile3D/Profile3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../Profile3D/Profile3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Count](../Profile3D/Profile3D_Count.md) | Property that returns the number of items in the collection. |
| [Item](../Profile3D/Profile3D_Item.md) | Method that returns the specified ProfilePath3D object from the collection. |
| [Parent](../Profile3D/Profile3D_Parent.md) | Property that returns the 3D sketch that the profile was derived from. |
| [Type](../Profile3D/Profile3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Wires](../Profile3D/Profile3D_Wires.md) | Property returning the Wires collection object associated with this Profile3D. |

## Accessed From

[Profile3DProxy.NativeObject](../Profile3DProxy/Profile3DProxy_NativeObject.md), [ProfilePath3D.Parent](../ProfilePath3D/ProfilePath3D_Parent.md), [ProfilePath3DProxy.Parent](../ProfilePath3DProxy/ProfilePath3DProxy_Parent.md), [Profiles3D.AddClosed](../Profiles3D/Profiles3D_AddClosed.md), [Profiles3D.AddOpen](../Profiles3D/Profiles3D_AddOpen.md), [Profiles3D.Item](../Profiles3D/Profiles3D_Item.md)

## Derived Classes

[Profile3DProxy](../Profile3DProxy/Profile3DProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 6
