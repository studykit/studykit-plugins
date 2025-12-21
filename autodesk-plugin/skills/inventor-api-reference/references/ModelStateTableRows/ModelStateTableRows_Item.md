# ModelStateTableRows.Item Property

Parent Object: [ModelStateTableRows](../ModelStateTableRows/ModelStateTableRows.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelStateTableRows.**Item**( ***Index*** As Variant ) As [ModelStateTableRow](../ModelStateTableRow/ModelStateTableRow.md)

## Property Value

This is a read only property whose value is a [ModelStateTableRow](../ModelStateTableRow/ModelStateTableRow.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ModelStateTableRow to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the member name. If an out-of-range index or a name of a non-existent ModelStateTableRow is provided, an error will occur. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |