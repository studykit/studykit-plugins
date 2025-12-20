# iPartTableRows.Item Property

Parent Object: [iPartTableRows](../iPartTableRows/iPartTableRows.md)

## Description

Returns the specified iPartTableRow object from the collection. This is the default property of the iPartTableRows collection object.

## Syntax

iPartTableRows.**Item**( ***Index*** As Long ) As [iPartTableRow](../iPartTableRow/iPartTableRow.md)

## Property Value

This is a read only property whose value is an [iPartTableRow](../iPartTableRow/iPartTableRow.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Variant value that specifies the iPartTableRow to return. The input can be either an Integer value or a string. In the case of an Integer, the value specifies the row where the first row has in index of 1. If a string is input it should be in a part identifier format (i.e. ''[Height=1.000 in][Length=2.000 in][Radius=0.250 in]''). If the part specified does not exist an error occurs. This index value is not the same as the index value indicated in the user interface dialog. Rows in the dialog may be re-ordered. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |