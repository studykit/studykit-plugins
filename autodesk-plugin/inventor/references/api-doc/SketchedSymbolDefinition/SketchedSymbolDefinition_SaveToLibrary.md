# SketchedSymbolDefinition.SaveToLibrary Method

Parent Object: [SketchedSymbolDefinition](../SketchedSymbolDefinition/SketchedSymbolDefinition.md)

## Description

Saves the sketched symbol definition to the specified library.

## Syntax

SketchedSymbolDefinition.**SaveToLibrary**( ***TargetSketchedSymbolDefinitionLibrary*** As Variant, [***RetainResourceFolderStructure***] As Variant, [***DestinationFolder***] As Variant, [***ReplaceExisting***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetSketchedSymbolDefinitionLibrary | Variant | Input SketchedSymbolDefinitionLibrary object or String that specifies the sketched symbol library name. |
| RetainResourceFolderStructure | Variant | Optional input Boolean that specifies whether retain resource folder structure when save sketched symbol definition to the library. |
| DestinationFolder | Variant | Optional input LibraryFolder that specifies destination folder to save the sketched symbol definition to.   This is an optional argument whose default value is null. |
| ReplaceExisting | Variant | Optional input Boolean that specifies whether replace the existing sketched symbol definition in the library if it has same name with the definition that is being saved to the library.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketched Symbol Definition Library Creation](../../sample-programs/SketchedSymbolDefinitionLibraries_Add_Sample.md) | This sample demonstrates how to create a sketched symbol definition and save it to the SketchedSymbolDefinitionLibrary, and then add the sketched symbol definition from the SketchedSymbolDefinitionLibrary to another drawing document. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |