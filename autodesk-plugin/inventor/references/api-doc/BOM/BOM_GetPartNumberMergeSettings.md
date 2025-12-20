# BOM.GetPartNumberMergeSettings Method

Parent Object: [BOM](../BOM/BOM.md)

## Description

Method that gets the part number row merge settings for the BOM.

## Syntax

BOM.**GetPartNumberMergeSettings**( ***MergeEnabled*** As Boolean, ***MergeExcludeList***() As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MergeEnabled | Boolean | Boolean that indicates whether the row merging based on part number match is enabled. |
| MergeExcludeList | String | Array that returns the strings to exclude when merging based on part number match. This array will contain a minimum of one string (''). |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |