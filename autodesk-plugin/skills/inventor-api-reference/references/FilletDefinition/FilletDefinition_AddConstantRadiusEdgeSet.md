# FilletDefinition.AddConstantRadiusEdgeSet Method

Parent Object: [FilletDefinition](../FilletDefinition/FilletDefinition.md)

## Description

Method that creates a new constant radius edge set. The new FilletDefinition is returned.

## Syntax

FilletDefinition.**AddConstantRadiusEdgeSet**( ***Edges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***ConstantRadius*** As Variant ) As [FilletConstantRadiusEdgeSet](../FilletConstantRadiusEdgeSet/FilletConstantRadiusEdgeSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input object that contains edges for the fillet feature. |
| ConstantRadius | Variant | Input Variant that defines the radius of the fillet. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature (Complex)](../../sample-programs/FilletFeature2_Sample.md) | This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge. |

## Version

Introduced in version 5.3
