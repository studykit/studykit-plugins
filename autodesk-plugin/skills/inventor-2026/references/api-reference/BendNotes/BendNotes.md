# BendNotes Object

## Description

The BendNotes collection object provides access to all of the bend notes on the sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../BendNotes/BendNotes_Add.md) | Method that creates a bend note based on the input bend edge on the sheet. The initial placement of the bend note will be along the bend edge without a leader. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BendNotes/BendNotes_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../BendNotes/BendNotes_Count.md) | Property that returns the number of items in the collection. |
| [Item](../BendNotes/BendNotes_Item.md) | Returns the specified BendNote object from the collection. |
| [Type](../BendNotes/BendNotes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingNotes.BendNotes](../DrawingNotes/DrawingNotes_BendNotes.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create bend note](../../sample-programs/BendNotes_Add_Sample.md) | This sample demonstrates the creation of a bend note on the drawing view of a flat pattern. |

## Version

Introduced in version 2010
