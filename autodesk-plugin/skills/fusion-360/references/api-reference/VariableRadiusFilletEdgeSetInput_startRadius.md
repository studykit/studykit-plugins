# VariableRadiusFilletEdgeSetInput.startRadius Property

Parent Object: [VariableRadiusFilletEdgeSetInput](VariableRadiusFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VariableRadiusFilletEdgeSetInput.h>

## Description

Gets and sets a ValueInput object that defines the starting radius of the fillet. If a single edge is being filleted, the start radius is at the start end of the edge. If multiple tangent edges are being filleted the start radius is the start end of the first edge in the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"variableRadiusFilletEdgeSetInput\_var" is a variable referencing a VariableRadiusFilletEdgeSetInput object.  ```` ``` # Get the value of the property. propertyValue = variableRadiusFilletEdgeSetInput_var.startRadius  # Set the value of the property. variableRadiusFilletEdgeSetInput_var.startRadius = propertyValue ``` ```` |

"variableRadiusFilletEdgeSetInput\_var" is a variable referencing a VariableRadiusFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/VariableRadiusFilletEdgeSetInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = variableRadiusFilletEdgeSetInput_var->startRadius();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = variableRadiusFilletEdgeSetInput_var->startRadius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |