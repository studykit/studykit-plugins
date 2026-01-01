# GeneralNotes Object

## Description

GeneralNotes collection object provides access to all of the general notes on the sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByRectangle](../GeneralNotes/GeneralNotes_AddByRectangle.md) | Method that creates a general note whose size is defined by the input points that define opposing diagonals of the note. |
| [AddFitted](../GeneralNotes/GeneralNotes_AddFitted.md) | Method that creates a fitted general note positioned at the specified point on the sheet. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GeneralNotes/GeneralNotes_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../GeneralNotes/GeneralNotes_Count.md) | Property that returns the number of items in the collection. |
| [Item](../GeneralNotes/GeneralNotes_Item.md) | Returns the specified GeneralNote object from the collection. |
| [Type](../GeneralNotes/GeneralNotes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingNotes.GeneralNotes](../DrawingNotes/DrawingNotes_GeneralNotes.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a general note](../../sample-programs/GeneralNote_Sample.md) | This sample illustrates creating text (general note) in a sheet. |

## Version

Introduced in version 10
