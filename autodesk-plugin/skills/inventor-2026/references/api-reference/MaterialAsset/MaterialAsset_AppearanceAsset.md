# MaterialAsset.AppearanceAsset Property

Parent Object: [MaterialAsset](../MaterialAsset/MaterialAsset.md)

## Description

Gets and sets the appearance associated with the material. When assigning an appearance, the appearance must exist in the same document as the material.

## Syntax

MaterialAsset.**AppearanceAsset**() As [Asset](../Asset/Asset.md)

## Property Value

This is a read/write property whose value is an [Asset](../Asset/Asset.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all materials to a file.](../../sample-programs/DumpAllMaterials_Sample.md) | This sample writes out information about all of the materials in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a material. |
| [Write out all document materials to a file.](../../sample-programs/DumpDocumentMaterials_Sample.md) | This sample writes out information about all of the materials in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a material. |

## Version

Introduced in version 2014
