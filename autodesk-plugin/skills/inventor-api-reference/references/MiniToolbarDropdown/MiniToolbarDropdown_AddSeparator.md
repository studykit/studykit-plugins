# MiniToolbarDropdown.AddSeparator Method

Parent Object: [MiniToolbarDropdown](../MiniToolbarDropdown/MiniToolbarDropdown.md)

## Description

Method that adds a separator to the control.

## Syntax

MiniToolbarDropdown.**AddSeparator**( [***InternalName***] As String, [***Index***] As Long ) As [MiniToolbarListItem](../MiniToolbarListItem/MiniToolbarListItem.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that specifies an internal name for the control. You can provide this for convenience in identifying the item at a later time. If provided, it must be unique with respect to all other items in this drop down. |
| Index | Long | Optional input Long value that specifies the 1-based index at which to add the separator. If not specified, the separator is added at the end.   This is an optional argument whose default value is 0. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |