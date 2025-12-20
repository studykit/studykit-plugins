# ModelWeldingSymbols.Item Property

Parent Object: [ModelWeldingSymbols](../ModelWeldingSymbols/ModelWeldingSymbols.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelWeldingSymbols.**Item**( ***Index*** As Variant ) As [ModelWeldingSymbol](../ModelWeldingSymbol/ModelWeldingSymbol.md)

## Property Value

This is a read only property whose value is a [ModelWeldingSymbol](../ModelWeldingSymbol/ModelWeldingSymbol.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the index of the ModelWeldingSymbol to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ModelWeldingSymbol name. If an out of range index or a name of a non-existent ModelWeldingSymbol is provided, an error will occur . |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |