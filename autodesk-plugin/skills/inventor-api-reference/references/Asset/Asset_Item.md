# Asset.Item Property

Parent Object: [Asset](../Asset/Asset.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

Asset.**Item**( ***Index*** As Variant ) As [AssetValue](../AssetValue/AssetValue.md)

## Property Value

This is a read only property whose value is an [AssetValue](../AssetValue/AssetValue.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the value to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the asset value name. If an out of range index or a name of a non-existent asset value is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a simple appearance.](../../sample-programs/CreateSimpleAppearance_Sample.md) | Creates a sample appearance in the active part or assembly document. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |