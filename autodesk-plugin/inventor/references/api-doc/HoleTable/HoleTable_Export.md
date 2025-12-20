# HoleTable.Export Method

Parent Object: [HoleTable](../HoleTable/HoleTable.md)

## Description

Method that saves the custom table to an external file.

## Remarks

Valid inputs for Options parameter:

| Name | Value type | Valid for Export formats |
| --- | --- | --- |
| TableName | String | kMicrosoftExcel |
| ExportedColumns | String containing semicolon separated column titles | All |
| IncludeTitle | Boolean | kMicrosoftExcel, kTextFileCommaDelimited, kTextFileTabDelimited, kUnicodeTextFileCommaDelimited, kUnicodeTextFileTabDelimited |
| StartingCell | String | kMicrosoftExcel |
| Template | String | kMicrosoftExcel |
| AutoFitColumnWidth | Boolean | kMicrosoftExcel |

## Syntax

HoleTable.**Export**( ***FileName*** As String, ***FileFormat*** As [FileFormatEnum](../FileFormatEnum.md), [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input string that specifies the file name to export the table to. The valid file extension for this file are .csv and .txt. |
| FileFormat | [FileFormatEnum](../FileFormatEnum.md) | Input FileFormatEnum to specify the file format to export. Valid values for export hole tables are:kTextFileCommaDelimitedFormat, kTextFileTabDelimitedFormat, kUnicodeTextFileCommaDelimitedFormat and kUnicodeTextFileTabDelimitedFormat. |
| Options | Variant | Optional input NameValueMap object that specifies additional options for export. See Remarks for valid inputs: |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |