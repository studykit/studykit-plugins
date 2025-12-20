# ChangeProcessor.OnExecute Event

Parent Object: [ChangeProcessor](../ChangeProcessor/ChangeProcessor.md)

## Description

Event that is fired when Inventor is in a state to accept changes to data. This is the event where the client application executes its logic on the specified document.

## Syntax

ChangeProcessor.**OnExecute**( ***Document*** As [Document](../Document/Document.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***Succeeded*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Document | [Document](../Document/Document.md) | Input Document object that specifies the document in which the client is to make its changes. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. |
| Succeeded | Boolean | The Succeeded argument is an in/out argument, and will always have an initial value of True. Leave it set to true and the change will be committed. If your change fails and you want the change's transaction to be aborted, set this value to False. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |