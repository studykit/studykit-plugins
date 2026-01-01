# SketchedSymbolDefinitionLibraries.Item Property

Parent Object: [SketchedSymbolDefinitionLibraries](../SketchedSymbolDefinitionLibraries/SketchedSymbolDefinitionLibraries.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

SketchedSymbolDefinitionLibraries.**Item**( ***Index*** As Variant ) As [SketchedSymbolDefinitionLibrary](../SketchedSymbolDefinitionLibrary/SketchedSymbolDefinitionLibrary.md)

## Property Value

This is a read only property whose value is a [SketchedSymbolDefinitionLibrary](../SketchedSymbolDefinitionLibrary/SketchedSymbolDefinitionLibrary.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the SketchedSymbolDefinitionLibrary to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the SketchedSymbolDefinitionLibrary’s name. If an out of range index or a name of a non-existent SketchedSymbolDefinitionLibrary is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketched Symbol Definition Library Creation](../../sample-programs/SketchedSymbolDefinitionLibraries_Add_Sample.md) | This sample demonstrates how to create a sketched symbol definition and save it to the SketchedSymbolDefinitionLibrary, and then add the sketched symbol definition from the SketchedSymbolDefinitionLibrary to another drawing document. |

## Version

Introduced in version 2016
