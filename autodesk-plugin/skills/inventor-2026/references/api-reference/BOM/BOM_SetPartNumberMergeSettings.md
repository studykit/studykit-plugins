# BOM.SetPartNumberMergeSettings Method

Parent Object: [BOM](../BOM/BOM.md)

## Description

Method that sets the part number row merge settings for the BOM.

## Syntax

BOM.**SetPartNumberMergeSettings**( ***MergeEnabled*** As Boolean, [***MergeKeys***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MergeEnabled | Boolean | Boolean that indicates whether the row merging based on part number match is enabled. |
| MergeKeys | Variant | Optional input array that contains the strings to exclude when merging based on part number match. If supplied, this array should contain a minimum of one string (''). |

## Version

Introduced in version 11
