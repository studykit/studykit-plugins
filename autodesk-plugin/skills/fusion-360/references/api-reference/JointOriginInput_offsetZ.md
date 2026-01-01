# JointOriginInput.offsetZ Property

Parent Object: [JointOriginInput](JointOriginInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginInput.h>

## Description

Gets and sets the value that defines the Z offset direction. This defaults to zero if it's not specified. The value defines a distance and if the ValueInput is defined using the createByReal method the value is assumed to be centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. |

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. ```` ``` #include <Fusion/Components/JointOriginInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = jointOriginInput_var->offsetZ();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = jointOriginInput_var->offsetZ(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |