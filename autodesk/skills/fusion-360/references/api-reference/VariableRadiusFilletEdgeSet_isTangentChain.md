# VariableRadiusFilletEdgeSet.isTangentChain Property

Parent Object: [VariableRadiusFilletEdgeSet](VariableRadiusFilletEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VariableRadiusFilletEdgeSet.h>

## Description

Gets and sets the Tangent chain for fillet. This enables tangent chain option for fillet.

## Syntax

* [Python](#Python)
* [C++](#C++)

"variableRadiusFilletEdgeSet\_var" is a variable referencing a VariableRadiusFilletEdgeSet object. |

"variableRadiusFilletEdgeSet\_var" is a variable referencing a VariableRadiusFilletEdgeSet object. ```` ``` #include <Fusion/Features/VariableRadiusFilletEdgeSet.h>  // Get the value of the property. boolean propertyValue = variableRadiusFilletEdgeSet_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = variableRadiusFilletEdgeSet_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |