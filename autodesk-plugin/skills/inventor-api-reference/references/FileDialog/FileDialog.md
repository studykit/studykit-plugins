# FileDialog Object

## Description

The FileDialog object represents the Inventor dialogs that are displayed when the user invokes the Place Component or Save As command. In the API, the FileDialog object provides the ability to use these same dialogs when a filename is needed from the user. It is very similar in concept to the Microsoft common file control.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [SetHelpContext](../FileDialog/FileDialog_SetHelpContext.md) | Method that sets the HTML Help Context to display when the help button is pressed in the FileDialog. |
| [SetHelpTopic](../FileDialog/FileDialog_SetHelpTopic.md) | Method that sets the HTML Help Topic to display when the help button is pressed in the FileDialog. |
| [ShowOpen](../FileDialog/FileDialog_ShowOpen.md) | Method that displays the open dialog. The existence of the specified file is checked for by the dialog, so only valid filenames will be returned. This does not actually open the file but only returns the filename the user has specified through the dialog. |
| [ShowSave](../FileDialog/FileDialog_ShowSave.md) | Method that displays the Save As dialog. If the user selects an existing file a warning message is displayed notifying them that the file already exists and the file will be overwritten if they continue. The use of this method does not actually perform a save but only returns the filename the user has specified through the dialog. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [CancelError](../FileDialog/FileDialog_CancelError.md) | Generate error when user cancels dialog if true. |
| [DialogTitle](../FileDialog/FileDialog_DialogTitle.md) | The string displayed in the dialog's title bar. |
| [FileDialogEvents](../FileDialog/FileDialog_FileDialogEvents.md) | Property that returns the FileDialogEvents object. |
| [FileName](../FileDialog/FileDialog_FileName.md) | The selected filename. Can be pre-set to initialize the selected filename in the dialog. |
| [Filter](../FileDialog/FileDialog_Filter.md) | The filter used to limit the types of files displayed in the dialog. |
| [FilterIndex](../FileDialog/FileDialog_FilterIndex.md) | The index of the default filter in the filter string (first index is 1). |
| [InitialDirectory](../FileDialog/FileDialog_InitialDirectory.md) | The initial directory displayed in the file dialog. This can also be set with the filename property. |
| [InsertMode](../FileDialog/FileDialog_InsertMode.md) | Gets and sets whether the FileDialog is being used for inserting a file (as opposed to opening one). If set to True, the OnFileInsertDialog event is fired by the ShowOpen method; if set to False, the OnFileOpenDialog event is fired. This defaults to True when a FileDialog is created. |
| [MultiSelectEnabled](../FileDialog/FileDialog_MultiSelectEnabled.md) | Gets and sets whether the 'Open' dialog should allow the selection of multiple files. If multiple files are selected by the user, the FileName property returns a string containing all selected file names delimited by a vertical bar ('|'). |
| [OptionsEnabled](../FileDialog/FileDialog_OptionsEnabled.md) | Gets and sets whether the 'Options' button on the dialog is enabled. If the button is enabled and the user clicks it, the OnOptions event is fired. |
| [OptionValues](../FileDialog/FileDialog_OptionValues.md) | Read-only property that returns the settings the user specified in the options dialog when a file type known to Inventor was selected. This includes the standard Inventor types (.ipt, .iam, .idw, etc.) and also any files types supported by any translator add-ins. In the case where it’s an unknown type (i.e. .txt, .xml), or if no options were specified this property will return Nothing.  The NameValueMap that’s returned can be used directly as the NameValueMap for the corresponding translator add-in. |
| [ShowQuickLaunch](../FileDialog/FileDialog_ShowQuickLaunch.md) | Gets and sets whether the quick launch controls on the dialog are visible or not. When the dialog is in insert mode the quick launch controls will be always hidden, so to show the quick launch controls the InsertMode should be set to False also. |
| [SuppressResolutionWarnings](../FileDialog/FileDialog_SuppressResolutionWarnings.md) | Specifies whether or not to warn that a file is being saved outside of a project resolvable location. |

## Accessed From

[Application.CreateFileDialog](../Application/Application_CreateFileDialog.md), [FileDialogEvents.Parent](../FileDialogEvents/FileDialogEvents_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [File Dialog](../../sample-programs/FileDialog_Sample.md) | This sample demonstrates the use of the FileDialog object. The only requirement to run this sample is to have Inventor open. |
| [Show online help sample for file dialog](../../sample-programs/ShowOnlineHelpForFileDialog_Sample.md) | The sample demonstrate how to set the online help for a file dialog. |

## Version

Introduced in version 6
