# FileManager.CopyFile Method

Parent Object: [FileManager](../FileManager/FileManager.md)

## Description

Method that copies the specified Autodesk Inventor file (.ipt, .idw, .ipt etc.) from one location to another.

## Syntax

FileManager.**CopyFile**( ***SourceFullFileName*** As String, ***DestinationFullFileName*** As String, [***FileManagementOption***] As [FileManagementEnum](../FileManagementEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SourceFullFileName | String | Input String that specifies the full path and filename of the file to copy. |
| DestinationFullFileName | String | Input String that specifies the full path and filename in which to place the results of the copy procedure. |
| FileManagementOption | [FileManagementEnum](../FileManagementEnum.md) | Input constant that specifies how to handle the results of the file operation. |

## Version

Introduced in version 6
