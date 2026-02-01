# LinearMachineAxis.name Property

Parent Object: [LinearMachineAxis](LinearMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxis.h>

## Description

The name of this axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. |

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. ```` ``` #include <Cam/Machine/LinearMachineAxis.h>  // Get the value of the property. string propertyValue = linearMachineAxis_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = linearMachineAxis_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |