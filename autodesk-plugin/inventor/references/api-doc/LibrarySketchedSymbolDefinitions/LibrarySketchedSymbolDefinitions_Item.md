# LibrarySketchedSymbolDefinitions.Item Property

Parent Object: [LibrarySketchedSymbolDefinitions](../LibrarySketchedSymbolDefinitions/LibrarySketchedSymbolDefinitions.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

LibrarySketchedSymbolDefinitions.**Item**( ***Index*** As Variant ) As [LibrarySketchedSymbolDefinition](../LibrarySketchedSymbolDefinition/LibrarySketchedSymbolDefinition.md)

## Property Value

This is a read only property whose value is a [LibrarySketchedSymbolDefinition](../LibrarySketchedSymbolDefinition/LibrarySketchedSymbolDefinition.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the index of sketched symbol definition in the library. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the name of the sketched symbol definition. If an out of range index is specified, an error occurs. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |