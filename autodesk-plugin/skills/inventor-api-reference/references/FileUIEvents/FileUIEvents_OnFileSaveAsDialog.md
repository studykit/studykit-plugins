# FileUIEvents.OnFileSaveAsDialog Event

Parent Object: [FileUIEvents](../FileUIEvents/FileUIEvents.md)

## Description

The OnFileSaveAsDialog event notifies the client when the end-user executes the Save As or Save Copy As command to create a new file.

## Remarks

This notification is also sent when the Save command is executed the first time for a file that has not been previously saved. By responding to this event the client can override Inventor's standard behavior of displaying the Save As dialog and provide their own interface to determine the new filename.

## Syntax

FileUIEvents.**OnFileSaveAsDialog**( ***FileTypes***() As String, ***SaveCopyAs*** As Boolean, ***ParentHWND*** As Long, ***FileName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileTypes | String | A list of the file types displayed in the 'Files of Type' combo box on the Save As dialog. When saving a copy of part an example of the list is: "Part Files (\*.ipt)|\*.ipt" "DWF Files (\*.dwf)|\*.dwf" "BMP (\*.bmp)|\*.bmp" "IGES Files (\*.igs;\*.ige;\*.iges)|\*.igs;\*.ige;\*.iges" "SAT Files (\*.sat)|\*.sat" |
| SaveCopyAs | Boolean | Indicates if the end-user is performing a Save As or Save Copy As operation. Returns True if it is a Save Copy As and False for Save As. |
| ParentHWND | Long | The Windows handle of the Inventor Application window. If the client displays their own dialog they can use this to associate their dialog to the Inventor window. This results in better behavior between the client dialog and Inventor. For example, the client window will stay on top of Inventor and if the Inventor window is collapsed the client dialog will also be collapsed. |
| FileName | String | The full filename to use when saving the file. The handling code must be set to kEventHandled in order to override the standard Save dialog and save the file using this filename. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. The following information is provided through the Context argument: Name = "TopLevelDocument". Value = The Document object being saved. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. Can supply any of the following three values: \* kEventNotHandled: Inventor continues with its standard behavior and displays the "Save As" dialog to allow the end-user to specify the filename. \* kEventHandled: Indicates that the client is handling getting the filename. Requires that the client also set the FileName argument. \* kEventCanceled: Cancels the operation. |

## Version

Introduced in version 4
