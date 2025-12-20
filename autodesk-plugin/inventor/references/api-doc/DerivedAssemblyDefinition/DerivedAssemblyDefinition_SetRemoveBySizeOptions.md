# DerivedAssemblyDefinition.SetRemoveBySizeOptions Method

Parent Object: [DerivedAssemblyDefinition](../DerivedAssemblyDefinition/DerivedAssemblyDefinition.md)

## Description

Method that sets the simplification options specifying geometry to remove based on size.

## Syntax

DerivedAssemblyDefinition.**SetRemoveBySizeOptions**( ***Enable*** As Boolean, [***SizeRatioPercentage***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Enable | Boolean | Input Boolean that specifies whether to enable or disable the 'remove by size' simplification option. |
| SizeRatioPercentage | Long | Optional input Long that specifies the size ratio percentage value of parts/faces to be removed. Valid range is 0 to 100. The ratio indicates the difference between the part bounding box and the assembly bounding box. This input is required if the Enable argument is specified to be True. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |