# SketchEvents.OnDelete Event

Parent Object: [SketchEvents](../SketchEvents/SketchEvents.md)

## Description

The OnDelete event notifies the client when a 2d or 3d sketch is being deleted. This notification is not sent when the contents of the sketch is deleted, but only when the sketch itself is deleted.

## Syntax

SketchEvents.**OnDelete**( ***DocumentObject*** As [Document](../Document/Document.md), ***Entity*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object that contains the sketch. |
| Entity | Object | The sketch that is being deleted. When the value of the BeforeOrAfter argument is kBefore, the entity provided is the sketch before being deleted. When the value is kAfter, an object is also provided but since the actual entity has been deleted calling any methods or properties on the object will fail. The only thing that is valid to do with the object at this time is to compare it's identity with a reference previously saved. For example: Private m\_oDeletedSketch As Object Private Sub oSketchEvents\_OnDelete( ByVal DocumentObject As Document, ByVal Entity As Object, ByVal BeforeOrAfter As EventTimingEnum, ...) If BeforeOrAfter = kBefore Then ' Somehow Check to see if the sketch being deleted is an interesting one. ' For example, it could have an attribute attached to it to identify it. If Interesting(Entity) Then ' Save a reference to the object. Set m\_ oDeletedSketch = Entity End If Else ' Now we're either after the delete or it's been aborted. ' Check to see if the sketch is the interesting one. If Entity is m\_ oDeletedSketch Then If BeforeOrAfter = kAfter then ' The sketch was deleted. ElseIf BeforeOrAfter = kAbort Then ' The delete was aborted. End If End If End Sub |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the sketch is deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |