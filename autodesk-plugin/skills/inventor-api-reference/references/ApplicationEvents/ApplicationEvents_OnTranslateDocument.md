# ApplicationEvents.OnTranslateDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

The OnTranslateDocument event notifies a client whenever a file is translated into Inventor or an Inventor document is translated out to a non-Inventor file.

## Syntax

ApplicationEvents.**OnTranslateDocument**( ***TranslatingIn*** As Boolean, ***DocumentObject*** As [Document](../Document/Document.md), ***FullFileName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TranslatingIn | Boolean | Input Boolean that specifies whether the document is being translated into Autodesk Inventor. |
| DocumentObject | [Document](../Document/Document.md) | The object that is created as a result of the translation. When the BeforOrAfter argument is kBefore the value of this argument will be Nothing because the document has not been created yet. |
| FullFileName | String | The full filename of the document being translated. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input that specifies whether to fire event before or after processing. Notification is sent before and after the document is translated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the notification. Name = " TranslationContext ". Value = The TranslationContext object to get and set the translation context. Name = " Options ", Value = The NameValueMap object to get and set the options for translation. Name = " SourceData", this is only returned when translate a file into Inventor. Value = The DataMedium for the translation. Name = " TargetData ", this is only returned when translate a document to a non-Inventor file. Value = The DataMedium for the translation. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |