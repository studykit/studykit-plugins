# DocumentEvents.OnDelete Event

Parent Object: [DocumentEvents](../DocumentEvents/DocumentEvents.md)

## Description

The OnDelete event notifies a client when an entity is deleted.

## Remarks

This notification is sent for each entity that is deleted. If the end-user selects multiple objects and then presses the delete key, an OnDelete notification is sent for each entity that's deleted.

## Syntax

DocumentEvents.**OnDelete**( ***Entity*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | The Entity that is being deleted. When the value of the BeforeOrAfter argument is kBefore, the object provided is the object before it is deleted. When the value is kAfter, an object is also provided but since the actual entity has been deleted calling any methods or properties on the object will fail. The only thing that is valid to do with the object at this time is to compare it's identity with a reference previously saved. For example: Private m\_oDeletedEntity As Object Private Sub oDocEvents\_OnDelete(ByVal Entity As Object, ByVal BeforeOrAfter As EventTimingEnum, ...) If BeforeOrAfter = kBefore Then ' Check to see if the Entity being deleted is an interesting one. ' For example, it could have an attribute attached to it. If Interesting(Entity) Then ' Save a reference to the object. Set m\_oDeletedEntity = Entity End If Else ' Now we're either after the delete or it's been aborted. ' Check to see if the object is the interesting one. If Entity is m\_oDeletedEntity Then If BeforeOrAfter = kAfter then ' The object was deleted. Else If BeforeOrAfter = kAbort Then ' The delete was aborted. End If End If End Sub |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the entity is deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |