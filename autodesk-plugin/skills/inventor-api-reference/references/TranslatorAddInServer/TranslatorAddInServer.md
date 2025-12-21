# TranslatorAddInServer Object

Derived from: [ApplicationAddInServer](../ApplicationAddInServer/ApplicationAddInServer.md) Object

## Description

Object required to be supported by Server to qualify as an Autodesk Inventor Translator AddIn.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../TranslatorAddInServer/TranslatorAddInServer_Activate.md) | Invoked by Autodesk Inventor after creating the AddIn. AddIn should initialize within this call. |
| [Deactivate](../TranslatorAddInServer/TranslatorAddInServer_Deactivate.md) | Invoked by Autodesk Inventor to shut down the AddIn. AddIn should complete shutdown within this call. |
| [ExecuteCommand](../TranslatorAddInServer/TranslatorAddInServer_ExecuteCommand.md) | Invoked by Autodesk Inventor in response to user requesting the execution of an AddIn-supplied command. AddIn must perform the command within this call. |
| [GetThumbnail](../TranslatorAddInServer/TranslatorAddInServer_GetThumbnail.md) | Obtains the thumbnail, if any, for the given data-source. Could be a metafile handle (long) or the interface to a StdPicture object. |
| [Open](../TranslatorAddInServer/TranslatorAddInServer_Open.md) | Open the data specified by the data-source. |
| [SaveCopyAs](../TranslatorAddInServer/TranslatorAddInServer_SaveCopyAs.md) | Save the specified document to the specified data-source. |
| [ShowOpenOptions](../TranslatorAddInServer/TranslatorAddInServer_ShowOpenOptions.md) | Show the open options for the specified data-source. This method is only called if True was returned from HasOpenOptions. |
| [ShowSaveCopyAsOptions](../TranslatorAddInServer/TranslatorAddInServer_ShowSaveCopyAsOptions.md) | Show the save options for the specified data-source. This method is only called if True was returned from HasSaveCopyAsOptions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Automation](../TranslatorAddInServer/TranslatorAddInServer_Automation.md) | Gets the IUnknown of the object implemented inside the AddIn that supports AddIn-specific API. |
| [HasOpenOptions](../TranslatorAddInServer/TranslatorAddInServer_HasOpenOptions.md) | Gets whether the translator has options available for opening the specified data-source. |
| [HasSaveCopyAsOptions](../TranslatorAddInServer/TranslatorAddInServer_HasSaveCopyAsOptions.md) | Gets whether the translator has options available for saving the specified data-source. |

## Version

Introduced in version 4
