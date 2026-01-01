# EqualDistanceChamferEdgeSet.isTangentChain Property

Parent Object: [EqualDistanceChamferEdgeSet](EqualDistanceChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EqualDistanceChamferEdgeSet.h>

## Description

Gets and sets the Tangent chain for chamfer. This enables tangent chain option for chamfer.

## Syntax

* [Python](#Python)
* [C++](#C++)

"equalDistanceChamferEdgeSet\_var" is a variable referencing an EqualDistanceChamferEdgeSet object. |

"equalDistanceChamferEdgeSet\_var" is a variable referencing an EqualDistanceChamferEdgeSet object. ```` ``` #include <Fusion/Features/EqualDistanceChamferEdgeSet.h>  // Get the value of the property. boolean propertyValue = equalDistanceChamferEdgeSet_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = equalDistanceChamferEdgeSet_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |