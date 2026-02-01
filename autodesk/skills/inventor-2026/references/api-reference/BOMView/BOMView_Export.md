# BOMView.Export Method

Parent Object: [BOMView](../BOMView/BOMView.md)

## Description

Method that saves the BOM as viewed in this BOM view to an external file.

## Syntax

BOMView.**Export**( ***FileName*** As String, ***FileFormat*** As [FileFormatEnum](../FileFormatEnum.md), [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input string that specifies the file name to export the BOM to. |
| FileFormat | [FileFormatEnum](../FileFormatEnum.md) | Input FileFormatEnum that specifies the file format to save to. |
| Options | Variant | Optional input String or NameValueMap that specifies more options when the FileFormat is specified as kMicrosoftExcel, otherwise this is ignored. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Exporting the assembly BOM](../../sample-programs/BOMView_Export_Sample.md) | This sample demonstrates exporting the Assembly BOM to an external file. |

## Version

Introduced in version 2009
