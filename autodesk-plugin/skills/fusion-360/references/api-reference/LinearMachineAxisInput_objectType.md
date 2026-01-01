# LinearMachineAxisInput.objectType Property

Parent Object: [LinearMachineAxisInput](LinearMachineAxisInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object.  ```` ``` # Get the value of the property. propertyValue = linearMachineAxisInput_var.objectType ``` ```` |

"linearMachineAxisInput\_var" is a variable referencing a LinearMachineAxisInput object. ```` ``` #include <Cam/Machine/LinearMachineAxisInput.h>  // Get the value of the property. string propertyValue = linearMachineAxisInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |