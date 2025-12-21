# PartEvents.OnSurfaceBodyChanged Event

Parent Object: [PartEvents](../PartEvents/PartEvents.md)

## Description

The OnSurfaceBodyChanged event notifies the client when the surface and solid geometry of a part geometrically changes.

## Remarks

If there are multiple surface bodies within a part, (solid and/or work surfaces), this notification is sent if any of them change.

## Syntax

PartEvents.**OnSurfaceBodyChanged**( ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the notification. Name = "Undo". Value = A Boolean indicating if the change occurred as the result of an undo operation. This context value is only provided in the case where the change does occur because of an undo operation, so the value will always be True. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating when the event is being fired. Notification is only sent after the surface body has changed, so this value is always kAfter. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) |  |

## Version

Introduced in version 4
