# ChangeProcessor.OnReadFromScript Event

Parent Object: [ChangeProcessor](../ChangeProcessor/ChangeProcessor.md)

## Description

Event that is fired in a replay scenario supplying the cached Inputs string. The client application interprets the inputs and converts them into meaningful data for use in the execution of logic in the OnExecute event. This event is always followed by the OnExecute event.

## Syntax

ChangeProcessor.**OnReadFromScript**( ***Document*** As [Document](../Document/Document.md), ***Inputs*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Document | [Document](../Document/Document.md) | Input Document object that specifies the document in which to make the changes. |
| Inputs | String | Input string, cached for playback. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |