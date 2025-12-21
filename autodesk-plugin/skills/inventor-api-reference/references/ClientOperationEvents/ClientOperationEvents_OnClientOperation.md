# ClientOperationEvents.OnClientOperation Event

Parent Object: [ClientOperationEvents](../ClientOperationEvents/ClientOperationEvents.md)

## Description

Event that is fired when FireOnClientOperation method is called.

## Syntax

ClientOperationEvents.**OnClientOperation**( ***ClientId*** As String, ***OperationName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input String value that indicates the application addin’s client ID. |
| OperationName | String | Input String value that specifies the client operation name. This can be something like “Login”, “Logout” etc.. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum that indicates if this event is fired just before or after a client operation. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. . This argument provides additional information as described below: |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event.. The following three values are supported:  kEventNotHandled: The client operation will continue.  kEventHandled: This is ignored currently.  kEventCanceled: Cancels the operation. |

## Version

Introduced in version 2025
