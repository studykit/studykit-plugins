# TranslatorAddIn Object

Derived from: [ApplicationAddIn](../ApplicationAddIn/ApplicationAddIn.md) Object

## Description

Object that represents an Translator AddIn inside Autodesk Inventor.

## Remarks

See the [Translator Options](TranslatorSettings.md) page for details about the supported options for each of the translators. The samples below are also very useful in understanding the steps required to use a translator add-in.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../TranslatorAddIn/TranslatorAddIn_Activate.md) | Creates and initializes the AddIn. No effect if AddIn already active. |
| [Deactivate](../TranslatorAddIn/TranslatorAddIn_Deactivate.md) | Invokes the shutdown sequence on the AddIn. No effect if AddIn inactive. |
| [GetThumbnail](../TranslatorAddIn/TranslatorAddIn_GetThumbnail.md) | Obtains the thumbnail, if any, for the given data-source. Could be a metafile handle (long) or the interface to a StdPicture object. |
| [Open](../TranslatorAddIn/TranslatorAddIn_Open.md) | Open the data specified by the data-source. |
| [SaveCopyAs](../TranslatorAddIn/TranslatorAddIn_SaveCopyAs.md) | Save the document to the specified data-source. |
| [ShowOpenOptions](../TranslatorAddIn/TranslatorAddIn_ShowOpenOptions.md) | Show the open options for the specified data-source. This method is only called if True was returned from HasOpenOptions. |
| [ShowSaveCopyAsOptions](../TranslatorAddIn/TranslatorAddIn_ShowSaveCopyAsOptions.md) | Show the save options for the specified data-source. This method is only called if True was returned from HasSaveCopyAsOptions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Activated](../TranslatorAddIn/TranslatorAddIn_Activated.md) | Gets a Boolean flag indicating whether this AddIn is currently active in the session. |
| [AddInType](../TranslatorAddIn/TranslatorAddIn_AddInType.md) | Gets the constant that indicates the type of this AddIn. |
| [Application](../TranslatorAddIn/TranslatorAddIn_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Automation](../TranslatorAddIn/TranslatorAddIn_Automation.md) | Property that returns the Add-in's automation interface (if any). Fails if the Add-in is currently inactive. |
| [ClassIdString](../TranslatorAddIn/TranslatorAddIn_ClassIdString.md) | Gets the CLSID of the AddIn as the string used in the class moniker. |
| [ClientId](../TranslatorAddIn/TranslatorAddIn_ClientId.md) | Property that returns a GUID in string format that uniquely identifies this Add-in. This GUID is used as an identifier when creating Add-in specific objects such as user interface elements, client features, etc. |
| [DataVersion](../TranslatorAddIn/TranslatorAddIn_DataVersion.md) | Gets and sets the current data version of the AddIn. This value corresponds to the 'Data Version' registry entry in the AddIn's registry hive. |
| [Description](../TranslatorAddIn/TranslatorAddIn_Description.md) | Gets the description of the AddIn. |
| [DisplayName](../TranslatorAddIn/TranslatorAddIn_DisplayName.md) | Gets the displayable name of the AddIn. |
| [FileExtensions](../TranslatorAddIn/TranslatorAddIn_FileExtensions.md) | Property that gets the semicolon-separated list of the native file extensions that this translator reads from and/or writes to. |
| [FilterText](../TranslatorAddIn/TranslatorAddIn_FilterText.md) | Property that gets the filter text string to be displayed in the file dialog for this translator. |
| [HasOpenOptions](../TranslatorAddIn/TranslatorAddIn_HasOpenOptions.md) | Gets whether the translator has options available for opening the specified data-source. |
| [HasSaveCopyAsOptions](../TranslatorAddIn/TranslatorAddIn_HasSaveCopyAsOptions.md) | Gets whether the translator has options available for saving the specified data-source. |
| [Hidden](../TranslatorAddIn/TranslatorAddIn_Hidden.md) | Gets and sets whether the AddIn is hidden or not. |
| [LicenseStatus](../TranslatorAddIn/TranslatorAddIn_LicenseStatus.md) | Gets the license status of the AddIn. |
| [LoadAutomatically](../TranslatorAddIn/TranslatorAddIn_LoadAutomatically.md) | Gets/Sets whether the add-in loads automatically based on the load behavior specified for the add-in. If set to False, the add-in needs to be manually loaded by the user. |
| [LoadBehavior](../TranslatorAddIn/TranslatorAddIn_LoadBehavior.md) | Gets a constant indicating the load behavior (load time) of the add-in. This applies only if the LoadAutomatically property is set to True. |
| [Location](../TranslatorAddIn/TranslatorAddIn_Location.md) | Property that returns the full file name of the dll associated with this Add-in. |
| [Parent](../TranslatorAddIn/TranslatorAddIn_Parent.md) | Property that returns the parent Application object. |
| [ProgId](../TranslatorAddIn/TranslatorAddIn_ProgId.md) | Gets the ProgID of the AddIn. |
| [ShortDisplayName](../TranslatorAddIn/TranslatorAddIn_ShortDisplayName.md) | Property that returns the short display name of the Add-in. Used in places to succinctly identify the AddIn inside Inventor's UI. |
| [SupportsImportInto](../TranslatorAddIn/TranslatorAddIn_SupportsImportInto.md) | Property that returns semicolon-separated Inventor file types that this translator supports importing into. Example: ".iam;.ipt." |
| [SupportsOpen](../TranslatorAddIn/TranslatorAddIn_SupportsOpen.md) | Property that gets whether this translator supports opening files. |
| [SupportsOpenInto](../TranslatorAddIn/TranslatorAddIn_SupportsOpenInto.md) | Property that returns semicolon-separated Inventor file types that this translator supports opening into. Example: ".iam;.ipt." |
| [SupportsSaveCopyAs](../TranslatorAddIn/TranslatorAddIn_SupportsSaveCopyAs.md) | Property that gets whether this translator supports saving data to a file. |
| [SupportsSaveCopyAsFrom](../TranslatorAddIn/TranslatorAddIn_SupportsSaveCopyAsFrom.md) | Property that returns semicolon-separated Inventor file types that this translator supports saving from. Example: ".iam;.ipt." |
| [TranslatorAvailable](../TranslatorAddIn/TranslatorAddIn_TranslatorAvailable.md) | Gets/Sets a Boolean flag indicating whether this Translator is available to Inventor, regardless of whether it is loaded or not. |
| [Type](../TranslatorAddIn/TranslatorAddIn_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserInterfaceVersion](../TranslatorAddIn/TranslatorAddIn_UserInterfaceVersion.md) | Property that returns the version of the user interface of the add-in. Incrementing this version results in all of the add-in"s UI getting cleaned up during Inventor start-up. |
| [UserUnloadable](../TranslatorAddIn/TranslatorAddIn_UserUnloadable.md) | Gets and sets whether the AddIn is allowed to be unloaded by the user. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Open a Catia file using the Catia Translator Sample](../../sample-programs/ImportCatiaTranslator_Sample.md) | This sample demonstrates how open an Catia file using the Catia translator add-in. |
| [Open an NX file suing the NX Translator Sample](../../sample-programs/ImportNXTranslator_Sample.md) | This sample demonstrates how open an NX file using the NX translator add-in. |
| [Open Rhino Translator Sample](../../sample-programs/ImportRhinoTranslator_Sample.md) | This sample demonstrates how to opening a Rhino file using the Rhino translator add-in. |
| [Open an STL file using the STL Translator Sample](../../sample-programs/ImportSTLslator_Sample.md) | This sample demonstrates how open an STL file using the STL translator add-in. |
| [Save as DWF Translator Sample](../../sample-programs/SaveAsDWFTranslator_Sample.md) | This sample demonstrates how to save a DWF file using the DWF translator add-in. |
| [Save as DWG Translator Sample](../../sample-programs/SaveAsDWGTranslator_Sample.md) | This sample demonstrates how to save a DWG file using the DWG translator add-in. |
| [Save as DXF Translator Sample](../../sample-programs/SaveAsDXFTranslator_Sample.md) | This sample demonstrates how to save a DXF file using the DXF translator add-in. |
| [Save as IGES Translator Sample](../../sample-programs/SaveAsIGESTranslator_Sample.md) | This sample demonstrates how to save a IGES file using the IGES translator add-in. |
| [Save as PDF Translator Sample](../../sample-programs/SaveAsPDFTranslator_Sample.md) | This sample demonstrates how to save a PDF file using the PDF translator add-in. |
| [Save as STEP Translator Sample](../../sample-programs/SaveAsSTEPTranslator_Sample.md) | This sample demonstrates how to save a STEP file using the STEP translator add-in. |
| [Export to DWF](../../sample-programs/TranslatorAddIn_Sample.md) | This sample demonstrates publishing of Inventor files in DWF format. |
| [Export to DWG](../../sample-programs/TranslatorAddIn2_Sample.md) | This sample uses the DWG Translator Addin to publish to DWG. |
| [Export to DXF](../../sample-programs/TranslatorAddIn3_Sample.md) | This sample uses the DXF Translator Addin to publish to DXF. |
| [Export to IGES](../../sample-programs/TranslatorAddIn4_Sample.md) | This sample demonstrates exporting of Inventor files in IGES format. |
| [Export to STEP](../../sample-programs/TranslatorAddIn5_Sample.md) | This sample demonstrates exporting of Inventor files in STEP format. |
| [Export to PDF](../../sample-programs/TranslatorAddIn6_Sample.md) | This sample demonstrates exporting of Inventor files in PDF format. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |