# ApprenticeServer.OpenWithOptions Method

Parent Object: [ApprenticeServer](../ApprenticeServer/ApprenticeServer.md)

## Description

Opens a document of the specified file-name with the specified set of options.

## Syntax

ApprenticeServer.**OpenWithOptions**( ***FullDocumentName*** As String, ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md) ) As [ApprenticeServerDocument](../ApprenticeServerDocument/ApprenticeServerDocument.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input String that specifies the full document name of the document to open. If only the FullFileName is specified for an assembly, the master document within the file is opened. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that specifies additional options for open. (An empty NameValueMap object can be provided). |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |