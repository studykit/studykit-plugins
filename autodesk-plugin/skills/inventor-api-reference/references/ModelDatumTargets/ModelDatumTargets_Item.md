# ModelDatumTargets.Item Property

Parent Object: [ModelDatumTargets](../ModelDatumTargets/ModelDatumTargets.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelDatumTargets.**Item**( ***Index*** As Variant ) As [ModelDatumTarget](../ModelDatumTarget/ModelDatumTarget.md)

## Property Value

This is a read only property whose value is a [ModelDatumTarget](../ModelDatumTarget/ModelDatumTarget.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ModelDatumTarget to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ModelDatumTarget name. If an out of range index or a name of a non-existent ModelDatumTarget is provided, an error will occur. |

## Version

Introduced in version 2023
