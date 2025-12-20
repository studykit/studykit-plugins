# AssemblyEvents.OnDelete Event

Parent Object: [AssemblyEvents](../AssemblyEvents/AssemblyEvents.md)

## Description

Event that is fired whenever an object within this events set is deleted in a document.

## Remarks

Assembly objects currently reported are ComponentOccurrence and AssemblyConstraint objects. The Document.OnDelete event can be used if delete notification is needed for other types of objects.

## Syntax

AssemblyEvents.**OnDelete**( ***DocumentObject*** As [Document](../Document/Document.md), ***Entity*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input Document object that indicates the document in which the change occurred. |
| Entity | Object | Input object that was just deleted. When the value of the BeforeOrAfter argument is kBefore, the object provided is the object being deleted. When the value is kAfter, an object is also provided but since the actual entity has been deleted calling any methods or properties on the object will fail. The only thing that is valid to do with the object at this time is to compare it's identity with a reference previously saved (usually during kBefore). For example: Private m\_oDeletedEntity As Object Private Sub oAssemblyEvents\_OnDelete(ByVal DocumentObject As Document, ByVal Entity As Object, ByVal BeforeOrAfter As EventTimingEnum, ...) If BeforeOrAfter = kBefore Then ' Check to see if the Entity being deleted is an interesting one. For example, it could have an attribute attached to it. If Interesting(Entity) Then ' Save a reference to the object. Set m\_oDeletedEntity = Entity End If Else ' Now we're either after the delete or it's been aborted. Check to see if the object is the interesting one. If Entity Is m\_oDeletedEntity Then If BeforeOrAfter = kAfter then ' The object was deleted. Else If BeforeOrAfter = kAbort Then ' The delete was aborted. End If End If End Sub |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the entity is deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |