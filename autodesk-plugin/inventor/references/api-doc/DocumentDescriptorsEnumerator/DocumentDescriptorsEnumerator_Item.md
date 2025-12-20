# DocumentDescriptorsEnumerator.Item Property

Parent Object: [DocumentDescriptorsEnumerator](../DocumentDescriptorsEnumerator/DocumentDescriptorsEnumerator.md)

## Description

Returns the specified DocumentDescriptor object from the collection.

## Syntax

DocumentDescriptorsEnumerator.**Item**( ***Index*** As Variant ) As [DocumentDescriptor](../DocumentDescriptor/DocumentDescriptor.md)

## Property Value

This is a read only property whose value is a [DocumentDescriptor](../DocumentDescriptor/DocumentDescriptor.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DocumentDescriptor to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the full document name. If an out of range index or a name of a non-existent DocumentDescriptor is provided, an error will occur. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |