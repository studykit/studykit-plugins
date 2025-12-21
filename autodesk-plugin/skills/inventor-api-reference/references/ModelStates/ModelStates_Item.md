# ModelStates.Item Property

Parent Object: [ModelStates](../ModelStates/ModelStates.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelStates.**Item**( ***Index*** As Variant ) As [ModelState](../ModelState/ModelState.md)

## Property Value

This is a read only property whose value is a [ModelState](../ModelState/ModelState.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ModelState to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ModelState name. If an out-of-range index or a name of a non-existent ModelState is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Modify Multiple Model States Sample](../../sample-programs/ModifyMultipleModelStatesSample_Sample.md) | This sample demonstrates how to set multiple but not all model states into edit mode. |

## Version

Introduced in version 2022
