# DocumentEvents.OnChangeSelectSet Event

Parent Object: [DocumentEvents](../DocumentEvents/DocumentEvents.md)

## Description

The OnChangeSelectSet event notifies a client when the contents of the select set have changed.

## Remarks

This notification is sent when items are added or removed from the select set and when the select set is cleared. The current contents of the select set can be obtained through the document's SelectSet object. Note. You can get what appears to be double notifications of this event when an object is already selected and the end-user selects another object. In this case the first notification is because the current object(s) in the select set are being removed and the second notification is for the new entity being added.

## Syntax

DocumentEvents.**OnChangeSelectSet**( ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input that indicates when the event is fired. This notification is only provided after the contents of the select set have changed so the value of this argument will always be kAfter. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input that specifies additional context information regarding the event. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that specifies how Autodesk Inventor is to handle the event. This argument is ignored for this event. |

## Version

Introduced in version 5
