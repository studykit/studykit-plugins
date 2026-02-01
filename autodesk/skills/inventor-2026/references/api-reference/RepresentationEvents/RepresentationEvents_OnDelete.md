# RepresentationEvents.OnDelete Event

Parent Object: [RepresentationEvents](../RepresentationEvents/RepresentationEvents.md)

## Description

The OnDelete event notifies the client when any representation related objects are deleted. These include positional representations and design views.

## Syntax

RepresentationEvents.**OnDelete**( ***DocumentObject*** As [Document](../Document/Document.md), ***Entity*** As Object, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object the deleted object is within. |
| Entity | Object | The representation that is being deleted. When the value of the BeforeOrAfter argument is kBefore, the object provided is the object before being deleted. When the value is kAfter, an object is also provided but since the actual entity has been deleted calling any methods or properties on the object will fail. The only thing that is valid to do with the object at this time is to compare it's identity with a reference previously saved. For example: Private m\_oDeletedEntity As Object Private Sub oRepresentationEvents\_OnDelete(ByVal DocumentObject As Document, ByVal Entity As Object, ByVal BeforeOrAfter As EventTimingEnum, ...) If BeforeOrAfter = kBefore Then ' Somehow Check to see if the representation being deleted is an interesting one. If Interesting(Entity) Then ' Save a reference to the object. Set m\_oDeletedEntity = Entity End If Else ' Now we're either after the delete or it's been aborted. ' Check to see if the object is the interesting one. If Entity is m\_oDeletedEntity Then If BeforeOrAfter = kAfter then ' The object was deleted. ElseIf BeforeOrAfter = kAbort Then ' The delete was aborted. End If End If End Sub |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. Notification is sent before and after the object is deleted. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 11
