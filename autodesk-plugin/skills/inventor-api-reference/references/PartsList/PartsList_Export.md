# PartsList.Export Method

Parent Object: [PartsList](../PartsList/PartsList.md)

## Description

Method that saves the parts list to an external file.

## Remarks

Valid inputs for Options parameter:

| Name | Value Type | Valid for export formats |
| --- | --- | --- |
| TableName | String | kMicrosoftExcel |
| ExportedColumns | String containing semicolon separated column titles | All |
| IncludeTitle | Boolean | kMicrosoftExcel, kTextFileCommaDelimited, kTextFileTabDelimited, kUnicodeTextFileCommaDelimited, kUnicodeTextFileTabDelimited |
| StartingCell | String | kMicrosoftExcel |
| Template | String | kMicrosoftExcel |
| AutoFitColumnWidth | Boolean | kMicrosoftExcel |

## Syntax

PartsList.**Export**( ***FileName*** As String, ***FileFormat*** As [PartsListFileFormatEnum](../PartsListFileFormatEnum.md), [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input string that specifies the file name to export the parts list to. |
| FileFormat | [PartsListFileFormatEnum](../PartsListFileFormatEnum.md) | Input that specifies the file format to save to. |
| Options | Variant | Optional input NameValueMap object that specifies additional options for export. See Remarks for valid inputs. |

## Version

Introduced in version 9
