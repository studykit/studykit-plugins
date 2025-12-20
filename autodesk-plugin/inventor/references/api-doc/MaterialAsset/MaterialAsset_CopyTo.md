# MaterialAsset.CopyTo Method

Parent Object: [MaterialAsset](../MaterialAsset/MaterialAsset.md)

## Description

Method that copies this asset to the specified target and returns the new asset. A failure will occur if you attempt to replace the asset itself..

## Syntax

MaterialAsset.**CopyTo**( ***Target*** As Variant, [***ReplaceExisting***] As Variant ) As [Asset](../Asset/Asset.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Target | Variant | Input Variant value that specifies the target where the asset should be copied. Valid values are:  * AssetLibrary object - Copied to the asset library, assuming the library is not read only. * AssetCategory object - Copied to the category, assuming the associated library is not read-only. * Document object - Copied to the specified document.  The String “Favorites” - Copies it to the Favorites list of assets. |
| ReplaceExisting | Variant | Optional input Boolean that specifies whether replace the existing asset if an asset of the same name exists. If set to False, and an asset of the same name exists, this method creates a duplicate asset and returns the new asset. If the asset is a material asset that specify this value will either replace the existing material asset and its referenced appearance and physical assets, or duplicate all of them. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |