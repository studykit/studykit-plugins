# DrawingEvents Object

## Description

The DrawingEvents object provides drawing event notification, such as onRetrieveDimensions.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingEvents/DrawingEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../DrawingEvents/DrawingEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../DrawingEvents/DrawingEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnRetrieveDimensions](../DrawingEvents/DrawingEvents_OnRetrieveDimensions.md) | The OnRetrieveDimensions event notifies a client whenever dimensions are retrieved into a drawing using the Retrieve Dimensions command. |

## Accessed From

[DrawingDocument.DrawingEvents](../DrawingDocument/DrawingDocument_DrawingEvents.md)

## Version

Introduced in version 9
