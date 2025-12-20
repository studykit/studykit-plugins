# RevisionTables.Add2 Method

Parent Object: [RevisionTables](../RevisionTables/RevisionTables.md)

## Description

Creates a new RevisionTable object on the sheet.

## Syntax

RevisionTables.**Add2**( ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), [***IsSheetScope***] As Boolean, [***AutoIndex***] As Boolean, [***AlphaIndex***] As Boolean, [***StartValue***] As String, [***RevisionTableStyle***] As Variant, [***Layer***] As Variant ) As [RevisionTable](../RevisionTable/RevisionTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the placement point of the revision table on the sheet. |
| IsSheetScope | Boolean | Optional input Boolean that specifies the scope of the revision table - False indicates sheet scope and True indicates the entire drawing scope. |
| AutoIndex | Boolean | Optional input Boolean that specifies whether to automatically index revision rows. If set to False, the revision cells remain blank. This value is ignored if a revision table of the same scope (drawing or sheet) has already been created.   This is an optional argument whose default value is True. |
| AlphaIndex | Boolean | Optional input Boolean that specifies whether the automatic indexing should be alphanumeric or numeric. Numeric by default. This value is ignored if AutoIndex is set to False or a revision table of the same scope (drawing or sheet) has already been created.   This is an optional argument whose default value is False. |
| StartValue | String | Optional input String that specifies the initial revision letter or number. This value is ignored if AutoIndex is set to False or a revision table of the same scope (drawing or sheet) has already been created.   This is an optional argument whose default value is "". |
| RevisionTableStyle | Variant | Optional input RevisionTableStyle object that specifies the style to use for the table. If not provided, the default style is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the revision table. If not provided, the default layer is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |