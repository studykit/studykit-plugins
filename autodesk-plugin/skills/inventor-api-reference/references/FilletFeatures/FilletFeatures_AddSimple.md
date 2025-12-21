# FilletFeatures.AddSimple Method

Parent Object: [FilletFeatures](../FilletFeatures/FilletFeatures.md)

## Description

Method that creates a new constant radius fillet where all fillets have the same radius. For more complex fillet features, the Add method of the FilletFeatures collection can be used.

## Syntax

FilletFeatures.**AddSimple**( ***Edges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***Radius*** As Variant, [***AllFillets***] As Boolean, [***AllRounds***] As Boolean, [***AutomaticEdgeChain***] As Boolean, [***RollAlongSharpEdges***] As Boolean, [***RollingBallWherePossible***] As Boolean, [***PreserveAllFeatures***] As Boolean ) As [FilletFeature](../FilletFeature/FilletFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input object that contains the edges to be filleted. |
| Radius | Variant | Input Variant that defines the radius of the fillet. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |
| AllFillets | Boolean | Optional input Boolean that specifies if all concave edges of the body are to be considered part of this edge set. True indicates all concave edges will be filleted. The default is False. |
| AllRounds | Boolean | Optional input Boolean that specifies if all convex edges of the body are to be considered part of this edge set. True indicates all convex edges will be filleted. The default is False.   This is an optional argument whose default value is False. |
| AutomaticEdgeChain | Boolean | Optional input Boolean that defines if automatic edge chaining along tangentially connected edges should be performed. The default is True.   This is an optional argument whose default value is True. |
| RollAlongSharpEdges | Boolean | Optional input Boolean that sets the solution method for fillets when the specified radius would cause adjacent faces to be extended. When True, the radius will be varied when necessary to preserve the edges of adjacent faces. When False, a constant radius will be maintained and adjacent faces extended as needed. The default is False.   This is an optional argument whose default value is False. |
| RollingBallWherePossible | Boolean | Optional input Boolean that sets the corner style for the fillet. When True, the fillet will be defined as if a ball had been rolled along the edge and around the corners. When False, a continuous tangent transition between fillets in sharp corners is created. The default is True.   This is an optional argument whose default value is True. |
| PreserveAllFeatures | Boolean | Optional input Boolean that specifies if all features that intersect with the fillet are checked and their intersections calculated during the fillet operation. If False, only the edges that are part of the fillet operation are calculated during the operation. The default is False.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature (All Rounds)](../../sample-programs/FilletFeature_Sample.md) | This sample demonstrates rounding all of the edges of a part. |
| [Fillet Feature (Simple)](../../sample-programs/FilletFeature3_Sample.md) | This sample demonstrates using the AddSimple method of the FilletFeatures collection to create a constant radius fillet. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |