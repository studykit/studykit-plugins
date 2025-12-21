# DerivedAssemblyDefinition.GetRemoveBySizeOptions Method

Parent Object: [DerivedAssemblyDefinition](../DerivedAssemblyDefinition/DerivedAssemblyDefinition.md)

## Description

Method that returns the simplification options specifying geometry to remove based on size.

## Syntax

DerivedAssemblyDefinition.**GetRemoveBySizeOptions**( ***Enable*** As Boolean, ***SizeRatioPercentage*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Enable | Boolean | Output Boolean that specifies whether to enable or disable the 'remove by size' simplification option. |
| SizeRatioPercentage | Long | Output Long that specifies the size ratio percentage value of parts/faces to be removed. Valid range is 0 to 100. The ratio indicates the difference between the part bounding box and the assembly bounding box. This value returns 1 and should be ignored if the Enable argument is returns False. |

## Version

Introduced in version 2011
