# TitleBlockDefinition Object

## Description

The TitleBlockDefinition object represents a title block definition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CopyTo](../TitleBlockDefinition/TitleBlockDefinition_CopyTo.md) | Method that copies the definition to the target drawing document. |
| [Delete](../TitleBlockDefinition/TitleBlockDefinition_Delete.md) | Method that deletes the TitleBlockDefinition object. This method will fail in the case where the definition is being referenced. This can be determined by using the IsReferenced property. |
| [Edit](../TitleBlockDefinition/TitleBlockDefinition_Edit.md) | Method that opens a copy of the title block definition's sketch for edit in the Sketch environment. Returns \Output DrawingSketch created by copying the sketch associated with the title block definition. |
| [ExitEdit](../TitleBlockDefinition/TitleBlockDefinition_ExitEdit.md) | Method that closes the currently active sketch (see below for limitations) and depending on the input parameters, replaces the sketch of the title block definition with the edited sketch. |
| [GetReferenceKey](../TitleBlockDefinition/TitleBlockDefinition_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TitleBlockDefinition/TitleBlockDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TitleBlockDefinition/TitleBlockDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [IsReferenced](../TitleBlockDefinition/TitleBlockDefinition_IsReferenced.md) | Property that specifies if the title block definition is being referenced or not. A title block definition is referenced whenever it is used on a sheet. A referenced title block definition cannot be deleted. |
| [Name](../TitleBlockDefinition/TitleBlockDefinition_Name.md) | Gets and sets the name of the title block definition. |
| [Parent](../TitleBlockDefinition/TitleBlockDefinition_Parent.md) | Property returning the parent . |
| [Sketch](../TitleBlockDefinition/TitleBlockDefinition_Sketch.md) | Property that returns the sketch associated with the title block definition. The DrawingSketch returned by the Sketch property supports all query functionality but cannot be edited. To edit the contents of a title block definition, use the Edit method. This creates a copy of the title block definition's sketch for edit. The ExitEdit method of the TitleBlockDefinition can then be used to save the edited sketch as the title block definition's sketch. |
| [Type](../TitleBlockDefinition/TitleBlockDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SheetFormat.ReferencedTitleBlockDefinition](../SheetFormat/SheetFormat_ReferencedTitleBlockDefinition.md), [TitleBlock.Definition](../TitleBlock/TitleBlock_Definition.md), [TitleBlockDefinition.CopyTo](../TitleBlockDefinition/TitleBlockDefinition_CopyTo.md), [TitleBlockDefinitions.Add](../TitleBlockDefinitions/TitleBlockDefinitions_Add.md), [TitleBlockDefinitions.Item](../TitleBlockDefinitions/TitleBlockDefinitions_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |
| [Copying a title block definition](../../sample-programs/TitleBlockDefinition_CopyTo_Sample.md) | This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |