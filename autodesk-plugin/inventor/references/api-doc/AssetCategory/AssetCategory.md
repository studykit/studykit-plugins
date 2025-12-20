# AssetCategory Object

## Description

The AssetCategory object represents a category within a library.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddAsset](../AssetCategory/AssetCategory_AddAsset.md) | Adds the specified asset to this category. The asset must exist in the same library as the category and the library must not be read-only. If the asset is already in another category, it will be moved to this category. |
| [Delete](../AssetCategory/AssetCategory_Delete.md) | Method that deletes this category from the library. Any assets associated with the category will also be deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssetCategory/AssetCategory_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Assets](../AssetCategory/AssetCategory_Assets.md) | Gets the assets associated with category. |
| [DisplayName](../AssetCategory/AssetCategory_DisplayName.md) | Gets and sets the name of this category as seen in the Material or Appearance Browser. |
| [Parent](../AssetCategory/AssetCategory_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../AssetCategory/AssetCategory_Type.md) | Read-only property returning kAssetCategoryObject indicating this object’s type. |

## Accessed From

[Asset.Category](../Asset/Asset_Category.md), [AssetCategories.Add](../AssetCategories/AssetCategories_Add.md), [AssetCategories.Item](../AssetCategories/AssetCategories_Item.md), [MaterialAsset.Category](../MaterialAsset/MaterialAsset_Category.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |