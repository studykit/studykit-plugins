# ApprenticeServer Object

## Description

Standalone mini component allowing limited access to an Inventor File. Refer to the Apprentice Server overview article.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Close](../ApprenticeServer/ApprenticeServer_Close.md) | Closes the current file. After this call there is no top-level Document. An attempt is also made to close the children Documents. |
| [Open](../ApprenticeServer/ApprenticeServer_Open.md) | Opens a file. It can now be accessed as the top-level Document |
| [OpenWithOptions](../ApprenticeServer/ApprenticeServer_OpenWithOptions.md) | Opens a document of the specified file-name with the specified set of options. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ApplicationAddIns](../ApprenticeServer/ApprenticeServer_ApplicationAddIns.md) | Gets all the Application AddIns found on this machine in a collection. |
| [DesignProjectManager](../ApprenticeServer/ApprenticeServer_DesignProjectManager.md) | Property that returns the DesignProjectManager object. |
| [DisplayAffinity](../ApprenticeServer/ApprenticeServer_DisplayAffinity.md) | Indicates the Boolean flag that fine tunes the performance of Apprentice when it is being used to display Inventor files. Defaults to false. |
| [DisplayOptions](../ApprenticeServer/ApprenticeServer_DisplayOptions.md) | Get the DisplayOptions object. |
| [Document](../ApprenticeServer/ApprenticeServer_Document.md) | Gets the top-level Apprentice Server Document. |
| [FileManager](../ApprenticeServer/ApprenticeServer_FileManager.md) | Gets the file manager object. |
| [FileOptions](../ApprenticeServer/ApprenticeServer_FileOptions.md) | Gets the File Options object. |
| [FileSaveAs](../ApprenticeServer/ApprenticeServer_FileSaveAs.md) | Gets the object that provides access to the helper object that provides the Save As facility. |
| [HardwareOptions](../ApprenticeServer/ApprenticeServer_HardwareOptions.md) | Get the HardwareOptions object. |
| [HelpManager](../ApprenticeServer/ApprenticeServer_HelpManager.md) | Gets the Help Manager object that provides access to the help-related activity taking place in the system. |
| [InstallPath](../ApprenticeServer/ApprenticeServer_InstallPath.md) | Property that returns the full path where Inventor/Apprentice is installed. |
| [Locale](../ApprenticeServer/ApprenticeServer_Locale.md) | Gets the Locale Id currently in use in Inventor. |
| [MultiUserExternallyManaged](../ApprenticeServer/ApprenticeServer_MultiUserExternallyManaged.md) | Get or set the Boolean flag indicating whether Multi-User facility is managed by Inventor or not. |
| [MultiUserMode](../ApprenticeServer/ApprenticeServer_MultiUserMode.md) | Get or set the enum indicating the Multi-User mode. |
| [SoftwareVersion](../ApprenticeServer/ApprenticeServer_SoftwareVersion.md) | Gets the object that encapsulates the version of the current software. |
| [TransientGeometry](../ApprenticeServer/ApprenticeServer_TransientGeometry.md) | Gets the object through which all transient geometry objects can be constructed. |
| [TransientObjects](../ApprenticeServer/ApprenticeServer_TransientObjects.md) | Property that returns the TransientObjects object. |
| [Type](../ApprenticeServer/ApprenticeServer_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserName](../ApprenticeServer/ApprenticeServer_UserName.md) | Get or set the string that identifies the current user. Inventor saves its own copy of this name per user and can thus be manipulated without effecting the rest of the OS. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |