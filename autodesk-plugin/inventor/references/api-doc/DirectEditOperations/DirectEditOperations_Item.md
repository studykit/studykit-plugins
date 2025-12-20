# DirectEditOperations.Item Property

Parent Object: [DirectEditOperations](../DirectEditOperations/DirectEditOperations.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

DirectEditOperations.**Item**( ***Index*** As Variant ) As [DirectEditOperation](../DirectEditOperation/DirectEditOperation.md)

## Property Value

This is a read only property whose value is a [DirectEditOperation](../DirectEditOperation/DirectEditOperation.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DirectEditOperation to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the DirectEditOperation name. If an out of range index or a name of a non-existent DirectEditOperation is provided, an error will occur. |

## Version

Introduced in version 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |