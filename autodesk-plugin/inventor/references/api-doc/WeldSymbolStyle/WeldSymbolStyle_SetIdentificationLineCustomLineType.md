# WeldSymbolStyle.SetIdentificationLineCustomLineType Method

Parent Object: [WeldSymbolStyle](../WeldSymbolStyle/WeldSymbolStyle.md)

## Description

Sets a custom line type to the identification line from the specified .lin file.

## Syntax

WeldSymbolStyle.**SetIdentificationLineCustomLineType**( ***FullFileName*** As String, ***LineTypeName*** As String, ***ReplaceExisting*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input string that specifies the full file name of the \*.lin file containing the custom line types. |
| LineTypeName | String | Input string that specifies the name of the line type. |
| ReplaceExisting | Boolean | Input Boolean that specifies whether to replace the existing line type if a line type of the same name exists. If set to False, and a line type of the same name exists, this method returns an error. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |