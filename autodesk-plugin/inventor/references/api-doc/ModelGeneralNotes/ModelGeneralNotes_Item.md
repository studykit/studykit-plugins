# ModelGeneralNotes.Item Property

Parent Object: [ModelGeneralNotes](../ModelGeneralNotes/ModelGeneralNotes.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelGeneralNotes.**Item**( ***Index*** As Variant ) As [ModelGeneralNote](../ModelGeneralNote/ModelGeneralNote.md)

## Property Value

This is a read only property whose value is a [ModelGeneralNote](../ModelGeneralNote/ModelGeneralNote.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the object to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the note name. If an out of range index or a name of a non-existent note is provided, an error occurs. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |