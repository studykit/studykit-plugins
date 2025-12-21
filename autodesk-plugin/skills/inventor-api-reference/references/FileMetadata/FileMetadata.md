# FileMetadata Object

## Description

A container object for defining the name and file properties for an Inventor file.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [BOMStructure](../FileMetadata/FileMetadata_BOMStructure.md) | Gets and sets the default BOM structure. |
| [DisplayName](../FileMetadata/FileMetadata_DisplayName.md) | Gets and sets name of the file. |
| [DisplayNameOverridden](../FileMetadata/FileMetadata_DisplayNameOverridden.md) | Gets and sets whether the display name has been overridden. This property should be set by the (PDM) application that overrides the display name to indicate that the overridden display name should not be changed by the command or the user. Defaults to False. |
| [Document](../FileMetadata/FileMetadata_Document.md) | Gets and sets the document object for which the file name and properties are being requested. This can be set to Nothing if the document hasn’t yet been created. |
| [FileName](../FileMetadata/FileMetadata_FileName.md) | Gets and sets just the file name portion (no extension and no path) of the FullFileName string. |
| [FileNameOverridden](../FileMetadata/FileMetadata_FileNameOverridden.md) | Gets and sets whether the file name has been overridden. This property should be set by the (PDM) application that overrides the file name to indicate that the overridden file name should not be changed by the command or the user. Defaults to False. |
| [FileProperties](../FileMetadata/FileMetadata_FileProperties.md) | Gets and sets an XML string containing the values for file properties. |
| [FullFileName](../FileMetadata/FileMetadata_FullFileName.md) | Gets and sets the full file name (with the extension and the path). |
| [TemplateFileName](../FileMetadata/FileMetadata_TemplateFileName.md) | Gets and sets the full filename of the file used as the template when create a new file. |
| [Type](../FileMetadata/FileMetadata_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[TransientObjects.CreateFileMetadata](../TransientObjects/TransientObjects_CreateFileMetadata.md)

## Version

Introduced in version 2009
