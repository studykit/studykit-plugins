# SketchEvents.OnNewSketch Event

Parent Object: [SketchEvents](../SketchEvents/SketchEvents.md)

## Description

Event that is fired whenever a sketch is created.

## Syntax

SketchEvents.**OnNewSketch**( ***DocumentObject*** As [Document](../Document/Document.md), ***Sketch*** As [Sketch](../Sketch/Sketch.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input Document object that indicates the document in which the change occurred. |
| Sketch | [Sketch](../Sketch/Sketch.md) | Input PlanarSketch or a DrawingSketch object that was just created. Nothing in the kBefore case. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the sketch is created. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |