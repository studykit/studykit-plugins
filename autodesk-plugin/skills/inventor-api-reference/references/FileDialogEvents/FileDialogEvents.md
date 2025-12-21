# FileDialogEvents Object

## Description

The FileDialogEvents object hosts events related to the FileDialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FileDialogEvents/FileDialogEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../FileDialogEvents/FileDialogEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../FileDialogEvents/FileDialogEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnOptions](../FileDialogEvents/FileDialogEvents_OnOptions.md) | Event that fires when the user clicks the Options button on the file dialog. This event can be used to put up customized option pages. |
| [OnOptionsReset](../FileDialogEvents/FileDialogEvents_OnOptionsReset.md) | Fires when the action to reset options on the file dialog occurs, e.g. file filter type changes, etc. |

## Accessed From

[FileDialog.FileDialogEvents](../FileDialog/FileDialog_FileDialogEvents.md)

## Version

Introduced in version 2008
