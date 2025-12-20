# ComponentOccurrences.AddWithOptions Method

Parent Object: [ComponentOccurrences](../ComponentOccurrences/ComponentOccurrences.md)

## Description

Method that creates a new occurrence for an existing part or subassembly. This method is the equivalent of the "Place Component" command.

## Syntax

ComponentOccurrences.**AddWithOptions**( ***FullDocumentName*** As String, ***Position*** As [Matrix](../Matrix/Matrix.md), ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md) ) As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | Input string that specifies the full document name of the part or the sub-assembly. If only the FullFileName is specified, the master document within the file is used. |
| Position | [Matrix](../Matrix/Matrix.md) | Input Matrix object that defines the location and orientation to position the occurrence. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that specifies additional options for creating the occurrence. (An empty NameValueMap object can be provided). The valid options are:   |  |  |  | | --- | --- | --- | | **Name** | **Value Type** | **Valid Document Type** |  |  |  |  | | --- | --- | --- | | PrivateRepresentationFileName | String | Assembly |  |  |  |  | | --- | --- | --- | | DesignViewRepresentation | String | Part,Assembly |  |  |  |  | | --- | --- | --- | | DesignViewAssociative | Boolean | Part,Assembly |  |  |  |  | | --- | --- | --- | | PositionalRepresentation | String | Assembly |  |  |  |  | | --- | --- | --- | | ModelState | String | Part,Assembly |   **Notes:**  PrivateRepresentationFileName: If a PrivateRepresentationFileName (an idv file name) is specified, the DesignViewRepresentation name should be one of the private design views within that idv file else an error will occur.  ModelState: Typically, the ModelState to use should be provided in the form of a FullDocumentName (first argument). But if this is provided separately, you should make sure that it does not conflict with the FullDocumentName argument by providing FullFileName as the first argument rather than a FullDocumentName. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create assembly occurrence with representations](../../sample-programs/OccurrenceAddWithOptions_Sample.md) | This sample demonstrates how to create an assembly occurrence by specifying various representations. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |