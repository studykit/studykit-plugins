# ClientView Object

## Description

The ClientView object represents a view of the document/drawing sheet attached to a user-specified window handle. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Close](../ClientView/ClientView_Close.md) | Method that closes out the graphics context for the view. The hWnd is not affected. |
| [GetSubsetExtents](../ClientView/ClientView_GetSubsetExtents.md) | Method that returns the extents of the client view within its assigned hWnd. |
| [Update](../ClientView/ClientView_Update.md) | Method that redraws the view. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ClientView/ClientView_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Camera](../ClientView/ClientView_Camera.md) | Property that returns the camera for the view. |
| [DisplayMode](../ClientView/ClientView_DisplayMode.md) | Rendering mode of view (shaded, hidden, hidden line). |
| [Document](../ClientView/ClientView_Document.md) | Property that returns the document object this is a view of. |
| [GroundShadow](../ClientView/ClientView_GroundShadow.md) | Gets and sets the ground shadow setting on the view!/s window. |
| [HWND](../ClientView/ClientView_HWND.md) | Property that returns the hWnd (the handle assigned by Windows to the current window) of the view. |
| [Parent](../ClientView/ClientView_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Type](../ClientView/ClientView_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ClientViews.Add](../ClientViews/ClientViews_Add.md), [ClientViews.AddBySubset](../ClientViews/ClientViews_AddBySubset.md), [ClientViews.Item](../ClientViews/ClientViews_Item.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |