# ModelHoleThreadNotes.Item Property

Parent Object: [ModelHoleThreadNotes](../ModelHoleThreadNotes/ModelHoleThreadNotes.md)

## Description

Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object.

## Syntax

ModelHoleThreadNotes.**Item**( ***Index*** As Variant ) As [ModelHoleThreadNote](../ModelHoleThreadNote/ModelHoleThreadNote.md)

## Property Value

This is a read only property whose value is a [ModelHoleThreadNote](../ModelHoleThreadNote/ModelHoleThreadNote.md).

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