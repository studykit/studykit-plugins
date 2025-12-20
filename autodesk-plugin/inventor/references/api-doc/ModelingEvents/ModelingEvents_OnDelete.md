# ModelingEvents.OnDelete Event

Parent Object: [ModelingEvents](../ModelingEvents/ModelingEvents.md)

## Description

The OnDelete event notifies the client when a modeling entity is deleted.

## Remarks

Currently the notification is limited to features and parameters. Notification for parameters is only sent when a parameter is explicitly deleted, not when it is deleted as a result of its owner being deleted. For example if you delete a fillet feature, the notification will be sent for the fillet feature, but not for the parameter that controls the fillet radius, even though the parameter is deleted as a result of the feature delete. The type of entities supported for this event may be expanded in the future so you should be careful to write code that is not dependent on the current behavior and filters correctly for the entity type you need.

## Syntax

ModelingEvents.**OnDelete**( ***DocumentObject*** As [Document](../Document/Document.md), ***Entity*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object that contains the entity being deleted. |
| Entity | Object | The Entity that is being deleted. When the value of the BeforeOrAfter argument is kBefore, the object provided is the object before being deleted. When the value is kAfter, an object is also provided but since the actual entity has been deleted calling any methods or properties on the object will fail. The only thing that is valid to do with the object at this time is to compare it's identity with a reference previously saved. For example: Private m\_oDeletedEntity As Object Private Sub oModelingEvents\_OnDelete(ByVal DocumentObject As Document, ByVal Entity As Object, ByVal BeforeOrAfter As EventTimingEnum, ...) If BeforeOrAfter = kBefore Then ' Somehow Check to see if the Entity being deleted is an interesting one. ' For example, it could have an attribute attached to it to identify it. If Interesting(Entity) Then ' Save a reference to the object. Set m\_oDeletedEntity = Entity End If Else ' Now we're either after the delete or it's been aborted. ' Check to see if the object is the interesting one. If Entity is m\_oDeletedEntity Then If BeforeOrAfter = kAfter then ' The object was deleted. ElseIf BeforeOrAfter = kAbort Then ' The delete was aborted. End If End If End Sub |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the entity is deleted. You should only perform query operations when the value of this argument is kBefore. Inventor is not in a state to correctly handle edit operations after that point. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |