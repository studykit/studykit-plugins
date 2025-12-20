# MiniToolbarComboBox.Item Property

Parent Object: [MiniToolbarComboBox](../MiniToolbarComboBox/MiniToolbarComboBox.md)

## Description

Returns the text of the specified item or the name of the specified separator from the combobox.

## Syntax

MiniToolbarComboBox.**Item**( ***Index*** As Variant ) As [MiniToolbarListItem](../MiniToolbarListItem/MiniToolbarListItem.md)

## Property Value

This is a read only property whose value is a [MiniToolbarListItem](../MiniToolbarListItem/MiniToolbarListItem.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the item to return. This can be a numeric value indicating the index of the item in the combobox or it can be a string that is the internal name of the item. If an out of range index is provided or a name that doesn’t exist, an error will occur. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |