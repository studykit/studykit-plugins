# CameraEvents.OnCameraChange Event

Parent Object: [CameraEvents](../CameraEvents/CameraEvents.md)

## Description

Event that fires when the camera of a view has been modified but before the view has been updated. You can modify client graphics in response to this event and the modified client graphics will be drawn when the view is updated.

## Syntax

CameraEvents.**OnCameraChange**( ***View*** As [View](../View/View.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| View | [View](../View/View.md) | The View object that is updating because of its associated camera has changed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | This notification is only provided after the camera has changed so the value of this argument will always be kAfter. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is currently provided for this event. |

## Version

Introduced in version 2011
