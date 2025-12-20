# TitleBlock Object

## Description

The TitleBlock object represents the instance of a title block on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TitleBlock/TitleBlock_Delete.md) | Method that deletes the title block from the sheet. |
| [GetResultText](../TitleBlock/TitleBlock_GetResultText.md) | Method that returns the text that is currently displayed for a specific text box. This is useful for text boxes that use input from other sources to define their content, i.e. properties and prompted text. The string displayed within this text box is returned. |
| [SetPromptResultText](../TitleBlock/TitleBlock_SetPromptResultText.md) | Method that sets the text that was supplied for a specified title block that contains prompted text. The string displayed within this title block is changed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TitleBlock/TitleBlock_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Definition](../TitleBlock/TitleBlock_Definition.md) | Property returning the title block definition object this title block is an instance of. |
| [Location](../TitleBlock/TitleBlock_Location.md) | Property that returns the position of the title block on the sheet. |
| [Name](../TitleBlock/TitleBlock_Name.md) | Gets and sets the name of the title block instance. |
| [Parent](../TitleBlock/TitleBlock_Parent.md) | Property returning the parent sheet object. |
| [Position](../TitleBlock/TitleBlock_Position.md) | Property that returns the position on the sheet where the origin of the title block definition's sketch is positioned. |
| [RangeBox](../TitleBlock/TitleBlock_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Transformation](../TitleBlock/TitleBlock_Transformation.md) | Property that provides the transform that is applied to display the associated title block definition in the correct location on the sheet. The matrix defines the sheet to title block transform. |
| [Type](../TitleBlock/TitleBlock_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.AddTitleBlock](../Sheet/Sheet_AddTitleBlock.md), [Sheet.TitleBlock](../Sheet/Sheet_TitleBlock.md)

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