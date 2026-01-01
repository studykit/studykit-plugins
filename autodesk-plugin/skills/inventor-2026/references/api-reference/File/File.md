# File Object

## Description

The File object represents an Inventor file on disk.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllReferencedFiles](../File/File_AllReferencedFiles.md) | Property that returns all the file references of this File along with all of the recursively nested references. |
| [Application](../File/File_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AvailableDocuments](../File/File_AvailableDocuments.md) | Property that returns an enumeration of all the documents within this file that are currently available (i.e. have been initialized). The returned documents may or may not be open. The property returns a DocumentsEnumerator object in Inventor and a ApprenticeServerDocuments in Apprentice. |
| [DatabaseRevisionId](../File/File_DatabaseRevisionId.md) | Gets the GUID that represents the last saved revision of database contained in this file. This revision id tracks modifications to the database (such as reference changes, geometry changes, etc.) but does not track file property changes. |
| [FileSaveCounter](../File/File_FileSaveCounter.md) | Returns the number that is indicative of the number of times the file has been saved. |
| [FullFileName](../File/File_FullFileName.md) | Gets and sets the fully qualified name of this file. This property can only be set if this file has never been saved. |
| [HasLoadedDocuments](../File/File_HasLoadedDocuments.md) | Read-only property that returns whether any documents within this file is loaded or not. |
| [HasReferencingFiles](../File/File_HasReferencingFiles.md) | Read-only property that returns whether this file is referenced by any other files in memory or not. |
| [InternalName](../File/File_InternalName.md) | Property that gets the Internal Name (a GUID) for this File. |
| [ReferencedFileDescriptors](../File/File_ReferencedFileDescriptors.md) | Property that returns an enumeration of descriptors that represent the direct file references held by this file. |
| [ReferencedFiles](../File/File_ReferencedFiles.md) | Property that returns all the files directly referenced by this file. |
| [ReferencingFiles](../File/File_ReferencingFiles.md) | Property that returns all the files in memory that reference this file. |
| [RevisionId](../File/File_RevisionId.md) | Gets the GUID that represents the last saved revision of this file. Works as a stamp of the contents of this file. |
| [SoftwareVersionCreated](../File/File_SoftwareVersionCreated.md) | Read-only property that returns object that encapsulates version of the software with which this file was created. |
| [SoftwareVersionSaved](../File/File_SoftwareVersionSaved.md) | Read-only property that returns object that encapsulates version of the software with which this file was last saved. |
| [Type](../File/File_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ApprenticeServerDocument.File](../ApprenticeServerDocument/ApprenticeServerDocument_File.md), [ApprenticeServerDrawingDocument.File](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_File.md), [AssemblyDocument.File](../AssemblyDocument/AssemblyDocument_File.md), [Document.File](../Document/Document_File.md), [DrawingDocument.File](../DrawingDocument/DrawingDocument_File.md), [FileDescriptor.Parent](../FileDescriptor/FileDescriptor_Parent.md), [FileDescriptor.ReferencedFile](../FileDescriptor/FileDescriptor_ReferencedFile.md), [FilesEnumerator.Item](../FilesEnumerator/FilesEnumerator_Item.md), [PartDocument.File](../PartDocument/PartDocument_File.md), [PresentationDocument.File](../PresentationDocument/PresentationDocument_File.md)

## Version

Introduced in version 11
