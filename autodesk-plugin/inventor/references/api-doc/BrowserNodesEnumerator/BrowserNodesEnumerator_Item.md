# BrowserNodesEnumerator.Item Property

Parent Object: [BrowserNodesEnumerator](../BrowserNodesEnumerator/BrowserNodesEnumerator.md)

## Description

Returns the specified object from the collection.

## Syntax

BrowserNodesEnumerator.**Item**( ***Index*** As Variant ) As [BrowserNode](../BrowserNode/BrowserNode.md)

## Property Value

This is a read only property whose value is a [BrowserNode](../BrowserNode/BrowserNode.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the BrowserNode to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the BrowserNode label. If an out-of-range index or a label of a non-existent BrowserNode is provided, an error will occur. If multiple nodes in the collection share the same label, the first one found will be returned. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |