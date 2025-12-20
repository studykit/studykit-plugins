# FinishParameters.Item Property

Parent Object: [FinishParameters](../FinishParameters/FinishParameters.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

FinishParameters.**Item**( ***Value*** As Variant ) As [FinishParameter](../FinishParameter/FinishParameter.md)

## Property Value

This is a read only property whose value is a [FinishParameter](../FinishParameter/FinishParameter.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Value | Variant | Input Variant value that specifies the FinishParameter to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the parameter name. If an out of range index or a name of a non-existent parameter is provided, an error occurs. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |