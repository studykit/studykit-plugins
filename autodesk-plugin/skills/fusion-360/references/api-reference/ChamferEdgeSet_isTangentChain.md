# ChamferEdgeSet.isTangentChain Property

Parent Object: [ChamferEdgeSet](ChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferEdgeSet.h>

## Description

Gets and sets the Tangent chain for chamfer. This enables tangent chain option for chamfer.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferEdgeSet\_var" is a variable referencing a ChamferEdgeSet object. |

"chamferEdgeSet\_var" is a variable referencing a ChamferEdgeSet object. ```` ``` #include <Fusion/Features/ChamferEdgeSet.h>  // Get the value of the property. boolean propertyValue = chamferEdgeSet_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = chamferEdgeSet_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |