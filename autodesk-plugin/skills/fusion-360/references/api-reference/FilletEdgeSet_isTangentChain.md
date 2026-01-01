# FilletEdgeSet.isTangentChain Property

Parent Object: [FilletEdgeSet](FilletEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSet.h>

## Description

Gets and sets the Tangent chain for fillet. This enables tangent chain option for fillet.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSet\_var" is a variable referencing a FilletEdgeSet object. |

"filletEdgeSet\_var" is a variable referencing a FilletEdgeSet object. ```` ``` #include <Fusion/Features/FilletEdgeSet.h>  // Get the value of the property. boolean propertyValue = filletEdgeSet_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = filletEdgeSet_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |