# CommandControls.Item Property

Parent Object: [CommandControls](../CommandControls/CommandControls.md)

## Description

Returns the specified CommandControl object from the collection.

## Syntax

CommandControls.**Item**( ***Index*** As Variant ) As [CommandControl](../CommandControl/CommandControl.md)

## Property Value

This is a read only property whose value is a [CommandControl](../CommandControl/CommandControl.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the CommandControl to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the CommandControl name. If an out of range index or a name of a non-existent CommandControl is provided, an error will occur. |

## Version

Introduced in version 2010
