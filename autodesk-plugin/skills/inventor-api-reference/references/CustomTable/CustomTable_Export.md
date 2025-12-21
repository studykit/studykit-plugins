# CustomTable.Export Method

Parent Object: [CustomTable](../CustomTable/CustomTable.md)

## Description

Method that saves the custom table to an external file.

## Remarks

Valid values for the Options parameter:

| Name | Value Type | Valid for export formats |
| --- | --- | --- |
>| TableName | String | kMicrosoftExcel |
| ExportedColumns | String | All containing semicolon separated column titles |
| IncludeTitle | Boolean | kMicrosoftExcel, kTextFileCommaDelimited, kTextFileTabDelimited, kUnicodeTextFileCommaDelimited, kUnicodeTextFileTabDelimited |
>|> StartingCell | String | kMicrosoftExcel |
 Template | String | kMicrosoftExcel || AutoFitColumnWidth | Boolean | kMicrosoftExcel |
>

## Syntax

CustomTable.**Export**( ***FileName*** As String, ***FileFormat*** As [FileFormatEnum](../FileFormatEnum.md), [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input string that specifies the file name to export the table to. |
| FileFormat | [FileFormatEnum](../FileFormatEnum.md) | Input FileFormatEnum that specifies the file format to save to. |
| Options | Variant | Optional input NameValueMap object that specifies additional options for export. See Remarks for valid options: |

## Version

Introduced in version 2009
