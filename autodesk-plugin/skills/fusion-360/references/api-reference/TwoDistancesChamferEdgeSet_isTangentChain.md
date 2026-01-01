# TwoDistancesChamferEdgeSet.isTangentChain Property

Parent Object: [TwoDistancesChamferEdgeSet](TwoDistancesChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoDistancesChamferEdgeSet.h>

## Description

Gets and sets the Tangent chain for chamfer. This enables tangent chain option for chamfer.

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoDistancesChamferEdgeSet\_var" is a variable referencing a TwoDistancesChamferEdgeSet object. |

"twoDistancesChamferEdgeSet\_var" is a variable referencing a TwoDistancesChamferEdgeSet object. ```` ``` #include <Fusion/Features/TwoDistancesChamferEdgeSet.h>  // Get the value of the property. boolean propertyValue = twoDistancesChamferEdgeSet_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = twoDistancesChamferEdgeSet_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |