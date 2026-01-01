# Sheets Object

## Description

The Sheets collection object provides access to all the existing objects in a drawing document and provides methods to create additional sheets. See here for an overview on drawing views.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../Sheets/Sheets_Add.md) | Method that creates a new Sheet. |
| [AddUsingSheetFormat](../Sheets/Sheets_AddUsingSheetFormat.md) | Method that creates a new Sheet based on the input format. The newly created Sheet is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Sheets/Sheets_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../Sheets/Sheets_Count.md) | Property that returns the number of items in this collection. |
| [Item](../Sheets/Sheets_Item.md) | Returns the specified Sheet object from the collection. |
| [Type](../Sheets/Sheets_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ApprenticeServerDrawingDocument.Sheets](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_Sheets.md), [DrawingDocument.Sheets](../DrawingDocument/DrawingDocument_Sheets.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Copying a title block definition](../../sample-programs/TitleBlockDefinition_CopyTo_Sample.md) | This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block. |

## Version

Introduced in version 4
