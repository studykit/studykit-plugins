# ApplicationEvents.OnCloseView Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

The OnCloseView event notifies a client when a view is closed. An API view is equivalent to an Inventor graphics window.

## Syntax

ApplicationEvents.**OnCloseView**( ***ViewObject*** As [View](../View/View.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewObject | [View](../View/View.md) | The view that is about to be closed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter) the view is closed. This notification is currently only provided before the view has been closed. To protect yourself against possible future changes to this event you should write your code so that you only respond to kBefore, as shown below. Private Sub ApplicationEvents\_OnCloseView(...) If BeforeOrAfter = kBefore Then ' Your code in reaction to the notification. End If End Sub |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 4
