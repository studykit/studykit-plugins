# ClientViews Object

## Description

The ClientViews collection object represents the collection of objects for a document/drawing sheet, along with the ability to add new views to the collection. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ClientViews/ClientViews_Add.md) | Method that adds a new to the collection. |
| [AddBySubset](../ClientViews/ClientViews_AddBySubset.md) | Add a new within a rectangular region of a window, identified by its hWnd. This allows multiple views in a single hWnd. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ClientViews/ClientViews_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ClientViews/ClientViews_Count.md) | Property that returns the number of items in this collection. |
| [Item](../ClientViews/ClientViews_Item.md) | Returns the specified object from the collection. This is the default property of the ClientViews collection object. |
| [Parent](../ClientViews/ClientViews_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Type](../ClientViews/ClientViews_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ApprenticeServerDocument.ClientViews](../ApprenticeServerDocument/ApprenticeServerDocument_ClientViews.md), [ApprenticeServerDrawingDocument.ClientViews](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ClientViews.md), [AssemblyDocument.ClientViews](../AssemblyDocument/AssemblyDocument_ClientViews.md), [ClientView.Parent](../ClientView/ClientView_Parent.md), [Document.ClientViews](../Document/Document_ClientViews.md), [DrawingDocument.ClientViews](../DrawingDocument/DrawingDocument_ClientViews.md), [PartDocument.ClientViews](../PartDocument/PartDocument_ClientViews.md), [PresentationDocument.ClientViews](../PresentationDocument/PresentationDocument_ClientViews.md), [Sheet.ClientViews](../Sheet/Sheet_ClientViews.md)

## Version

Introduced in version 6
