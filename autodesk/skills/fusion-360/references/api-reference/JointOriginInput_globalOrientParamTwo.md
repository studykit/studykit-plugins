# JointOriginInput.globalOrientParamTwo Property

Parent Object: [JointOriginInput](JointOriginInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginInput.h>

## Description

Gets and sets the value that defines the second global orient parameter for the joint origin. This defaults to zero if it's not specified. For Cylinder or cone, it is not used. For Sphere, it represents the polar angle, which is the angle between the radius line and the equator plane. For Torus, it represents the angle around the center of the section circle. For Spline, it represents the V parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. |

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. ```` ``` #include <Fusion/Components/JointOriginInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = jointOriginInput_var->globalOrientParamTwo();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = jointOriginInput_var->globalOrientParamTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |