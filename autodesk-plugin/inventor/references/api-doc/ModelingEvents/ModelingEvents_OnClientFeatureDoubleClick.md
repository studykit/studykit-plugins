# ModelingEvents.OnClientFeatureDoubleClick Event

Parent Object: [ModelingEvents](../ModelingEvents/ModelingEvents.md)

## Description

Event that fires when the user double-clicks a client feature.

## Remarks

Applications should typically invoke the edit of the client feature when this event is fired.

## Syntax

ModelingEvents.**OnClientFeatureDoubleClick**( ***DocumentObject*** As [Document](../Document/Document.md), ***Feature*** As [ClientFeature](../ClientFeature/ClientFeature.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input Document object that indicates the document in which the change occurred. |
| Feature | [ClientFeature](../ClientFeature/ClientFeature.md) | Input ClientFeature object that indicates the client feature that was double-clicked. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. This argument is currently ignored for the event. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |