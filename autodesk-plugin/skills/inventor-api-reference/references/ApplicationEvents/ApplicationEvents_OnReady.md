# ApplicationEvents.OnReady Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

The OnReady event notifies a client when Inventor has completely initialized and is ready for interactive use.

## Remarks

This event fires (only once) after Inventor has completed its initialization. This includes initialization of all the Add-ins loaded at startup. This event should be used in conjunction with the Application.Ready property. This event is intended to be used by Add-Ins. When an Add-In is activated by inventor, Inventor itself is still initializing at that point so there are a few limitations to what an Add-In can do. An example is an Add-In that needs to access another Add-In or see what other Add-Ins have been loaded. When the Add-In is activated, Inventor is in the process of activating each Add-In and it's likely not all of the Add-Ins have been activated yet. By listening to the OnReady event the Add-In can perform these types of tasks once Inventor is in completely loaded state.

## Syntax

ApplicationEvents.**OnReady**( ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) initialization is complete. This notification is only provided after Inventor has initialized so the value of this argument will always be kAfter. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |