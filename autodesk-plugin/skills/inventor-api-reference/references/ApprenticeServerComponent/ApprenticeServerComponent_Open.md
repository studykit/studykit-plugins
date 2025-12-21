# ApprenticeServerComponent.Open Method

Parent Object: [ApprenticeServerComponent](../ApprenticeServerComponent/ApprenticeServerComponent.md)

## Description

Opens a file. It can now be accessed as the top-level Document.

## Syntax

ApprenticeServerComponent.**Open**( ***FullDocumentName*** As String ) As [ApprenticeServerDocument](../ApprenticeServerDocument/ApprenticeServerDocument.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input String that specifies the full document name of the document to open. If only the FullFileName is specified for part and assembly documents, the master document within the file is opened. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Update iProperty values using Apprentice](../../sample-programs/iPropertyApprentice_Sample.md) | Updates some iProperty values using Apprentice. The document specified in the code for the Open method must exist. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |