# ChangeProcessor.OnWriteToScript Event

Parent Object: [ChangeProcessor](../ChangeProcessor/ChangeProcessor.md)

## Description

Event that is fired before the execution of and commit of the change. The return string should be set with a formatted string of the arguments. The string may be persisted for eventual replay, such as a transcript replay. A semicolon (';') character should be considered a reserved character used as a separator between individual arguments. The recommended format would be a variable name value pair separated by an equal character, with arguments separated by semicolons. For example "Argument1Name=Value1;Argument2Name=Value2"

## Syntax

ChangeProcessor.**OnWriteToScript**( ***Document*** As [Document](../Document/Document.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***ResultInputs*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Document | [Document](../Document/Document.md) | Input Document object that specifies the document in which to execute the ChangeProcessor. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. |
| ResultInputs | String | Return string - most likely a formatted string of the arguments for eventual replay. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |