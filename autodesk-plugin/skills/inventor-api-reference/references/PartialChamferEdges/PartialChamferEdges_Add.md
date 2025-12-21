# PartialChamferEdges.Add Method

Parent Object: [PartialChamferEdges](../PartialChamferEdges/PartialChamferEdges.md)

## Description

Adds an item to the collection.

## Syntax

PartialChamferEdges.**Add**( ***Edge*** As Object, ***Start*** As Variant, ***End*** As Variant ) As [PartialChamferEdge](../PartialChamferEdge/PartialChamferEdge.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edge | Object | Input Edge or EdgeCollection object that specifies the which Edge or Edge chain to be partially chamfered. If the AutomaticEdgeChain is True and an Edge is input the Edge chain will be used if there is an Edge chain connected with the Edge. |
| Start | Variant | Input value that specifies the start of the Edge or Edge chain to be partially chamfered. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |
| End | Variant | Input value that specifies the end of the Edge or Edge chain to be partially chamfered. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Partial Chamfer Sample](../../sample-programs/PartialChamferSample_Sample.md) | This sample demonstrates how to edit a chamfer feature to set the partial chamfer on a chamfered edge. |

## Version

Introduced in version 2018
