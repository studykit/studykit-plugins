# FileManager.GetDesignViewRepresentations Method

Parent Object: [FileManager](../FileManager/FileManager.md)

## Description

Method that returns the names of all the design view representations contained within the input file (either \*.iam, \*.ipt or \*.idv).

## Remarks

Returned in the following order:

1. Last Active
2. Master
3. All Visible
4. Nothing Visible
5. Default
6. Other

## Syntax

FileManager.**GetDesignViewRepresentations**( ***FullFileName*** As String ) As String()

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String that specifies the file (\*.iam, \*.ipt or \*.idv) to retrieve the design view names from. A FullDocumentName can also be specified. If an idv file is specified, the private design views contained within it are returned. |

## Version

Introduced in version 11
