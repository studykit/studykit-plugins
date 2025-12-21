# FileUIEvents.OnFileInsertNewDialog Event

Parent Object: [FileUIEvents](../FileUIEvents/FileUIEvents.md)

## Description

The OnFileInsertNewDialog event notifies the client whenever the end-user executes the Create Component command within an assembly.

## Remarks

By responding to this event the client can replace the 'Create In-Place Component' dialog with their own. This notification is sent to the client immediately after the command is executed but before the standard dialog is displayed to the end-user. By supplying at least the Filename argument and setting the HandlingCode to kEventHandled, Inventor will bypass displaying the standard dialog and use the information provided to create a new in-place component within the assembly. The rest of the command behavior remains the same. That is, if this isn't the first component being placed in the assembly, the end-user must select a location in the assembly to position the new component. Valid NameValueMap values for the Context parameter:

| Name | Value | Comments |
| --- | --- | --- |
| BOMStructure | BOMStructureEnum |  |
| VirtualComponent | Boolean | The *FileName* argument is the virtual component name. |
| ConstrainSketchPlane | Boolean | Does not apply for the first component in assembly. |

## Syntax

FileUIEvents.**OnFileInsertNewDialog**( ***TemplateDir*** As String, ***FileTypes***() As String, ***DocumentObject*** As [Document](../Document/Document.md), ***ParentHWND*** As Long, ***TemplateFileName*** As String, ***FileName*** As String, ***RelativeFileName*** As String, ***LibraryName*** As String, ***CustomLogicalName***() As Byte, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TemplateDir | String | The default template directory as defined in the File tab of the Application Options dialog. This information can be used by the client in their dialog to allow the end-user to select one of the standard templates. |
| FileTypes | String | A list of the file types displayed in the "Files of Type" combo box on the Open dialog. For example, when the Derived Component command is executed the array contains the following strings: "Part Files (\*.ipt)|\*.ipt" "Assembly Files (\*.iam)|\*.iam" |
| DocumentObject | [Document](../Document/Document.md) | The AssemblyDocument object the new component will be created within. |
| ParentHWND | Long | The Windows handle of the Inventor Application window. If the client displays their own dialog they can use this to associate their dialog to the Inventor window. This results in better behavior between the client dialog and Inventor. For example, the client window will stay on top of Inventor and if the Inventor window is collapsed the client dialog will also be collapsed. |
| TemplateFileName | String | The full filename of the file to use as the template when creating the new component. This can be any existing file and is not restricted to the files within the default template path. If this argument is not set, then the default part or assembly template will be used for the component. The type of document is determined based on the extension of the filename supplied in the Filename argument. This argument is ignored unless the HandlingCode argument is set to kEventHandled. |
| FileName | String | The full filename of the file to be created. When creating a component in-place, the component is created in memory and is not written to disk until the end-user performs a save of the file. Because the filename is specified during the creation of the component the end-user will not be prompted for a filename during the save operation. This argument is required if the HandlingCode is set to kEventHandled. |
| RelativeFileName | String | Not used. |
| LibraryName | String | Not used. |
| CustomLogicalName | Byte | An array of Bytes that could have been defined by an application as an additional identifier for this document. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. No context information is provided for this event. See Remarks for valid NameValueMap values. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. This can supply any of the following three values\: \* kEventNotHandled\: Inventor continues with its standard behavior and displays the "Create In-Place Component" dialog to allow the end-user to specify the component information. \* kEventHandled\: Indicates that the client is handling getting the component information. Requires that the client also set, at least, the FileName argument with the full filename of the component to be created. \* kEventCanceled\: Cancels the operation. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |