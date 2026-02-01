# FilletEdgeSets.addConstantRadiusEdgeSet Method

Parent Object: [FilletEdgeSets](FilletEdgeSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSets.h>

## Description

Adds a set of edges with a constant radius to this fillet feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSets\_var" is a variable referencing a [FilletEdgeSets](FilletEdgeSets.htm) object.```` ``` returnValue = filletEdgeSets_var.addConstantRadiusEdgeSet(entities, radius, isTangentChain) ``` ```` |

"filletEdgeSets\_var" is a variable referencing a [FilletEdgeSets](FilletEdgeSets.htm) object.  ```` ``` #include <Fusion/Features/FilletEdgeSets.h>  returnValue = filletEdgeSets_var->addConstantRadiusEdgeSet(entities, radius, isTangentChain); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstantRadiusFilletEdgeSet](ConstantRadiusFilletEdgeSet.htm) | Returns the newly created FilletEdgeSet. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entities | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing the BRepEdge, BRepFace, and Feature objects to be filleted. If the isTangentChain argument is true additional edges or faces may also get filleted if they are tangentially connected to any of the input edges or faces. |
| radius | [ValueInput](ValueInput.htm) | A ValueInput object that defines the radius of the fillet. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length. |
| isTangentChain | boolean | A boolean value for setting whether or not edges that are tangentially connected to the input edges (if any) will also be filleted. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |