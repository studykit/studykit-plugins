# Layer.SetCustomLineType Method

Parent Object: [Layer](../Layer/Layer.md)

## Description

Method that sets a custom line type to the entity from the specified .lin file. The method automatically changes the value of the LineType property to kCustomLineType.

## Syntax

Layer.**SetCustomLineType**( ***FullFileName*** As String, ***LineTypeName*** As String, ***ReplaceExisting*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | The full path and file name of the .lin file. |
| LineTypeName | String | The linetype name specified in the .lin file. |
| ReplaceExisting | Boolean | Indicates whether to override an existing line type of the same name. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |