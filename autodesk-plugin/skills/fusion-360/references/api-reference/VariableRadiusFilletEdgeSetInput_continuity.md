# VariableRadiusFilletEdgeSetInput.continuity Property

Parent Object: [VariableRadiusFilletEdgeSetInput](VariableRadiusFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VariableRadiusFilletEdgeSetInput.h>

## Description

Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType. The default is TangentSurfaceContinuityType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"variableRadiusFilletEdgeSetInput\_var" is a variable referencing a VariableRadiusFilletEdgeSetInput object. |

"variableRadiusFilletEdgeSetInput\_var" is a variable referencing a VariableRadiusFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/VariableRadiusFilletEdgeSetInput.h>  // Get the value of the property. SurfaceContinuityTypes propertyValue = variableRadiusFilletEdgeSetInput_var->continuity();  // Set the value of the property, where value_var is a SurfaceContinuityTypes. bool returnValue = variableRadiusFilletEdgeSetInput_var->continuity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceContinuityTypes](SurfaceContinuityTypes.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |