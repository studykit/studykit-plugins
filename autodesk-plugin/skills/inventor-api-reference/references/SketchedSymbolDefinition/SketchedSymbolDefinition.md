# SketchedSymbolDefinition Object

## Description

The SketchedSymbolDefinition object represents a sketched symbol definition. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CopyTo](../SketchedSymbolDefinition/SketchedSymbolDefinition_CopyTo.md) | Method that copies the definition to the target drawing document. |
| [Delete](../SketchedSymbolDefinition/SketchedSymbolDefinition_Delete.md) | Method that deletes the SketchedSymbolDefinition object. This method will fail in the case where the definition is being referenced. This can be determined by using the IsReferenced property. |
| [Edit](../SketchedSymbolDefinition/SketchedSymbolDefinition_Edit.md) | Method that opens a copy of the sketched symbol definition's sketch for edit in the Sketch environment. The DrawingSketch returned is a new sketch that Autodesk Inventor creates by copying the sketch associated with the sketched symbol definition. Returns \Output DrawingSketch created by copying the sketch associated with the sketched symbol definition. |
| [ExitEdit](../SketchedSymbolDefinition/SketchedSymbolDefinition_ExitEdit.md) | Method that closes the currently active sketch (see below for limitations) and depending on the input parameters, replaces the sketch of the sketched symbol definition with the edited sketch. |
| [GetReferenceKey](../SketchedSymbolDefinition/SketchedSymbolDefinition_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToLibrary](../SketchedSymbolDefinition/SketchedSymbolDefinition_SaveToLibrary.md) | Saves the sketched symbol definition to the specified library. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchedSymbolDefinition/SketchedSymbolDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchedSymbolDefinition/SketchedSymbolDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [IsReferenced](../SketchedSymbolDefinition/SketchedSymbolDefinition_IsReferenced.md) | Property that specifies if the sketched symbol definition is being referenced or not. A sketched symbol definition is referenced when an instance of the definition has been placed. A referenced sketched symbol definition cannot be deleted. |
| [Name](../SketchedSymbolDefinition/SketchedSymbolDefinition_Name.md) | Gets and sets the name of the sketched symbol definition. |
| [Parent](../SketchedSymbolDefinition/SketchedSymbolDefinition_Parent.md) | Property returning the parent . |
| [Sketch](../SketchedSymbolDefinition/SketchedSymbolDefinition_Sketch.md) | Property that returns the sketch associated with the sketched symbol definition. The DrawingSketch returned by the Sketch property supports all query functionality but cannot be edited. To edit the contents of a sketched symbol definition, use the Edit method. This creates a copy of the sketched symbol definition's sketch for edit. The ExitEdit method of the SketchedSymbolDefinition can then be used to save the edited sketch as the sketched symbol definition's sketch. |
| [Thumbnail](../SketchedSymbolDefinition/SketchedSymbolDefinition_Thumbnail.md) | Returns the thumbnail of this objec. |
| [Type](../SketchedSymbolDefinition/SketchedSymbolDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchedSymbol.Definition](../SketchedSymbol/SketchedSymbol_Definition.md), [SketchedSymbolDefinition.CopyTo](../SketchedSymbolDefinition/SketchedSymbolDefinition_CopyTo.md), [SketchedSymbolDefinitions.Add](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_Add.md), [SketchedSymbolDefinitions.AddFromLibrary](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_AddFromLibrary.md), [SketchedSymbolDefinitions.Item](../SketchedSymbolDefinitions/SketchedSymbolDefinitions_Item.md)

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