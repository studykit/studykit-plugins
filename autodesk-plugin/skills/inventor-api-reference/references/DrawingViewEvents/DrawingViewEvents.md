# DrawingViewEvents Object

## Description

Call-back or 'outgoing' sink interface through which Inventor fires the DrawingView Events. See the article in the overviews section.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingViewEvents/DrawingViewEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../DrawingViewEvents/DrawingViewEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../DrawingViewEvents/DrawingViewEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnViewUpdate](../DrawingViewEvents/DrawingViewEvents_OnViewUpdate.md) | The OnViewUpdate event notifies a client when the document associated with the drawing view has been modified and causes the drawing view to update. |

## Accessed From

[DetailDrawingView.DrawingViewEvents](../DetailDrawingView/DetailDrawingView_DrawingViewEvents.md), [DrawingView.DrawingViewEvents](../DrawingView/DrawingView_DrawingViewEvents.md), [SectionDrawingView.DrawingViewEvents](../SectionDrawingView/SectionDrawingView_DrawingViewEvents.md)

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |