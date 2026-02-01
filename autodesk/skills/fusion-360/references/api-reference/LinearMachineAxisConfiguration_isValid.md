# LinearMachineAxisConfiguration.isValid Property

Parent Object: [LinearMachineAxisConfiguration](LinearMachineAxisConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisConfiguration.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisConfiguration\_var" is a variable referencing a LinearMachineAxisConfiguration object. |

"linearMachineAxisConfiguration\_var" is a variable referencing a LinearMachineAxisConfiguration object. ```` ``` #include <Cam/Machine/LinearMachineAxisConfiguration.h>  // Get the value of the property. boolean propertyValue = linearMachineAxisConfiguration_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |