# MiniToolbarControls.Item Property

Parent Object: [MiniToolbarControls](../MiniToolbarControls/MiniToolbarControls.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

MiniToolbarControls.**Item**( ***Index*** As Variant ) As [MiniToolbarControl](../MiniToolbarControl/MiniToolbarControl.md)

## Property Value

This is a read only property whose value is a [MiniToolbarControl](../MiniToolbarControl/MiniToolbarControl.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the MiniToolbarControl to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the InternalName of the MiniToolbarControl. If an out of range index or a name of a non-existent MiniToolbarControl is provided, an error will occur. |

## Version

Introduced in version 2012
