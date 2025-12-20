# ContentTableRows.Add Method

Parent Object: [ContentTableRows](../ContentTableRows/ContentTableRows.md)

## Description

Method that creates a new row. Any changes to the table are not actually applied until the ContentFamily.Save method is called.

## Syntax

ContentTableRows.**Add**( ***RowData***() As String, [***Position***] As Long ) As [ContentTableRow](../ContentTableRow/ContentTableRow.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RowData | String | Input String array that contains the new values for the row. The array should be the same size as the number of columns and the values are defined in the same order as the column order. |
| Position | Long | Optional input Long that defines the position within the table where the new row should be created. If this argument is not supplied or is out of range the row will be created at the end of the table. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |