# WorkPoints.AddByMidPoint Method

Parent Object: [WorkPoints](../WorkPoints/WorkPoints.md)

## Description

Method that creates a new work point at the midpoint of the input edge. This method is not currently supported when creating a work point within an assembly.

## Syntax

WorkPoints.**AddByMidPoint**( ***Edge*** As [Edge](../Edge/Edge.md), [***Construction***] As Boolean ) As [WorkPoint](../WorkPoint/WorkPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edge | [Edge](../Edge/Edge.md) | Input Edge object. Any open edge is valid as input. Inputting a closed edge, (i.e. circle), will cause and error to occur. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work point as a construction point or not. The default is False, which indicates to create a standard work point. A construction work point is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 4
