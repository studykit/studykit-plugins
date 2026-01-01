# FileManagerEvents Object

## Description

The FileManagerEvents object provides access to file events, such as file deletion.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FileManagerEvents/FileManagerEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../FileManagerEvents/FileManagerEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../FileManagerEvents/FileManagerEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnFileCopy](../FileManagerEvents/FileManagerEvents_OnFileCopy.md) | Event that fires whenever a file is moved or copied using the MoveFile or CopyFile methods of the FileManager object. |
| [OnFileDelete](../FileManagerEvents/FileManagerEvents_OnFileDelete.md) | The OnFileDelete event notifies a client whenever a file is deleted using the DeleteFile method of the FileManager object. |

## Accessed From

[FileManager.FileManagerEvents](../FileManager/FileManager_FileManagerEvents.md)

## Version

Introduced in version 9
