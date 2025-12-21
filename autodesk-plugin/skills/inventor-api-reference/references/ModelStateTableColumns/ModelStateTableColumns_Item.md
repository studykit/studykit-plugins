# ModelStateTableColumns.Item Property

Parent Object: [ModelStateTableColumns](../ModelStateTableColumns/ModelStateTableColumns.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelStateTableColumns.**Item**( ***Index*** As Variant ) As [ModelStateTableColumn](../ModelStateTableColumn/ModelStateTableColumn.md)

## Property Value

This is a read only property whose value is a [ModelStateTableColumn](../ModelStateTableColumn/ModelStateTableColumn.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ModelStateTableColumn to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the heading name. If an out-of-range index or a heading of a non-existent ModelStateTableColumn is provided, an error will occur. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |