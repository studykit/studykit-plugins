# BOM.GetPartNumberMergeSettings2 Method

Parent Object: [BOM](../BOM/BOM.md)

## Description

Gets the part number row merge settings for the BOM.

## Syntax

BOM.**GetPartNumberMergeSettings2**( ***MergeEnabled*** As Boolean, ***MergeExcludeList***() As String, ***MergeInstanceRows*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MergeEnabled | Boolean | Output Boolean that indicates whether the row merging based on part number match is enabled. |
| MergeExcludeList | String | Output array that returns the strings to exclude when merging based on part number match. This array will contain a minimum of one string (“”). |
| MergeInstanceRows | Boolean | Output Boolean that indicates whether the merge instance rows is enabled or not. |

## Version

Introduced in version 2022
