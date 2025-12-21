# SketchEvents.OnSketchChange Event

Parent Object: [SketchEvents](../SketchEvents/SketchEvents.md)

## Description

The OnSketchChange event notifies the client when the geometry of a 2D sketch is changed.

## Remarks

Sketch changes that fire this event include adding new geometry, modifying existing geometry either directly or indirectly by editing dimension constraints, deleting geometry, and placing or deleting constraints where it will cause a change in any geometry. For example, placing a perpendicular constraint between two lines will cause this notification to be sent if the orientation of the lines needs to be changed to make them perpendicular. If the lines are already positioned perpendicular to one another, adding the constraint will not cause this notification to fire since the geometry does not change. Deleting the constraint does not cause the notification to be sent since the geometry is not changed as a result. Adding dimension constraints does not change the geometry so it does not result in this notification being sent, but editing the value of the dimension does modify the geometry and will result in this notification being sent.

## Syntax

SketchEvents.**OnSketchChange**( ***DocumentObject*** As [Document](../Document/Document.md), ***Sketch*** As [Sketch](../Sketch/Sketch.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the 3D sketch is within. |
| Sketch | [Sketch](../Sketch/Sketch.md) | PlanarSketch or a DrawingSketch object that is changing. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the sketch is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11
