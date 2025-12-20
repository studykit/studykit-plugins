# iFeatureTableRow.Item Property

Parent Object: [iFeatureTableRow](../iFeatureTableRow/iFeatureTableRow.md)

## Description

Method that returns the specified iFeatureTableCell object from the row.

## Syntax

iFeatureTableRow.**Item**( ***Index*** As Variant ) As [iFeatureTableCell](../iFeatureTableCell/iFeatureTableCell.md)

## Property Value

This is a read only property whose value is an [iFeatureTableCell](../iFeatureTableCell/iFeatureTableCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Specifies the index of the iFeatureTableCell to return. The first column in the row has an index of 1. This can be either a numeric value indicating the index of the item in the collection, a string indicating the title of a column header, or a iFeatureTableColumn object. If an out of range index, a non-existent column header title, or an invalid iFeatureTableColumn object is specified, an error occurs. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |