# CameraEvents Object

## Description

The CameraEvents object supports a set of properties and events used to work with a camera object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CameraEvents/CameraEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../CameraEvents/CameraEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../CameraEvents/CameraEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnCameraChange](../CameraEvents/CameraEvents_OnCameraChange.md) | Event that fires when the camera of a view has been modified but before the view has been updated. You can modify client graphics in response to this event and the modified client graphics will be drawn when the view is updated. |

## Accessed From

[Application.CameraEvents](../Application/Application_CameraEvents.md)

## Version

Introduced in version 2011
