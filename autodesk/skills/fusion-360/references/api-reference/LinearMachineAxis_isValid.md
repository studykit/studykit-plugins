# LinearMachineAxis.isValid Property

Parent Object: [LinearMachineAxis](LinearMachineAxis.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxis.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. |

"linearMachineAxis\_var" is a variable referencing a LinearMachineAxis object. ```` ``` #include <Cam/Machine/LinearMachineAxis.h>  // Get the value of the property. boolean propertyValue = linearMachineAxis_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |