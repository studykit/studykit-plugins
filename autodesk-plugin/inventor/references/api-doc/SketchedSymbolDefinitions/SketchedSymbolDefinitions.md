# SketchedSymbolDefinitions Object

## Description

The SketchedSymbolDefinitions collection object provides access to all the existing objects in a drawing document and provides methods to create additional sketched symbol definitions. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_Add.md) | Method that creates a new sketched symbol definition. This method will fail in the case where a sketch is currently active. You can check for this case using the ActiveEditObject property of the Application object to see if a sketch is active. |
| [AddFromLibrary](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_AddFromLibrary.md) | Imports a new sketched symbol definition from library. |
| [SaveAllToLibrary](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_SaveAllToLibrary.md) | Saves all the sketched symbol definitions in current document to the specified library. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_Count.md) | Property that returns the number of items in the collection. |
| [Item](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_Item.md) | Method that returns the specified SketchedSymbolDefinition object from the collection. |
| [SketchedSymbolDefinitionLibraries](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_SketchedSymbolDefinitionLibraries.md) | Read-only property that returns the SketchedSymbolDefinitionLibraries collection object. |
| [Type](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingDocument.SketchedSymbolDefinitions](../DrawingDocument/DrawingDocument_SketchedSymbolDefinitions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |