# SketchedSymbolDefinitions.AddFromLibrary Method

Parent Object: [SketchedSymbolDefinitions](../SketchedSymbolDefinitions/SketchedSymbolDefinitions.md)

## Description

Imports a new sketched symbol definition from library.

## Syntax

SketchedSymbolDefinitions.**AddFromLibrary**( ***SketchedSymbolDefinitionLibrary*** As Variant, ***SketchedSymbolDefinitionName*** As String, [***ReplaceExisting***] As Variant ) As [SketchedSymbolDefinition](../SketchedSymbolDefinition/SketchedSymbolDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchedSymbolDefinitionLibrary | Variant | Input SketchedSymbolDefinitionLibrary object or String that specifies the sketched symbol library name. |
| SketchedSymbolDefinitionName | String | Input String that specifies the name of the sketched symbol definition in the library. |
| ReplaceExisting | Variant | Optional input Boolean that specifies whether replace the existing sketched symbol definition in the document if one with the same name is found in the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketched Symbol Definition Library Creation](../../sample-programs/SketchedSymbolDefinitionLibraries_Add_Sample.md) | This sample demonstrates how to create a sketched symbol definition and save it to the SketchedSymbolDefinitionLibrary, and then add the sketched symbol definition from the SketchedSymbolDefinitionLibrary to another drawing document. |

## Version

Introduced in version 2016
