# AssetLibraries Object

## Description

The AssetLibraries collection object provides access to the various asset libraries and also supports opening and migrating existing libraries, and creating new libraries. A library can contain both appearance and physical material assets.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../AssetLibraries/AssetLibraries_Add.md) | Method that creates a new asset library. The newly created AssetLibrary object is returned. The library can contain both appearance and material assets. |
| [MigrateInventorStyle](../AssetLibraries/AssetLibraries_MigrateInventorStyle.md) | Method that migrates existing inventor color and material styles into an existing or new library. |
| [Open](../AssetLibraries/AssetLibraries_Open.md) | Method that open an existing asset library. The opened AssetLibrary object is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssetLibraries/AssetLibraries_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../AssetLibraries/AssetLibraries_Count.md) | Gets the number of items in this collection. |
| [Item](../AssetLibraries/AssetLibraries_Item.md) | Read-only property that returns the specified AssetLibrary object from the collection. |
| [Type](../AssetLibraries/AssetLibraries_Type.md) | Read-only property returning kAssetLibrariesObject indicating this object’s type. |

## Accessed From

[Application.AssetLibraries](../Application/Application_AssetLibraries.md), [InventorServer.AssetLibraries](InventorServer_AssetLibraries.md), [InventorServerObject.AssetLibraries](InventorServerObject_AssetLibraries.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set the appearance of an occurrence.](../../sample-programs/SetOccurrenceAppearance_Sample.md) | Sets the appearance of a selected occurrence in an assembly. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |