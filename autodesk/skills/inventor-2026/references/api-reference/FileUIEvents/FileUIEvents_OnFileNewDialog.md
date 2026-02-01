# FileUIEvents.OnFileNewDialog Event

Parent Object: [FileUIEvents](../FileUIEvents/FileUIEvents.md)

## Description

The OnFileNewDialog event notifies the client when the end-user executes the New or Create Drawing View command to create a new file.

## Remarks

By responding to this event the client can override Inventor's standard behavior of displaying the Create New File dialog and provide their own interface to determine the template to use in creating the new file. This notification is only made in cases where the Create New File dialog is displayed to allow the end-user to select a template. If the end-user uses the pop-up command list next to the New command to select an assembly, part, presentation, or drawing document, the Create New File dialog is bypassed and this notification is not sent in this case.

## Syntax

FileUIEvents.**OnFileNewDialog**( ***TemplateDir*** As String, ***ParentHWND*** As Long, ***TemplateFileName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TemplateDir | String | The default template directory as defined in the File tab of the Application Options dialog. This information can be used by the client in their dialog to allow the end-user to select one of the standard templates. |
| ParentHWND | Long | The Windows handle of the Inventor Application window. If the client displays their own dialog they can use this to associate their dialog to the Inventor window. This results in better behavior between the client dialog and Inventor. For example, the client window will stay on top of Inventor and if the Inventor window is collapsed the client dialog will also be collapsed. |
| TemplateFileName | String | The full filename of the file to use as the template when creating the new file. This can be any existing file and is not restricted to the files within the default template path. This argument must be set if the HandlingCode is set to kEventHandled. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. Can supply any of the following three values:  * kEventNotHandled: Inventor continues with its standard behavior and displays the "Open" dialog to allow the end-user to select a template. * kEventHandled: Indicates that the client is handling getting the template. Requires that the client also set the TemplateFileName argument. * kEventCanceled: Cancels the operation. |

## Version

Introduced in version 4
