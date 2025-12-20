# InventorVBAComponents.Item Property

Parent Object: [InventorVBAComponents](../InventorVBAComponents/InventorVBAComponents.md)

## Description

Returns the specified InventorVBAComponent object from the collection. This is the default property of the InventorVBAComponents collection object.

## Syntax

InventorVBAComponents.**Item**( ***Index*** As Variant ) As [InventorVBAComponent](../InventorVBAComponent/InventorVBAComponent.md)

## Property Value

This is a read only property whose value is an [InventorVBAComponent](../InventorVBAComponent/InventorVBAComponent.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the InventorVBAComponent to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the component's name. If an out-of-range index or a name of a non-existent component name is provided, an error occurs. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |