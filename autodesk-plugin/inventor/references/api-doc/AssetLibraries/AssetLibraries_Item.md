# AssetLibraries.Item Property

Parent Object: [AssetLibraries](../AssetLibraries/AssetLibraries.md)

## Description

Read-only property that returns the specified AssetLibrary object from the collection.

## Syntax

AssetLibraries.**Item**( ***Index*** As Variant ) As [AssetLibrary](../AssetLibrary/AssetLibrary.md)

## Property Value

This is a read only property whose value is an [AssetLibrary](../AssetLibrary/AssetLibrary.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the AssetLibrary to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the library name. The name specified can be either the name shown in the asset browser, the full filename, or the internal name of the libary. If an out of range index or a name of a non-existent library is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set the appearance of an occurrence.](../../sample-programs/SetOccurrenceAppearance_Sample.md) | Sets the appearance of a selected occurrence in an assembly. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |