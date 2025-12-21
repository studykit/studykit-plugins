# TransitionSymbolStylesEnumerator.Item Property

Parent Object: [TransitionSymbolStylesEnumerator](../TransitionSymbolStylesEnumerator/TransitionSymbolStylesEnumerator.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

TransitionSymbolStylesEnumerator.**Item**( ***Index*** As Variant ) As [TransitionSymbolStyle](../TransitionSymbolStyle/TransitionSymbolStyle.md)

## Property Value

This is a read only property whose value is a [TransitionSymbolStyle](../TransitionSymbolStyle/TransitionSymbolStyle.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the TransitionSymbolStyle to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the TransitionSymbolStyle name. If an out of range index or a name of a non-existent TransitionSymbolStyle is provided, an error will occur. |

## Version

Introduced in version 2025.1
