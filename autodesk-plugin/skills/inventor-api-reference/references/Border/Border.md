# Border Object

## Description

The Border object represents the instance of a border on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Border/Border_Delete.md) | Method that deletes the title block from the sheet. |
| [GetResultText](../Border/Border_GetResultText.md) | Method that returns the text that is currently displayed for a specific text box. This is useful for text boxes that use input form other sources to define their content, i.e. properties and prompted text. The string displayed within this text box is returned. |
| [SetPromptResultText](../Border/Border_SetPromptResultText.md) | Method that sets the text that was supplied for a specified border that contains prompted text. The string displayed within this border is changed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Border/Border_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Definition](../Border/Border_Definition.md) | Property returning the border definition object that this border is an instance of. |
| [Name](../Border/Border_Name.md) | Gets and sets the name of the border instance. |
| [Parent](../Border/Border_Parent.md) | Property returning the parent sheet object. |
| [RangeBox](../Border/Border_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Type](../Border/Border_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.AddBorder](../Sheet/Sheet_AddBorder.md), [Sheet.Border](../Sheet/Sheet_Border.md)

## Derived Classes

[DefaultBorder](../DefaultBorder/DefaultBorder.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a parts list](../../sample-programs/PartsLists_Add_Sample.md) | This sample demonstrates the creation of a parts list. The parts list is placed at the top right corner of the border if one exists, else it is placed at the top right corner of the sheet. |
| [Border Insert](../../sample-programs/Sheet_AddDefaultBorder_Sample.md) | This sample illustrates inserting a default border. |
| [Border Insert Default](../../sample-programs/Sheet_AddDefaultBorder2_Sample.md) | This sample illustrates inserting a default border using the default values. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |