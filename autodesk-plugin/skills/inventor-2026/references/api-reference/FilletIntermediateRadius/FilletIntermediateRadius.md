# FilletIntermediateRadius Object

## Description

The FilletIntermediateRadius object represents the information needed to define the radius at a point along an edge for a variable radius fillet.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Edge](../FilletIntermediateRadius/FilletIntermediateRadius_Edge.md) | Property that returns the associated with the PercentLength value. This property is only available when a FilletDefinition object is being defined to use as input for creating a fillet. When the parent FilletDefinition object is obtained from an existing Fillet, the end-of-part marker should be placed above this fillet feature to allow access this property. |
| [PercentLength](../FilletIntermediateRadius/FilletIntermediateRadius_PercentLength.md) | Property that returns the parameter that controls the position of the point along the edge. The value defines it's position as a percentage of the entire length. This property will return Nothing if the fillet feature has not been created yet. |
| [Radius](../FilletIntermediateRadius/FilletIntermediateRadius_Radius.md) | Property that returns the parameter that controls the radius of the fillet at the defined point. This property will return Nothing if the fillet feature has not been created yet. |

## Accessed From

[FilletVariableRadiusEdgeSet.AddIntermediateRadius](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_AddIntermediateRadius.md), [FilletVariableRadiusEdgeSet.IntermediateRadiusItem](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet_IntermediateRadiusItem.md)

## Version

Introduced in version 5.3
