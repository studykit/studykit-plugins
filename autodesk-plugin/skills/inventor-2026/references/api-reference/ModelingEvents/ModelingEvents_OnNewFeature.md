# ModelingEvents.OnNewFeature Event

Parent Object: [ModelingEvents](../ModelingEvents/ModelingEvents.md)

## Description

Event that is fired whenever a feature is created.

## Syntax

ModelingEvents.**OnNewFeature**( ***DocumentObject*** As [Document](../Document/Document.md), ***Feature*** As [PartFeature](../PartFeature/PartFeature.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input Document object that indicates the document in which the change occurred. |
| Feature | [PartFeature](../PartFeature/PartFeature.md) | Input PartFeature object that was just created. Nothing in the kBefore case. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Notification is sent before and after the feature has been created. You should only perform query operations when the valueof this argument is kBefore. Inventor is not in a state to correctly handle edit operations at that point. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2008
