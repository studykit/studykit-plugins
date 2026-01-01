# MiniToolbarDropdown.Item Property

Parent Object: [MiniToolbarDropdown](../MiniToolbarDropdown/MiniToolbarDropdown.md)

## Description

Returns the display name of the specified item from the dropdown.

## Syntax

MiniToolbarDropdown.**Item**( ***Index*** As Variant ) As [MiniToolbarListItem](../MiniToolbarListItem/MiniToolbarListItem.md)

## Property Value

This is a read only property whose value is a [MiniToolbarListItem](../MiniToolbarListItem/MiniToolbarListItem.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the item to remove. This can be a numeric value indicating the index of the item in the list or it can be a string that is the internal name of the item. If an out of range index is provided or a name that doesn’t exist, an error will occur. |

## Version

Introduced in version 2012
