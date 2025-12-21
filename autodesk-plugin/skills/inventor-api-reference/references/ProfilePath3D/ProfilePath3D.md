# ProfilePath3D Object

## Description

The ProfilePath3D object represents a single set of connected 3D curves. The order of the collection defines the connected order of the entities.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../ProfilePath3D/ProfilePath3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProfilePath3D/ProfilePath3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProfilePath3D/ProfilePath3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../ProfilePath3D/ProfilePath3D_Closed.md) | Property that returns a Boolean indicating if the path is closed or not. Returns True in the case of a closed path. |
| [Count](../ProfilePath3D/ProfilePath3D_Count.md) | Property that returns the number of items in the collection. |
| [Item](../ProfilePath3D/ProfilePath3D_Item.md) | Method that returns the specified ProfileEntity3D object from the collection. |
| [Parent](../ProfilePath3D/ProfilePath3D_Parent.md) | Property that returns the parent Profile3D. |
| [Type](../ProfilePath3D/ProfilePath3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Profile3D.Item](../Profile3D/Profile3D_Item.md), [Profile3DProxy.Item](../Profile3DProxy/Profile3DProxy_Item.md), [ProfileEntity3D.Parent](../ProfileEntity3D/ProfileEntity3D_Parent.md), [ProfileEntity3DProxy.Parent](../ProfileEntity3DProxy/ProfileEntity3DProxy_Parent.md), [ProfilePath3DProxy.NativeObject](../ProfilePath3DProxy/ProfilePath3DProxy_NativeObject.md)

## Derived Classes

[ProfilePath3DProxy](../ProfilePath3DProxy/ProfilePath3DProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |