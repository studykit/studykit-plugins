# ApplicationEvents.OnActivateView Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Event that fires just after a view is activated.

## Remarks

The OnActivateView event notifies a client when a view is activated. An API View object is equivalent to an Inventor window. When the end-user clicks on a window to work in it, it becomes the active window. The OnActivateView event is fired at this time.

## Syntax

ApplicationEvents.**OnActivateView**( ***ViewObject*** As [View](../View/View.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewObject | [View](../View/View.md) | The view that has been activated. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter) the view is activated. This notification is currently only provided after the view has been activated. To protect yourself against possible future changes to this event you should write your code so that you only respond to kAfter, as shown below. Private Sub ApplicationEvents\_OnActivateView(...) If BeforeOrAfter = kAfter Then ' Your code in reaction to the notification. End If End Sub |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 4
