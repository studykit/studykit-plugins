# BOM.SetPartNumberMergeSettings2 Method

Parent Object: [BOM](../BOM/BOM.md)

## Description

Sets the part number row merge settings for the BOM.

## Syntax

BOM.**SetPartNumberMergeSettings2**( ***MergeEnabled*** As Boolean, [***MergeKeys***] As Variant, [***MergeInstanceRows***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MergeEnabled | Boolean | Input Boolean that indicates whether the row merging based on part number match is enabled. |
| MergeKeys | Variant | Optional input array that contains the strings to exclude when merging based on part number match. If supplied, this array should contain a minimum of one string (“”). |
| MergeInstanceRows | Variant | Output Boolean that indicates whether the merge instance rows is enabled or not.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |