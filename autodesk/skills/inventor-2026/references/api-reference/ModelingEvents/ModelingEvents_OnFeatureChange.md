# ModelingEvents.OnFeatureChange Event

Parent Object: [ModelingEvents](../ModelingEvents/ModelingEvents.md)

## Description

Event that is fired whenever a feature changes.

## Remarks

This is provided for features in parts and also for assembly features. A change is defined as the modification of a feature's definition. This can occur when the end-user uses the edit command for that particular feature and when a feature is modified using the API. A feature recomputing as the result of other changes in the model is not considered a feature change. For example, if a fillet recomputes because the underlying geometry has changed, this is not considered a feature change because only the resulting geometry changed, not the definition of the fillet. Also, editing any of the various objects the feature is dependent on (sketch, parameters) is also not considered a feature change.

## Syntax

ModelingEvents.**OnFeatureChange**( ***DocumentObject*** As [Document](../Document/Document.md), ***Feature*** As [PartFeature](../PartFeature/PartFeature.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input Document object that indicates the document in which the change occurred. |
| Feature | [PartFeature](../PartFeature/PartFeature.md) | Input PartFeature object that indicates the feature that changed. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the feature is changed. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 2008
