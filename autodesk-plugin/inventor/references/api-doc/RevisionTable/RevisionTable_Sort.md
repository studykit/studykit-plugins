# RevisionTable.Sort Method

Parent Object: [RevisionTable](../RevisionTable/RevisionTable.md)

## Description

Changes the sort order of rows in the revision table.

## Syntax

RevisionTable.**Sort**( ***PrimaryColumnTitle*** As String, [***PrimaryColumnAscending***] As Boolean, [***SecondaryColumnTitle***] As String, [***SecondaryColumnAscending***] As Boolean, [***TertiaryColumnTitle***] As String, [***TertiaryColumnAscending***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PrimaryColumnTitle | String | Input string that specifies the primary column to use for the sorting. If the name of a non-existing column is provided, an error occurs. |
| PrimaryColumnAscending | Boolean | Optional input Boolean that specifies whether to sort from the lowest value to the highest or vice versa. If not specified, a default value of True is used indicating that the sorting will be from the lowest value to the highest. |
| SecondaryColumnTitle | String | Optional input string that specifies the secondary column to use for the sorting. If the name of a non-existing column or the primary column is provided, an error occurs.   This is an optional argument whose default value is "". |
| SecondaryColumnAscending | Boolean | Optional input Boolean that specifies whether to sort from the lowest value to the highest or vice versa. If not specified, a default value of True is used indicating that the sorting will be from the lowest value to the highest.   This is an optional argument whose default value is True. |
| TertiaryColumnTitle | String | Optional input string that specifies the tertiary column to use for the sorting. If the name of a non-existing column, the primary column or the secondary column is provided, an error occurs.   This is an optional argument whose default value is "". |
| TertiaryColumnAscending | Boolean | Optional input Boolean that specifies whether to sort from the lowest value to the highest or vice versa. If not specified, a default value of True is used indicating that the sorting will be from the lowest value to the highest.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |