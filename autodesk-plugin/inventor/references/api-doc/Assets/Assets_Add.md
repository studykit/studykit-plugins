# Assets.Add Method

Parent Object: [Assets](../Assets/Assets.md)

## Description

Method that creates a new asset. The new created Asset object is returned. Currently only material and appearance assets can be created. When a material asset is created a physical asset is automatically created that is associated with it that you can edit.

## Syntax

Assets.**Add**( ***AssetType*** As [AssetTypeEnum](../AssetTypeEnum.md), ***LocalType*** As String, [***Reserved***] As Variant, [***DisplayName***] As Variant ) As [Asset](../Asset/Asset.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AssetType | [AssetTypeEnum](../AssetTypeEnum.md) | The type of asset to be created, either an appearance or material asset. |
| LocalType | String | If the AssetType argument is kAssetAppearanceType, then you can specify the type of appearance asset you want to create. If a material asset is being created, this argument is ignored. If an appearance argument is being created and this argument is not provided it will default to creating a Generic type of appearance asset. The valid types of assets that can be created are: “Ceramic”, “Concrete”, “Generic”, “Glazing”, “Masonry”, “Metal”, “Metallic Paint”, “Mirror”, “Plastic”, “Solid Glass”, “Stone”, “Wall Paint”, “Water” and “Wood”. |
| Reserved | Variant | Reserved for future use. |
| DisplayName | Variant | Displayed name of the asset as shown to the user in the browser. If no name is specified, Inventor creates a default name.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Change color of part, features or faces](../../sample-programs/ChangeAppearanceUsingMiniToolbar_Sample.md) | This sample demonstrates how to use MiniToolBar to change appearance color of part or features or faces. |
| [Create a simple appearance.](../../sample-programs/CreateSimpleAppearance_Sample.md) | Creates a sample appearance in the active part or assembly document. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |