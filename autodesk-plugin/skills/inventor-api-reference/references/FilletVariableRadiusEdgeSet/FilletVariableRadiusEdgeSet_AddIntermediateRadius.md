# FilletVariableRadiusEdgeSet.AddIntermediateRadius Method

Parent Object: [FilletVariableRadiusEdgeSet](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet.md)

## Description

Method that creates a new FilletIntermediateRadius. The new FilletIntermediateRadius is returned. This method is used to define radii at intermediate points along an edge.

## Syntax

FilletVariableRadiusEdgeSet.**AddIntermediateRadius**( ***Edge*** As [Edge](../Edge/Edge.md), ***Radius*** As Variant, ***PercentLength*** As Variant ) As [FilletIntermediateRadius](../FilletIntermediateRadius/FilletIntermediateRadius.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edge | [Edge](../Edge/Edge.md) | Input object that the intermediate radius lies on. |
| Radius | Variant | Input Variant that defines the radius at the specified point. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |
| PercentLength | Variant | Input Variant that defines the position of the point along the edge as a percentage of the length of the edge. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. The units for input value need to be unitless and the value should be between 0 and 1. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature (Complex)](../../sample-programs/FilletFeature2_Sample.md) | This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge. |

## Version

Introduced in version 5.3
