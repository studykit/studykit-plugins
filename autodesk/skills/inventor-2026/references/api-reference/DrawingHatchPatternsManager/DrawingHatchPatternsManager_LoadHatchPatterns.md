# DrawingHatchPatternsManager.LoadHatchPatterns Method

Parent Object: [DrawingHatchPatternsManager](../DrawingHatchPatternsManager/DrawingHatchPatternsManager.md)

## Description

Method that loads hatch patterns from a PAT file. If a hatch pattern has the same name as specified in the PatternDefinitionNames is already loaded, it will be replaced.

## Syntax

DrawingHatchPatternsManager.**LoadHatchPatterns**( ***FullFileName*** As String, ***PatternDefinitionNames***() As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String value that specifies the full file name of the PAT(.pat) file which contains hatch patterns. |
| PatternDefinitionNames | String | Input String array value that specifies the names of the hatch pattern definitions to load from the PAT file. |

## Version

Introduced in version 2021
