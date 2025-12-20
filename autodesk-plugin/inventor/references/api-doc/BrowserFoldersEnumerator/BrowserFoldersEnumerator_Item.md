# BrowserFoldersEnumerator.Item Property

Parent Object: [BrowserFoldersEnumerator](../BrowserFoldersEnumerator/BrowserFoldersEnumerator.md)

## Description

Returns the specified BrowserFolder object from the collection.

## Syntax

BrowserFoldersEnumerator.**Item**( ***Index*** As Variant ) As [BrowserFolder](../BrowserFolder/BrowserFolder.md)

## Property Value

This is a read only property whose value is a [BrowserFolder](../BrowserFolder/BrowserFolder.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the BrowserFolder to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the BrowserFolder label. If an out of range index or a label of a non-existent BrowserFolder is provided, an error will occur. If multiple folders in the collection share the same label, the first one found will be returned. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |