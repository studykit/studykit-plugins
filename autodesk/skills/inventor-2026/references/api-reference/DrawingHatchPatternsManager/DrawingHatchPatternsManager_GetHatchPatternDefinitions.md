# DrawingHatchPatternsManager.GetHatchPatternDefinitions Method

Parent Object: [DrawingHatchPatternsManager](../DrawingHatchPatternsManager/DrawingHatchPatternsManager.md)

## Description

Method that gets the hatch pattern definitions from a PAT file.

## Syntax

DrawingHatchPatternsManager.**GetHatchPatternDefinitions**( ***FullFileName*** As String, ***PatternDefinitionNames***() As String, ***Descriptions***() As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String value that specifies the full file name of the PAT(.pat) file which contains hatch patterns. |
| PatternDefinitionNames | String | Output String array that returns the names of the hatch pattern definitions in the PAT file. |
| Descriptions | String | Output String array that returns the description strings of the hatch pattern definitions.The Descriptions and PatternDefinitionNames are returned in the same order within each array that the name and description to the name and the description of the same index will be the same pattern. |

## Version

Introduced in version 2021
