# FileUIEvents.OnFileInsertDialog Event

Parent Object: [FileUIEvents](../FileUIEvents/FileUIEvents.md)

## Description

The OnFileInsertDialog event notifies a client whenever the end-user has executed a command that provides for the selection and insertion of a document into another document.

## Remarks

Three common commands are the Place Component command in assembly, the Derived Component command in part, and the Base View command in drawing. When these commands are run, the end-user needs to select a file. By default Inventor displays the standard Open dialog to allow them to specify the file. Using this event a client can override the standard behavior of Inventor and provide the filename using whatever procedure they choose; typically replacing the Open dialog with their own dialog. This notification is sent to the client at the point the Open dialog would usually be displayed. If the client wants to handle getting the filename then they get a filename any way they choose and then respond to this event by setting the FileName argument with the filename they have and set the HandlingCode argument to kEventHandled. If the client responds to this event with a filename and the kEventHandled, then Inventor uses the supplied filename and does not display its standard Open dialog. If the client responds with kEventNotHandled, Inventor uses its standard behavior and will display the Open dialog. If the client responds with kEventCanceled, the command is cancelled. Valid NameValueMap values for the Context argument:

| Name | Value | Valid when inserting |
| --- | --- | --- |
| Embed | Boolean | .xls, .xlsx, all image files |
| DesignViewRepresentation | String | .iam |
| DesignViewAssociative | Boolean | .iam |
| PrivateRepresentationFileName | String | .iam |
| PositionalRepresentation | String | .iam |
| ModelState | String | .iam;.ipt |
| InteractiveiMates | Boolean | .ipt,.iam |
| AutomaticiMates | Boolean | .ipt,.iam |

## Syntax

FileUIEvents.**OnFileInsertDialog**( ***FileTypes***() As String, ***DocumentObject*** As [Document](../Document/Document.md), ***ParentHWND*** As Long, ***FileName*** As String, ***RelativeFileName*** As String, ***LibraryName*** As String, ***CustomLogicalName***() As Byte, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileTypes | String | A list of the file types displayed in the 'Files of Type' combo box on the Open dialog. For example, when the Derived Component command is executed the array contains the following three strings: "Component Files (\*.ipt, \*.iam)|\*.ipt; \*.iam" "Part Files (\*.ipt)|\*.ipt" "Assembly Files (\*.iam)|\*.iam" |
| DocumentObject | [Document](../Document/Document.md) | The object the file will be inserted into. For example, if the Place Component command is invoked, this will be the assembly the component will be inserted into. |
| ParentHWND | Long | The Windows handle of the Inventor Application window. If the client displays their own dialog they can use this to associate their dialog to the Inventor window. This results in better behavior between the client dialog and Inventor. For example, the client window will stay on top of Inventor and if the Inventor window is collapsed the client dialog will also be collapsed. |
| FileName | String | The full filename that the client returns to Inventor if they choose to override Inventor's standard behavior and obtain the filename themselves. In order for this filename to be used the client must also return kEventHandled as the handling code.  Multiple files are also supported where the file names are delimited with the "|" character. For example:  `FileName = "C:\Temp\Part1.ipt|C:\Temp\Part2.ipt"` |
| RelativeFileName | String | Not used. |
| LibraryName | String | Not used. |
| CustomLogicalName | Byte | An array of Bytes that can be used by data management systems as a way to associate additional information with a file reference. During file resolution, the data management system can use this information to help look up the file within the data management system. Supplying an array of bytes for this event will associate this custom logical name with the reference created to the document being inserted. If a reference already exists for this document, the existing custom logical name will be replaced by this one. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the notification. See the Remarks section for valid NameValueMap values. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. The following three values are supportd:  * kEventNotHandled: Inventor continues with its standard behavior and displays the Open dialog to allow the end-user to select a file. * kEventHandled: Indicates that the client is handling getting the filename. Requires that the client also sets the FileName argument with the full filename of the file Inventor should use. * kEventCanceled: Cancels the operation. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |