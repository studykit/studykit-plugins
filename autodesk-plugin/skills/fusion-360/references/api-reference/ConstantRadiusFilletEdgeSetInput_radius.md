# ConstantRadiusFilletEdgeSetInput.radius Property

Parent Object: [ConstantRadiusFilletEdgeSetInput](ConstantRadiusFilletEdgeSetInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ConstantRadiusFilletEdgeSetInput.h>

## Description

Gets and sets ValueInput object that defines the radius of the fillet. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constantRadiusFilletEdgeSetInput\_var" is a variable referencing a ConstantRadiusFilletEdgeSetInput object. |

"constantRadiusFilletEdgeSetInput\_var" is a variable referencing a ConstantRadiusFilletEdgeSetInput object. ```` ``` #include <Fusion/Features/ConstantRadiusFilletEdgeSetInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = constantRadiusFilletEdgeSetInput_var->radius();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = constantRadiusFilletEdgeSetInput_var->radius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |