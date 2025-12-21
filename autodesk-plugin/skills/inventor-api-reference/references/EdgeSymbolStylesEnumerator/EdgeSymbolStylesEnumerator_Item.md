# EdgeSymbolStylesEnumerator.Item Property

Parent Object: [EdgeSymbolStylesEnumerator](../EdgeSymbolStylesEnumerator/EdgeSymbolStylesEnumerator.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

EdgeSymbolStylesEnumerator.**Item**( ***Index*** As Variant ) As [EdgeSymbolStyle](../EdgeSymbolStyle/EdgeSymbolStyle.md)

## Property Value

This is a read only property whose value is an [EdgeSymbolStyle](../EdgeSymbolStyle/EdgeSymbolStyle.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the EdgeSymbolStyle to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the EdgeSymbolStyle name. If an out of range index or a name of a non-existent EdgeSymbolStyle is provided, an error will occur. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |