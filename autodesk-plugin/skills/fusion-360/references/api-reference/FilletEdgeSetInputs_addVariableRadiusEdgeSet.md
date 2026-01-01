# FilletEdgeSetInputs.addVariableRadiusEdgeSet Method

Parent Object: [FilletEdgeSetInputs](FilletEdgeSetInputs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSetInputs.h>

## Description

Adds a single edge or set of tangent edges to the fillet feature input. Some settings are initialized with a default value and can be set by modifying properties on the returned VariableRadiusFilletEdgeSetInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSetInputs\_var" is a variable referencing a [FilletEdgeSetInputs](FilletEdgeSetInputs.htm) object.```` ``` returnValue = filletEdgeSetInputs_var.addVariableRadiusEdgeSet(tangentEdges, startRadius, endRadius, isTangentChain) ``` ```` |

"filletEdgeSetInputs\_var" is a variable referencing a [FilletEdgeSetInputs](FilletEdgeSetInputs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [VariableRadiusFilletEdgeSetInput](VariableRadiusFilletEdgeSetInput.htm) | Returns the newly created VariableRadiusFilletEdgeSetInput. This object provides access to additional settings. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tangentEdges | [ObjectCollection](ObjectCollection.htm) | An object collection containing a single edge or multiple edges. Multiple edges must be tangentially connected and added to the collection in their connected order. If a single edge is input, you can use the isTangentChain argument to automatically find any tangentially connected edges. |
| startRadius | [ValueInput](ValueInput.htm) | A ValueInput object that defines the starting radius of the fillet. If a single edge is being filleted, the start radius is at the start end of the edge. If multiple tangent edges are being filleted the start radius is the start end of the first edge in the collection.   If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length. |
| endRadius | [ValueInput](ValueInput.htm) | A ValueInput object that defines the ending radius of the fillet. If a single edge is being filleted, the end radius is at the end of the edge. If multiple tangent edges are being filleted the end radius is the open end of the last edge in the collection.   If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length. |
| isTangentChain | boolean | A boolean value for setting whether or not edges that are tangentially connected to the single input edge will also be filleted. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature API Sample](FilletFeatureSample_Sample.htm) | Demonstrates creating fillets using the various types of fillets. Create a new design and add a box that is at least 2 cm on each side. The script creates a constant radius, variable radius and chord length fillets. After creating each one, it deletes it and then creates the next. To see any of the fillets that were deleted, undo to get the fillet back. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |