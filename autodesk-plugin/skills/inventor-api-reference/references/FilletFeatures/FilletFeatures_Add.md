# FilletFeatures.Add Method

Parent Object: [FilletFeatures](../FilletFeatures/FilletFeatures.md)

## Description

Method that creates a new FilletFeature. This method may be used to create fillet features of constant radius, variable radius or a combination of constant and variable radius. Setbacks may also be specified. The new FilletFeature is returned.

## Syntax

FilletFeatures.**Add**( ***FilletDefinition*** As [FilletDefinition](../FilletDefinition/FilletDefinition.md), [***AutomaticEdgeChain***] As Boolean, [***SmoothRadiusTransition***] As Boolean, [***RollAlongSharpEdges***] As Boolean, [***RollingBallWherePossible***] As Boolean, [***PreserveAllFeatures***] As Boolean ) As [FilletFeature](../FilletFeature/FilletFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FilletDefinition | [FilletDefinition](../FilletDefinition/FilletDefinition.md) | Input object that defines the input definition for the fillet feature. The object defines the edges, radii, and setbacks. |
| AutomaticEdgeChain | Boolean | Optional input Boolean that defines if automatic edge chaining along tangentially connected edges should be performed. The default is True. |
| SmoothRadiusTransition | Boolean | Optional input Boolean that applies only to variable radius fillets and defines whether the transition between different radii is to be smooth. For a smooth transition there is a gradual blending transition between the defined radius points and the transitions are tangent. Without a smooth transition, a linear transition is used between radius points. The default is True for a smooth transition.   This is an optional argument whose default value is True. |
| RollAlongSharpEdges | Boolean | Optional input Boolean that sets the solution method for fillets when the specified radius would cause adjacent faces to be extended. When True, the radius will be varied when necessary to preserve the edges of adjacent faces. When False, a constant radius will be maintained and adjacent faces extended as needed. The default is False.   This is an optional argument whose default value is False. |
| RollingBallWherePossible | Boolean | Optional input Boolean that sets the corner style for the fillet. When True, the fillet will be defined as if a ball had been rolled along the edge and around the corners. When False, a continuous tangent transition between fillets in sharp corners is created. The default is True.   This is an optional argument whose default value is True. |
| PreserveAllFeatures | Boolean | Optional input Boolean that specifies if all features that intersect with the fillet are checked and their intersections calculated during the fillet operation. If False, only the edges that are part of the fillet operation are calculated during the operation. The default is False.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature (Complex)](../../sample-programs/FilletFeature2_Sample.md) | This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge. |

## Version

Introduced in version 5.3
