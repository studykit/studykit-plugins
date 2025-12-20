# ModelGeneralNoteDefinition Object

## Description

The ModelGeneralNoteDefinition provides access to all of the information that defines a model leader note.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Copy.md) | Method that creates a copy of this LeaderModelNoteDefinition object. The new LeaderModelNoteDefinition object is independent of any leader note. It can edited and used as input to edit an existing note or to create a new note. |
| [SetToModelSpaceDisplay](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_SetToModelSpaceDisplay.md) | Sets the general note to be displayed in model space. This will set the OnScreen to be False. |
| [SetToOnScreenDisplay](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_SetToOnScreenDisplay.md) | Sets the general note to be displayed on screen. This will set the OnScreen to be True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_AnnotationPlane.md) | Read-write property that gets and sets the annotation plane for the dimension. |
| [AnnotationPlaneDefinition](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_AnnotationPlaneDefinition.md) | Read-write property that gets and sets the annotation plane definition for the dimension. |
| [Application](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Intent](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Intent.md) | Read-write property that gets and sets the geometric entity the note is attached to. |
| [OnScreen](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_OnScreen.md) | Gets whether the general note is displayed on screen. |
| [Parent](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Position](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Position.md) | Read-write property that gets and sets the position of the note in the part or assembly. The point is projected onto the orientation plane. |
| [ScreenQuadrant](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_ScreenQuadrant.md) | Gets or sets the location where the general note is displayed on screen. Setting this property is only applicable when the OnScreen returns True. |
| [ShowTextBorder](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_ShowTextBorder.md) | Read-write property that gets and sets whether to show the text border or not. |
| [SymbolDefinitions](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_SymbolDefinitions.md) | Returns the GeneralNoteSymbolDefinitions object, which allows you add model annotation definitions that can be used to display their symbols in the general note. |
| [Text](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Text.md) | Read-only property that returns an object that controls all of the text information associated with this note. Properties on the returned ModelAnnoationText object can be edited to change the displayed text. |
| [Type](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[GeneralNoteSymbolDefinition.Parent](../GeneralNoteSymbolDefinition/GeneralNoteSymbolDefinition_Parent.md), [ModelGeneralNote.Definition](../ModelGeneralNote/ModelGeneralNote_Definition.md), [ModelGeneralNoteDefinition.Copy](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Copy.md), [ModelGeneralNoteProxy.Definition](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_Definition.md), [ModelGeneralNotes.CreateDefinition](../ModelGeneralNotes/ModelGeneralNotes_CreateDefinition.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |