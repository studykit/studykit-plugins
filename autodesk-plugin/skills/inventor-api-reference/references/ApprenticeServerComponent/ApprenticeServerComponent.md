# ApprenticeServerComponent Object

## Description

Inventor::ApprenticeServer

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Close](../ApprenticeServerComponent/ApprenticeServerComponent_Close.md) | Closes the current file. After this call there is no top-level Document. Attempt is also made to close the children Documents. |
| [Close2](../ApprenticeServerComponent/ApprenticeServerComponent_Close2.md) | Closes the current file. After this call there is no top-level Document. Optionally forces any child Documents to close. |
| [Open](../ApprenticeServerComponent/ApprenticeServerComponent_Open.md) | Opens a file. It can now be accessed as the top-level Document. |
| [OpenWithOptions](../ApprenticeServerComponent/ApprenticeServerComponent_OpenWithOptions.md) | Opens a document of the specified file-name with the specified set of options. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ApplicationAddIns](../ApprenticeServerComponent/ApprenticeServerComponent_ApplicationAddIns.md) | Gets all the Application AddIns found on this machine in a collection. |
| [DesignProjectManager](../ApprenticeServerComponent/ApprenticeServerComponent_DesignProjectManager.md) | Gets the design project manager object. |
| [DisplayAffinity](../ApprenticeServerComponent/ApprenticeServerComponent_DisplayAffinity.md) | Gets/Sets the Boolean flag that fine tunes the performance of Apprentice when it is being used to display Inventor files. Defaults to false. |
| [DisplayOptions](../ApprenticeServerComponent/ApprenticeServerComponent_DisplayOptions.md) | Gets the Display Options object. |
| [Document](../ApprenticeServerComponent/ApprenticeServerComponent_Document.md) | Gets the top-level Apprentice Server Document. |
| [FileManager](../ApprenticeServerComponent/ApprenticeServerComponent_FileManager.md) | Gets the file manager object. |
| [FileOptions](../ApprenticeServerComponent/ApprenticeServerComponent_FileOptions.md) | Gets the File Options object. |
| [FileSaveAs](../ApprenticeServerComponent/ApprenticeServerComponent_FileSaveAs.md) | Gets the object that provides access to the helper object that provides the Save As facility. |
| [HardwareOptions](../ApprenticeServerComponent/ApprenticeServerComponent_HardwareOptions.md) | Gets the Hardware Options. |
| [HelpManager](../ApprenticeServerComponent/ApprenticeServerComponent_HelpManager.md) | Gets the Help Manager object that provides access to the help-related activity taking place in the system. |
| [InstallPath](../ApprenticeServerComponent/ApprenticeServerComponent_InstallPath.md) | Read-only property that returns the full path where Inventor/Apprentice is installed. |
| [Locale](../ApprenticeServerComponent/ApprenticeServerComponent_Locale.md) | Gets the Locale Id currently in use in Inventor. |
| [MultiUserExternallyManaged](../ApprenticeServerComponent/ApprenticeServerComponent_MultiUserExternallyManaged.md) | Gets/Sets the Boolean flag indicating whether Multi-User facility is managed by Inventor or not. |
| [MultiUserMode](../ApprenticeServerComponent/ApprenticeServerComponent_MultiUserMode.md) | Gets/Sets the enum indicating the Multi-User mode. |
| [SoftwareVersion](../ApprenticeServerComponent/ApprenticeServerComponent_SoftwareVersion.md) | Gets the object that encapsulates the version of the current software. |
| [TransientGeometry](../ApprenticeServerComponent/ApprenticeServerComponent_TransientGeometry.md) | Gets the object through which all transient geometry objects can be constructed. |
| [TransientObjects](../ApprenticeServerComponent/ApprenticeServerComponent_TransientObjects.md) | Gets the TransientObjects object. |
| [Type](../ApprenticeServerComponent/ApprenticeServerComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserName](../ApprenticeServerComponent/ApprenticeServerComponent_UserName.md) | Gets/Sets the string that identifies the current user. Inventor saves its own copy of this name per user and can thus be manipulated without effecting the rest of the OS. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Update iProperty values using Apprentice](../../sample-programs/iPropertyApprentice_Sample.md) | Updates some iProperty values using Apprentice. The document specified in the code for the Open method must exist. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |