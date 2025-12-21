# AssetsEnumerator Object

## Description

The AssetsEnumerator collection object provides access to a set of assets.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssetsEnumerator/AssetsEnumerator_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../AssetsEnumerator/AssetsEnumerator_Count.md) | Gets the number of items in this collection. |
| [Item](../AssetsEnumerator/AssetsEnumerator_Item.md) | Read-only property that returns the specified Asset object from the collection. |
| [Type](../AssetsEnumerator/AssetsEnumerator_Type.md) | Read-only property returning kAssetsEnumeratorObject indicating this object’s type. |

## Accessed From

[Application.FavoriteAssets](../Application/Application_FavoriteAssets.md), [AssemblyDocument.AppearanceAssets](../AssemblyDocument/AssemblyDocument_AppearanceAssets.md), [AssemblyDocument.MaterialAssets](../AssemblyDocument/AssemblyDocument_MaterialAssets.md), [AssemblyDocument.PhysicalAssets](../AssemblyDocument/AssemblyDocument_PhysicalAssets.md), [AssetCategory.Assets](../AssetCategory/AssetCategory_Assets.md), [AssetLibrary.AppearanceAssets](../AssetLibrary/AssetLibrary_AppearanceAssets.md), [AssetLibrary.MaterialAssets](../AssetLibrary/AssetLibrary_MaterialAssets.md), [AssetLibrary.PhysicalAssets](../AssetLibrary/AssetLibrary_PhysicalAssets.md), [InventorServer.FavoriteAssets](InventorServer_FavoriteAssets.md), [InventorServerObject.FavoriteAssets](InventorServerObject_FavoriteAssets.md), [PartDocument.AppearanceAssets](../PartDocument/PartDocument_AppearanceAssets.md), [PartDocument.MaterialAssets](../PartDocument/PartDocument_MaterialAssets.md), [PartDocument.PhysicalAssets](../PartDocument/PartDocument_PhysicalAssets.md), [PresentationDocument.AppearanceAssets](../PresentationDocument/PresentationDocument_AppearanceAssets.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all materials to a file.](../../sample-programs/DumpAllMaterials_Sample.md) | This sample writes out information about all of the materials in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a material. |
| [Write out all physical properties to a file.](../../sample-programs/DumpAllPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a physical property. |
| [Write out all document appearances](../../sample-programs/DumpDocumentAppearances_Sample.md) | This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance. |
| [Write out all document materials to a file.](../../sample-programs/DumpDocumentMaterials_Sample.md) | This sample writes out information about all of the materials in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a material. |
| [Write out all document physical properties to a file.](../../sample-programs/DumpDocumentPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a physical property |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |