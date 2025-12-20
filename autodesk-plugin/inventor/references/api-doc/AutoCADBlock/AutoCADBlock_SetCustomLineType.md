# AutoCADBlock.SetCustomLineType Method

Parent Object: [AutoCADBlock](../AutoCADBlock/AutoCADBlock.md)

## Description

Method that sets a custom line type to the symbol from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType.

## Syntax

AutoCADBlock.**SetCustomLineType**( ***FullFileName*** As String, ***LineTypeName*** As String, ***ReplaceExisting*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Specifies the full file name of the \*.lin file containing the custom line types. |
| LineTypeName | String | Specifies the name of the line type. |
| ReplaceExisting | Boolean | Specifies whether to replace the existing line type if a line type of the same name exists. If set to False, and a line type of the same name exists, this method returns an error. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |