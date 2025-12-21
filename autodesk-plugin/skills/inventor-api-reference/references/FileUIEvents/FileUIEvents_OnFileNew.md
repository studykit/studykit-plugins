# FileUIEvents.OnFileNew Event

Parent Object: [FileUIEvents](../FileUIEvents/FileUIEvents.md)

## Description

Fires before a File New from standard template is executed.

## Syntax

FileUIEvents.**OnFileNew**( ***DocumentType*** As [DocumentTypeEnum](../DocumentTypeEnum.md), ***TemplateFileName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentType | [DocumentTypeEnum](../DocumentTypeEnum.md) | DocumentTypeEnum indicating the document's type. Possible values include kUnknownDocumentObject,  kPartDocumentObject, kAssemblyDocumentObject, kDrawingDocumentObject, kPresentationDocumentObject, kDesignElementDocumentObject, kForeignModelDocumentObject, and kSATFileDocumentObject. |
| TemplateFileName | String | The full filename of the file to use as the template when creating the new file. This can be any existing file and is not restricted to the files within the default template path. This argument must be set if the HandlingCode is set to kEventHandled. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that, if populated, can be used to determine the context of why the event fired. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. Can supply any of the following three values\: \* kEventNotHandled\: Inventor continues with its standard behavior and displays the "Open" dialog to allow the end-user to select a template. \* kEventHandled\: Indicates that the client is handling getting the template. Requires that the client also set the TemplateFileName argument. \* kEventCanceled\: Cancels the operation. |

## Version

Introduced in version 2009
