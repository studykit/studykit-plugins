# InventorVBAArguments.Item Property

Parent Object: [InventorVBAArguments](../InventorVBAArguments/InventorVBAArguments.md)

## Description

Returns the specified InventorVBAArgument object from the collection. This is the default property of the InventorVBAArguments collection object.

## Syntax

InventorVBAArguments.**Item**( ***Index*** As Variant ) As [InventorVBAArgument](../InventorVBAArgument/InventorVBAArgument.md)

## Property Value

This is a read only property whose value is an [InventorVBAArgument](../InventorVBAArgument/InventorVBAArgument.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the OccurrencePattern to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the pattern name. This is the name that is displayed to the user in the assembly browser. If an out of range index or a name of a non-existent occurrence name is provided, an error occurs. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |