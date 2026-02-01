# VariableRadiusFilletEdgeSetInput.endRadius Property

Parent Object: [VariableRadiusFilletEdgeSetInput](VariableRadiusFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VariableRadiusFilletEdgeSetInput.h>

## Description

Gets and sets a ValueInput object that defines the ending radius of the fillet. If a single edge is being filleted, the end radius is at the end of the edge. If multiple tangent edges are being filleted the end radius is the open end of the last edge in the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"variableRadiusFilletEdgeSetInput\_var" is a variable referencing a VariableRadiusFilletEdgeSetInput object.  ```` ``` # Get the value of the property. propertyValue = variableRadiusFilletEdgeSetInput_var.endRadius  # Set the value of the property. variableRadiusFilletEdgeSetInput_var.endRadius = propertyValue ``` ```` |

"variableRadiusFilletEdgeSetInput\_var" is a variable referencing a VariableRadiusFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/VariableRadiusFilletEdgeSetInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = variableRadiusFilletEdgeSetInput_var->endRadius();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = variableRadiusFilletEdgeSetInput_var->endRadius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |