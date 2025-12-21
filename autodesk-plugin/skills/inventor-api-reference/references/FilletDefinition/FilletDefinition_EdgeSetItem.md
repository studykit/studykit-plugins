# FilletDefinition.EdgeSetItem Property

Parent Object: [FilletDefinition](../FilletDefinition/FilletDefinition.md)

## Description

Method that returns the specified FilletRadiusEdgeSet object from the collection. This will return either a FilletConstantRadiusEdgeSet or FilletVariableRadiusEdgeSet object.

## Syntax

FilletDefinition.**EdgeSetItem**( ***Index*** As Long ) As [FilletRadiusEdgeSet](../FilletRadiusEdgeSet/FilletRadiusEdgeSet.md)

## Property Value

This is a read only property whose value is a [FilletRadiusEdgeSet](../FilletRadiusEdgeSet/FilletRadiusEdgeSet.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the index of the to return from the definition. If an out of range index is provided, an error occurs. |

## Version

Introduced in version 5.3
