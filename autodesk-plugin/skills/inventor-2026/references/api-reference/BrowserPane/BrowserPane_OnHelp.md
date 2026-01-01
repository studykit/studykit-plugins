# BrowserPane.OnHelp Event

Parent Object: [BrowserPane](../BrowserPane/BrowserPane.md)

## Description

The OnHelp event notifies a client when the end-user clicks the help button on the browser pane.

## Remarks

By setting the HandlingCode argument, the client can choose to handle displaying help themselves or let Inventor handle displaying some help information.

## Syntax

BrowserPane.**OnHelp**( ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter). This notification is only provided before any help is displayed so the value of this argument will always be kBefore. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. Setting the value of the HandlingCode argument specifies how Inventor is to handle displaying help. If you set this argument to kEventNotHandled or kEventCanceled, Inventor will display some general browser help. Setting the value of this argument to kEventHandled will allow you to handle displaying help to the end-user and Inventor will not display anything. To display help to the end-user you can choose to use whatever help system you want. Inventor's API does not provide support for the actual display of the clients help. |

## Version

Introduced in version 6
