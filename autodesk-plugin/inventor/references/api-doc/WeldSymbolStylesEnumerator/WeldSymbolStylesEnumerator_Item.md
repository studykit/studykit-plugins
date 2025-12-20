# WeldSymbolStylesEnumerator.Item Property

Parent Object: [WeldSymbolStylesEnumerator](../WeldSymbolStylesEnumerator/WeldSymbolStylesEnumerator.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

WeldSymbolStylesEnumerator.**Item**( ***Index*** As Variant ) As [WeldSymbolStyle](../WeldSymbolStyle/WeldSymbolStyle.md)

## Property Value

This is a read only property whose value is a [WeldSymbolStyle](../WeldSymbolStyle/WeldSymbolStyle.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the WeldSymbolStyle to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the WeldSymbolStyle name. If an out of range index or a name of a non-existent WeldSymbolStyle is provided, an error will occur. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |