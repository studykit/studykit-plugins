# FileDescriptorsEnumerator.Item Property

Parent Object: [FileDescriptorsEnumerator](../FileDescriptorsEnumerator/FileDescriptorsEnumerator.md)

## Description

Returns the specified FileDescriptor object from the collection.

## Syntax

FileDescriptorsEnumerator.**Item**( ***Index*** As Variant ) As [FileDescriptor](../FileDescriptor/FileDescriptor.md)

## Property Value

This is a read only property whose value is a [FileDescriptor](../FileDescriptor/FileDescriptor.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the FileDescriptor to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the full file name. If an out of range index or a name of a non-existent FileDescriptor is provided, an error will occur. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |