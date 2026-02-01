# VariableRadiusFilletEdgeSetInput.tangencyWeight Property

Parent Object: [VariableRadiusFilletEdgeSetInput](VariableRadiusFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VariableRadiusFilletEdgeSetInput.h>

## Description

Gets and sets the tangency weight for the given edge set. The tangency weight controls the influence of the continuity (G1 or G2) on the fillet. The ValueInput must be a real value between 0.1 and 2.0 inclusive, with no units. The default value is 1.0.

## Syntax

* [Python](#Python)
* [C++](#C++)

"variableRadiusFilletEdgeSetInput\_var" is a variable referencing a VariableRadiusFilletEdgeSetInput object. |

"variableRadiusFilletEdgeSetInput\_var" is a variable referencing a VariableRadiusFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/VariableRadiusFilletEdgeSetInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = variableRadiusFilletEdgeSetInput_var->tangencyWeight();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = variableRadiusFilletEdgeSetInput_var->tangencyWeight(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |