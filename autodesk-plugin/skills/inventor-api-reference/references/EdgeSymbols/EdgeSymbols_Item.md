# EdgeSymbols.Item Property

Parent Object: [EdgeSymbols](../EdgeSymbols/EdgeSymbols.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

EdgeSymbols.**Item**( ***Index*** As Long ) As [EdgeSymbol](../EdgeSymbol/EdgeSymbol.md)

## Property Value

This is a read only property whose value is an [EdgeSymbol](../EdgeSymbol/EdgeSymbol.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Variant value that specifies the EdgeSymbol to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the EdgeSymbol name. If an out of range index or a name of a non-existent EdgeSymbol is provided, an error will occur . |

## Version

Introduced in version 2024
