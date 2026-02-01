# LinearMachineAxisInput.homePosition Property

Parent Object: [LinearMachineAxisInput](LinearMachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisInput.h>

## Description

Specifies the value that this axis returns to when the machine is homed. Units are cm for linear axes or radians for rotary axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. |

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. ```` ``` #include <Cam/Machine/LinearMachineAxisInput.h>  // Get the value of the property. double propertyValue = linearMachineAxisInput_var->homePosition();  // Set the value of the property, where value_var is a double. bool returnValue = linearMachineAxisInput_var->homePosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |