# SketchedSymbolDefinitions.SaveAllToLibrary Method

Parent Object: [SketchedSymbolDefinitions](../SketchedSymbolDefinitions/SketchedSymbolDefinitions.md)

## Description

Saves all the sketched symbol definitions in current document to the specified library.

## Syntax

SketchedSymbolDefinitions.**SaveAllToLibrary**( ***TargetSketchedSymbolDefinitionLibrary*** As Variant, [***RetainResourceFolderStructure***] As Variant, [***DestinationFolder***] As Variant, [***ReplaceExisting***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetSketchedSymbolDefinitionLibrary | Variant | Input SketchedSymbolDefinitionLibrary object or String that specifies the sketched symbol library name. |
| RetainResourceFolderStructure | Variant | Optional input Boolean that specifies whether retain resource folder structure when save sketched symbol definitions to the library. This defaults to True indicating the resource folder structure will be retained. |
| DestinationFolder | Variant | Optional input LibraryFolder that specifies destination folder to save the sketched symbol definition to.   This is an optional argument whose default value is null. |
| ReplaceExisting | Variant | Optional input Boolean that specifies whether replace the existing sketched symbol definitions in the library if they have same names with the definitions that are being saved to the library.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |