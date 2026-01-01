# FilletEdgeSets.addVariableRadiusEdgeSet Method

Parent Object: [FilletEdgeSets](FilletEdgeSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSets.h>

## Description

Adds a single edge or set of tangent edges along with variable radius information to this fillet feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSets\_var" is a variable referencing a [FilletEdgeSets](FilletEdgeSets.htm) object.```` ``` returnValue = filletEdgeSets_var.addVariableRadiusEdgeSet(tangentEdges, startRadius, endRadius, positions, radii, isTangentChain) ``` ```` |

"filletEdgeSets\_var" is a variable referencing a [FilletEdgeSets](FilletEdgeSets.htm) object.  ```` ``` #include <Fusion/Features/FilletEdgeSets.h>  returnValue = filletEdgeSets_var->addVariableRadiusEdgeSet(tangentEdges, startRadius, endRadius, positions, radii, isTangentChain); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [VariableRadiusFilletEdgeSet](VariableRadiusFilletEdgeSet.htm) | Returns the newly created FilletEdgeSet. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tangentEdges | [ObjectCollection](ObjectCollection.htm) | An object collection containing a single edge or multiple edges. Multiple edges must be tangentially connected and added to the collection in their connected order. If a single edge is input, you can use the isTangentChain argument to automatically find any tangentially connected edges. |
| startRadius | [ValueInput](ValueInput.htm) | A ValueInput object that defines the starting radius of the fillet. If a single edge is being filleted, the start radius is at the start end of the edge. If multiple tangent edges are being filleted the start radius is the open end of the first edge in the collection.   If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length. |
| endRadius | [ValueInput](ValueInput.htm) | A ValueInput object that defines the ending radius of the fillet. If a single edge is being filleted, the end radius is at the end of the edge. If multiple tangent edges are being filleted the end radius is the open end of the last edge in the collection. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length. |
| positions | ValueInput[] | An array of ValueInput objects that defines the positions of any additional radii along the edge(s). The value must be between 0 and 1 and defines the percentage along the curve where a radius is defined. The value is unitless. This array must have the same number of values as the array passed in for the radii argument. |
| radii | ValueInput[] | An array of ValueInput objects that define the radii at positions along the edge(s). This array must have the same number of values as the array passed in for the positions argument. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it will be interpreted using the current default units for length. |
| isTangentChain | boolean | A boolean value for setting whether or not edges that are tangentially connected to the single input edge will also be filleted. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |