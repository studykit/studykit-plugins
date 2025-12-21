# ClientOperationEvents.FireOnClientOperation Method

Parent Object: [ClientOperationEvents](../ClientOperationEvents/ClientOperationEvents.md)

## Description

Method that fires the OnClientOperation even.

## Syntax

ClientOperationEvents.**FireOnClientOperation**( ***ClientId*** As String, ***OperationName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input String value that indicates the client ID(GUID) of an application addin. |
| OperationName | String | Input String value that specifies the client operation name. This can be something like “Login”, “Logout” etc.. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum that indicates if this event is fired just before or after a client operation. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. This argument provides additional information as described below: |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Out HandlingCodeEnum that indicates how you are handling the event. The following three values are supported:  kEventNotHandled: The client operation will continue.  kEventHandled: This is ignored currently which has the same effect as kEventNotHandled.  kEventCanceled: Cancels the operation.. |

## Version

Introduced in version 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |