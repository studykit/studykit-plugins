# SoftwareVersion Object

## Description

Object that encapsulates a given software version. Used in various contexts.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [BetaVersion](../SoftwareVersion/SoftwareVersion_BetaVersion.md) | Gets the Beta version. If this is not a Beta version software, this value will be zero. |
| [BuildIdentifier](../SoftwareVersion/SoftwareVersion_BuildIdentifier.md) | Gets the number that completely identifies a particular build of Autodesk Inventor. |
| [DisplayName](../SoftwareVersion/SoftwareVersion_DisplayName.md) | Gets the human-readable, displayable name designating this particular version (e.g.: 'Autodesk Inventor (tm) Release 2.5 Service Pack 3'). |
| [DisplayVersion](../SoftwareVersion/SoftwareVersion_DisplayVersion.md) | Returns the release version displayed to users. (e.g.: '2009' for Major version 13 or '2010' for Major version 14) |
| [Is64BitVersion](../SoftwareVersion/SoftwareVersion_Is64BitVersion.md) | Always false in 32-bit Inventor. Use this property to find out whether your code is connected to a 64-bit version of Inventor. |
| [IsEducationVersion](../SoftwareVersion/SoftwareVersion_IsEducationVersion.md) | Returns whether this is an educational versions of Inventor. |
| [Major](../SoftwareVersion/SoftwareVersion_Major.md) | Gets the Major release number (e.g.: Release '1', '2', ...). |
| [Minor](../SoftwareVersion/SoftwareVersion_Minor.md) | Gets the Minor release number. If none, a zero is returned. (e.g.: the '5' in release 1.5). |
| [NotProduction](../SoftwareVersion/SoftwareVersion_NotProduction.md) | Gets a Boolean flag indicating whether this software is intended for purely internal purposes or not. Beta is considered external. |
| [ProductEdition](../SoftwareVersion/SoftwareVersion_ProductEdition.md) | Gets the product edition. Only valid when SoftwareVersion is obtained from the Application. |
| [ProductName](../SoftwareVersion/SoftwareVersion_ProductName.md) | Gets the product name. Only valid when SoftwareVersion is obtained from the Application. |
| [ServicePack](../SoftwareVersion/SoftwareVersion_ServicePack.md) | Gets the number of the Service Pack if this software has been updated with such. If none, a zero is returned. (e.g.: the '3' in Release 2.5 Service Pack 3). |
| [Type](../SoftwareVersion/SoftwareVersion_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.SoftwareVersion](../Application/Application_SoftwareVersion.md), [ApprenticeServer.SoftwareVersion](../ApprenticeServer/ApprenticeServer_SoftwareVersion.md), [ApprenticeServerComponent.SoftwareVersion](../ApprenticeServerComponent/ApprenticeServerComponent_SoftwareVersion.md), [ApprenticeServerDocument.SoftwareVersionCreated](../ApprenticeServerDocument/ApprenticeServerDocument_SoftwareVersionCreated.md), [ApprenticeServerDocument.SoftwareVersionSaved](../ApprenticeServerDocument/ApprenticeServerDocument_SoftwareVersionSaved.md), [ApprenticeServerDrawingDocument.SoftwareVersionCreated](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_SoftwareVersionCreated.md), [ApprenticeServerDrawingDocument.SoftwareVersionSaved](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_SoftwareVersionSaved.md), [AssemblyDocument.SoftwareVersionCreated](../AssemblyDocument/AssemblyDocument_SoftwareVersionCreated.md), [AssemblyDocument.SoftwareVersionSaved](../AssemblyDocument/AssemblyDocument_SoftwareVersionSaved.md), [Document.SoftwareVersionCreated](../Document/Document_SoftwareVersionCreated.md), [Document.SoftwareVersionSaved](../Document/Document_SoftwareVersionSaved.md), [DrawingDocument.SoftwareVersionCreated](../DrawingDocument/DrawingDocument_SoftwareVersionCreated.md), [DrawingDocument.SoftwareVersionSaved](../DrawingDocument/DrawingDocument_SoftwareVersionSaved.md), [File.SoftwareVersionCreated](../File/File_SoftwareVersionCreated.md), [File.SoftwareVersionSaved](../File/File_SoftwareVersionSaved.md), [FileManager.SoftwareVersionSaved](../FileManager/FileManager_SoftwareVersionSaved.md), [InventorServer.SoftwareVersion](InventorServer_SoftwareVersion.md), [InventorServerObject.SoftwareVersion](InventorServerObject_SoftwareVersion.md), [PartDocument.SoftwareVersionCreated](../PartDocument/PartDocument_SoftwareVersionCreated.md), [PartDocument.SoftwareVersionSaved](../PartDocument/PartDocument_SoftwareVersionSaved.md), [PresentationDocument.SoftwareVersionCreated](../PresentationDocument/PresentationDocument_SoftwareVersionCreated.md), [PresentationDocument.SoftwareVersionSaved](../PresentationDocument/PresentationDocument_SoftwareVersionSaved.md)

## Version

Introduced in version 4
