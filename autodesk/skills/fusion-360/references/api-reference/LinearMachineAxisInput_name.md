# LinearMachineAxisInput.name Property

Parent Object: [LinearMachineAxisInput](LinearMachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisInput.h>

## Description

The user facing name of this axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. |

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. ```` ``` #include <Cam/Machine/LinearMachineAxisInput.h>  // Get the value of the property. string propertyValue = linearMachineAxisInput_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = linearMachineAxisInput_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |