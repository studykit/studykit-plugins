# ApprenticeServerComponent.OpenWithOptions Method

Parent Object: [ApprenticeServerComponent](../ApprenticeServerComponent/ApprenticeServerComponent.md)

## Description

Opens a document of the specified file-name with the specified set of options.

## Remarks

When opening non-Inventor DWG files, this method honors the application option to decide between open and import, unless an override is specified in the Options argument.

Valid Options arguments are:

| Name Value | Type | Valid Document | Notes |
| --- | --- | --- | --- |
| DesignViewRepresentation | String | Part,Assembly |  |
| PositionalRepresentation | String | Assembly |  |
| ModelState | String | Part,Assembly | Typically, the ModelState to use should be provided in the form of a FulDocumentName (first argument). But if this is provided separately, you should make sure that it does not conflict with the FullDocumentName argument by providing FullFileName as the first argument rather than a FullDocumentName. |
| DeferUpdates | Boolean | Drawing |  |
| FileVersionOption | FileVersionEnum | All | Valid values for FileVersionEnum are kOpenOldVersion, kOpenCurrentVersion and kRestoreOldVersionToCurrent. If set to kOpenOldVersion, save will not be allowed on the opened document. kRestoreOldVersionToCurrent is valid only if no other versions are open and the current version is not checked out. |
| ImportNonInventorDWG | Boolean | Imports the DWG file to an IDW if True, Opens it into Inventor DWG if False | When opening non-Inventor DWG files, this method honors the application option to decide between open and import, unless an override is specified in the Options argument. |
| Password | String | All |  |
| SkipAllUnresolvedFiles | Boolean | All |  |

## Syntax

ApprenticeServerComponent.**OpenWithOptions**( ***FullDocumentName*** As String, ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md) ) As [ApprenticeServerDocument](../ApprenticeServerDocument/ApprenticeServerDocument.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input String that specifies the full document name of the document to open. If only the FullFileName is specified for part and assembly documents, the master document within the file is opened. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that specifies additional options for open. (An empty NameValueMap object can be provided). See Remarks section for the valid options. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |