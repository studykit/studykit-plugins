# FileAccessEvents Object

## Description

The FileAccessEvents object supports a set of properties and events used to get access to files.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [FireOnFileResolution](../FileAccessEvents/FileAccessEvents_FireOnFileResolution.md) | Method that fires the OnFileResolution event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FileAccessEvents/FileAccessEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../FileAccessEvents/FileAccessEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../FileAccessEvents/FileAccessEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnFileDirty](../FileAccessEvents/FileAccessEvents_OnFileDirty.md) | The OnFileDirty event notifies a client when a document is about to become to dirty. |
| [OnFileResolution](../FileAccessEvents/FileAccessEvents_OnFileResolution.md) | The OnFileResolution event notifies a client whenever Inventor is trying to find the location of a file on disk. |

## Accessed From

[Application.FileAccessEvents](../Application/Application_FileAccessEvents.md), [InventorServer.FileAccessEvents](InventorServer_FileAccessEvents.md), [InventorServerObject.FileAccessEvents](InventorServerObject_FileAccessEvents.md)

## Version

Introduced in version 4
