# Asset.Category Property

Parent Object: [Asset](../Asset/Asset.md)

## Description

Gets the category that this asset is a member of. A value of Nothing indicates this asset is not a member of a category. A value of Nothing is also returned when an Asset is associated with a document, rather than a library. Categories don’t exist in a documen.

## Syntax

Asset.**Category**() As [AssetCategory](../AssetCategory/AssetCategory.md)

## Property Value

This is a read/write property whose value is an [AssetCategory](../AssetCategory/AssetCategory.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all physical properties to a file.](../../sample-programs/DumpAllPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a physical property. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |