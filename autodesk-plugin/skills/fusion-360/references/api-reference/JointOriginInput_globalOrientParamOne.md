# JointOriginInput.globalOrientParamOne Property

Parent Object: [JointOriginInput](JointOriginInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginInput.h>

## Description

Gets and sets the value that defines the first global orient parameter for the joint origin. This defaults to zero if it's not specified. For Cylineder or cone, it represents the angle around the center axis. For Sphere and Torus, it represents the angle around the center axis. For Spline, it represents the U parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. |

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. ```` ``` #include <Fusion/Components/JointOriginInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = jointOriginInput_var->globalOrientParamOne();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = jointOriginInput_var->globalOrientParamOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |