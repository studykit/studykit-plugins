# SketchEvents.OnNewSketch3D Event

Parent Object: [SketchEvents](../SketchEvents/SketchEvents.md)

## Description

The OnNewSketch3D event notifies the client when a new 3D sketch is being created.

## Syntax

SketchEvents.**OnNewSketch3D**( ***DocumentObject*** As [Document](../Document/Document.md), ***Sketch3D*** As [Sketch3D](../Sketch3D/Sketch3D.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the new 3D sketch is being created within. |
| Sketch3D | [Sketch3D](../Sketch3D/Sketch3D.md) | The new 3D sketch just created. When the BeforeOrAfter argument is kBefore, the value of this argument is Nothing since the sketch has not yet been created. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the sketch is created. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11
