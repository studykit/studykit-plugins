# DocumentEvents.OnSave Event

Parent Object: [DocumentEvents](../DocumentEvents/DocumentEvents.md)

## Description

The OnSave event notifies a client whenever the document is saved.

## Remarks

The notification is made when the standard Save and the Save Copy As commands are invoked.

## Syntax

DocumentEvents.**OnSave**( ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating when the event is being fired. Specifies if the notification is being sent before the document is saved (kBefore) or after the save (kAfter). |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the save. Name = "SaveFileName", Value = The full filename that document is being saved to. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This event supports the ability to cancel the change. Setting this argument to kEventCanceled when the BeforeOrAfter argument is kBefore Inventor will abort the save. If the event is aborted, it is not fired again with either kAfter or kAbort. |

## Version

Introduced in version 4
