# ApplicationEvents.OnOpenDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

The OnOpenDocument event notifies a client when a document is opened.

## Remarks

Documents are opened directly by the end-user using the Open command, but they are also opened indirectly as a result of being referenced by another document. For example, if an assembly is opened all of the documents referenced by the assembly are also opened. This notification is sent in all cases. The Context argument provides information that can help determine the context of the open. **You should not assume that the events will always arrive in the same sequence.** As an example, let us say you are writing an Addin that listens to both the OnOpenDocument event and the OnDocumentChange event. You are interested in a document called MyFavoriteDocument. Your Addin assumes that the OnOpenDocument event will arrive before the OnDocumentChange event. In its OnOpenDocument event handler it checks for MyFavoriteDocument and sets a global variable MyFavoriteDocumentIsOpen as true. In the OnDocumentChange event handler, it first checks whether MyFavoriteDocumentIsOpen is true, and only then takes any action. In your testing that code may work, *but fail on a customer's machine*. This can happen when another Addin receives the OnOpenDocument event before your Addin, and in its event handler makes a change to the document - causing an OnDocumentChange event to be fired. So you will get OnDocumentChange event before you get an OnOpenDocument event. So in this instance, the assumption that OnOpenDocument event will always arrive before OnDocumentChange event on the same document, results in a very hard to find problem. As a general rule, it's safer not to make any assumption about the order in which these events will be received.

## Syntax

ApplicationEvents.**OnOpenDocument**( ***DocumentObject*** As [Document](../Document/Document.md), ***FullDocumentName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object being opened. When the BeforeOrAfter argument is kBefore, this argument will be nothing because the document does not yet exist. |
| FullDocumentName | String | Output string that specifies the fully qualified name of the document being opened. This is supplied both before and after. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Output EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the document is opened. Notification is sent before and after the document is opened. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Output NameValueMap object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of how the document is being opened. Name = "TopLevelFilename", Value = The full filename of the top-level file that was opened that's causing this file to be opened. For example, if an assembly is opened and a document referenced by that assembly is opened as a result, the TopLevelFilename will be the full filename of the assembly. This value can be the same as the FullDocumentName argument which indicates this document was opened by itself. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. The value of this argument is currently ignored for this event. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |