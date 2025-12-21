# FilesEnumerator.Item Property

Parent Object: [FilesEnumerator](../FilesEnumerator/FilesEnumerator.md)

## Description

Returns the specified File object from the collection.

## Syntax

FilesEnumerator.**Item**( ***Index*** As Variant ) As [File](../File/File.md)

## Property Value

This is a read only property whose value is a [File](../File/File.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the File to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the full file name. If an out of range index or a name of a non-existent File is provided, an error will occur. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |