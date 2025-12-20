# RevisionTable.Export Method

Parent Object: [RevisionTable](../RevisionTable/RevisionTable.md)

## Description

Saves the revision table to an external file.

## Syntax

RevisionTable.**Export**( ***FileName*** As String, ***FileFormat*** As [FileFormatEnum](../FileFormatEnum.md), [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input string that specifies the file name to export the revision table to. |
| FileFormat | [FileFormatEnum](../FileFormatEnum.md) | Input FileFormatEnum that specifies the file format to save to. |
| Options | Variant | Optional input NameValueMap object that specifies additional options for export. Valid inputs are listed in the table below.  | Name | Value Type | Valid for export formats | | --- | --- | --- | | TableName | String | kMicrosoftExcel | | ExportedColumns | String containing semicolon separated column titles | All | | IncludeTitle | Boolean | kMicrosoftExcel, kTextFileCommaDelimited, kTextFileTabDelimited, kUnicodeTextFileCommaDelimited, kUnicodeTextFileTabDelimited | | StartingCell | String | kMicrosoftExcel | | Template | String | kMicrosoftExcel | | AutoFitColumnWidth | Boolean | kMicrosoftExcel | |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |