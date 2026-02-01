# ModelDatums.Item Property

Parent Object: [ModelDatums](../ModelDatums/ModelDatums.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelDatums.**Item**( ***Index*** As Variant ) As [ModelDatum](../ModelDatum/ModelDatum.md)

## Property Value

This is a read only property whose value is a [ModelDatum](../ModelDatum/ModelDatum.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ModelDatum to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ModelDatum name. If an out of range index or a name of a non-existent ModelDatum is provided, an error will occur. |

## Version

Introduced in version 2023
