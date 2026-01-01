# DistanceAndAngleChamferEdgeSet.isTangentChain Property

Parent Object: [DistanceAndAngleChamferEdgeSet](DistanceAndAngleChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>

## Description

Gets and sets the Tangent chain for chamfer. This enables tangent chain option for chamfer.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object. |

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object. ```` ``` #include <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>  // Get the value of the property. boolean propertyValue = distanceAndAngleChamferEdgeSet_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = distanceAndAngleChamferEdgeSet_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |