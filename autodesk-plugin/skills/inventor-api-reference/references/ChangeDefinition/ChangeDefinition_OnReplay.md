# ChangeDefinition.OnReplay Event

Parent Object: [ChangeDefinition](../ChangeDefinition/ChangeDefinition.md)

## Description

Event that is fired by Inventor in a script replay scenario. In the handler of this event (typically, written by the client who created this ChangeDefinition), it is expected that a new ChangeProcessor will be generated using the CreateChangeProcessor method of this object, followed by the client proceeding to 'hook up' its ChangeProcessor handler code, and returning this hooked-up processor back. Inventor will then use this returned ChangeProcessor to replay the scripted command.

## Syntax

ChangeDefinition.**OnReplay**( ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***ResultProcessor*** As [ChangeProcessor](../ChangeProcessor/ChangeProcessor.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. |
| ResultProcessor | [ChangeProcessor](../ChangeProcessor/ChangeProcessor.md) | The client returns this ChangeProcessor which Autodesk Inventor will use to replay the scripted command. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |