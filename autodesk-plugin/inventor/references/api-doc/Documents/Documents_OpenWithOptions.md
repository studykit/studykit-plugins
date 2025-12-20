# Documents.OpenWithOptions Method

Parent Object: [Documents](../Documents/Documents.md)

## Description

Method that opens the specified Inventor document.

## Remarks

Valid values for the NameValueMap in the Options argument:

| Name | Type | Valid Document Type | Notes |
| --- | --- | --- | --- |
| DesignViewRepresentation | String | Part, Assembly | The name of the design view representation. If empty string is input then thhis will be ignored, and the setting in the FileOpenOptions will be applied. |
| PositionalRepresentation | String | Assembly | The name of the positional representation. |
| ModelState | String | Part,Assembly | Typically, the ModelState to use should be provided in the form of a FulDocumentName (first argument). But if this is provided separately, you should make sure that it does not conflict with the FullDocumentName argument by providing FullFileName as the first argument rather than a FullDocumentName. |
| DeferUpdates | Boolean | Drawing | Indicates if any pending updates for the drawing will be deferred when the drawing is opened. |
| FileVersionOption | Value from FileVersionEnum | All | Valid values for FileVersionEnum are kOpenOldVersion, kOpenCurrentVersion and kRestoreOldVersionToCurrent. If set to kOpenOldVersion, save will not be allowed on the opened document. kRestoreOldVersionToCurrent is valid only if no other versions are open and the current version is not checked out. |
| ImportNonInventorDWG | Boolean | Imports the DWG file to an IDW if True, Opens it into Inventor DWG if False | When opening non-Inventor DWG files, this method honors the application option to decide between open and import, unless an override is specified in the Options argument. |
| Password | String | All |  |
| ExpressModeBehavior | String | Assembly | The following values are valid for this setting: OpenExpress - Open the assembly in express mode. OpenFull - Open the assembly in full mode. OpenDefault - Open the assembly in the mode it was saved in. |
| SkipAllUnresolvedFiles | Boolean | All | Indicates to skip all unresolved files and continue to open the document. |
| DeferFlatPatternUpdate | Boolean | Part | Indicates whether to defer the flat pattern compute or not when open a part with flat pattern in it. |

## Syntax

Documents.**OpenWithOptions**( ***FullDocumentName*** As String, ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md), [***OpenVisible***] As Boolean ) As [Document](../Document/Document.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input String that specifies the full document name of the document to open. If only the FullFileName is specified for an assembly, the master document within the file is opened. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that specifies additional options for open. (An empty NameValueMap object can be provided). See Remarks section for the valid options. |
| OpenVisible | Boolean | Optional input Boolean that specifies whether to open the document as visible. If not specified, the document is opened visible. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |