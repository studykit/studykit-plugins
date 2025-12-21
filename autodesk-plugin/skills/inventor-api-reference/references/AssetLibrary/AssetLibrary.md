# AssetLibrary Object

## Description

The AssetLibrary object represents a material and appearance library which exists as a .asdklib file. A library can contain both appearance and physical material information.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Remove](../AssetLibrary/AssetLibrary_Remove.md) | Method that removes the library from the set of loaded libraries. The associated .adsklib file is not affected. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AppearanceAssetCategories](../AssetLibrary/AssetLibrary_AppearanceAssetCategories.md) | Gets the AssetCategories collection which provides access to the appearance related categories defined within this library. |
| [AppearanceAssets](../AssetLibrary/AssetLibrary_AppearanceAssets.md) | Gets an Assets collection which provides access to all of the appearance assets in this library. |
| [Application](../AssetLibrary/AssetLibrary_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DisplayName](../AssetLibrary/AssetLibrary_DisplayName.md) | Gets and sets the name of this library as seen in the Material or Appearance Browser. |
| [FullFileName](../AssetLibrary/AssetLibrary_FullFileName.md) | Gets the full filename of this library. |
| [InternalName](../AssetLibrary/AssetLibrary_InternalName.md) | Gets the unique internal name of this library. |
| [IsReadOnly](../AssetLibrary/AssetLibrary_IsReadOnly.md) | Gets the boolean flag that indicates if this library is read-only. If True any attempted edits will fail. |
| [MaterialAssetCategories](../AssetLibrary/AssetLibrary_MaterialAssetCategories.md) | Gets the AssetCategories collection which provides access to the material related categories defined within this library. |
| [MaterialAssets](../AssetLibrary/AssetLibrary_MaterialAssets.md) | Gets the Assets collection which provides access to all of the materials in this library. |
| [PhysicalAssets](../AssetLibrary/AssetLibrary_PhysicalAssets.md) | Gets an Assets collection which provides access to all of the physical assets in this library. A physical asset defines the physical properties that are associated with a material. |
| [Type](../AssetLibrary/AssetLibrary_Type.md) | Read-only property returning kAssetLibraryObject indicating this object’s type. |

## Accessed From

[Application.ActiveAppearanceLibrary](../Application/Application_ActiveAppearanceLibrary.md), [Application.ActiveMaterialLibrary](../Application/Application_ActiveMaterialLibrary.md), [AssetCategory.Parent](../AssetCategory/AssetCategory_Parent.md), [AssetLibraries.Add](../AssetLibraries/AssetLibraries_Add.md), [AssetLibraries.Item](../AssetLibraries/AssetLibraries_Item.md), [AssetLibraries.Open](../AssetLibraries/AssetLibraries_Open.md), [InventorServer.ActiveAppearanceLibrary](InventorServer_ActiveAppearanceLibrary.md), [InventorServer.ActiveMaterialLibrary](InventorServer_ActiveMaterialLibrary.md), [InventorServerObject.ActiveAppearanceLibrary](InventorServerObject_ActiveAppearanceLibrary.md), [InventorServerObject.ActiveMaterialLibrary](InventorServerObject_ActiveMaterialLibrary.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all materials to a file.](../../sample-programs/DumpAllMaterials_Sample.md) | This sample writes out information about all of the materials in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a material. |
| [Write out all physical properties to a file.](../../sample-programs/DumpAllPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a physical property. |
| [Set the appearance of an occurrence.](../../sample-programs/SetOccurrenceAppearance_Sample.md) | Sets the appearance of a selected occurrence in an assembly. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |