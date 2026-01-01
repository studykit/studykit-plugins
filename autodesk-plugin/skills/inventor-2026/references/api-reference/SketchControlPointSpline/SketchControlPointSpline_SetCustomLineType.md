# SketchControlPointSpline.SetCustomLineType Method

Parent Object: [SketchControlPointSpline](../SketchControlPointSpline/SketchControlPointSpline.md)

## Description

Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType.

## Syntax

SketchControlPointSpline.**SetCustomLineType**( ***FullFileName*** As String, ***LineTypeName*** As String, ***ReplaceExisting*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input string that specifies the full file name of the \*.lin file containing the custom line types. |
| LineTypeName | String | OInput string that specifies the name of the line type. |
| ReplaceExisting | Boolean | Input Boolean that specifies whether to replace the existing line type if a line type of the same name exists. If set to False, and a line type of the same name exists, this method returns an error. |

## Version

Introduced in version 2014
