# DrawingNotes Object

## Description

The DrawingNotes collection object provides access to all of the drawing notes on the sheet.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingNotes/DrawingNotes_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendNotes](../DrawingNotes/DrawingNotes_BendNotes.md) | Property that returns the collection of bend notes on the sheet. |
| [ChamferNotes](../DrawingNotes/DrawingNotes_ChamferNotes.md) | Property that returns the collection of chamfer notes on the sheet. |
| [Count](../DrawingNotes/DrawingNotes_Count.md) | Property that returns the number of items in the collection. |
| [GeneralNotes](../DrawingNotes/DrawingNotes_GeneralNotes.md) | Property that returns the collection of general notes on the sheet. |
| [HoleThreadNotes](../DrawingNotes/DrawingNotes_HoleThreadNotes.md) | Property that returns the collection of hole and thread notes on the sheet. |
| [Item](../DrawingNotes/DrawingNotes_Item.md) | Returns the specified DrawingNote object from the collection. |
| [LeaderNotes](../DrawingNotes/DrawingNotes_LeaderNotes.md) | Property that returns the collection of leader notes on the sheet. |
| [PunchNotes](../DrawingNotes/DrawingNotes_PunchNotes.md) | Property that returns the collection of punch notes on the sheet. |
| [Type](../DrawingNotes/DrawingNotes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.DrawingNotes](../Sheet/Sheet_DrawingNotes.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create bend note](../../sample-programs/BendNotes_Add_Sample.md) | This sample demonstrates the creation of a bend note on the drawing view of a flat pattern. |
| [Add a general note](../../sample-programs/GeneralNote_Sample.md) | This sample illustrates creating text (general note) in a sheet. |
| [Create thread note](../../sample-programs/HoleThreadNotes_Add_Sample.md) | This sample demonstrates the creation of a thread note on a drawing view. |
| [create punch note](../../sample-programs/PunchNotes_Add_Sample.md) | This sample demonstrates the creation of a punch note on the drawing view of a flat pattern. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |