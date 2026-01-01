# ControllerConfigurationMachineElement.maxNormalSpeed Property

Parent Object: [ControllerConfigurationMachineElement](ControllerConfigurationMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/ControllerConfigurationMachineElement.h>

## Description

Global maximum non-rapid linear motion speed. Units are cm/s.

## Syntax

* [Python](#Python)
* [C++](#C++)

"controllerConfigurationMachineElement\_var" is a variable referencing a ControllerConfigurationMachineElement object. |

"controllerConfigurationMachineElement\_var" is a variable referencing a ControllerConfigurationMachineElement object. ```` ``` #include <Cam/Machine/ControllerConfigurationMachineElement.h>  // Get the value of the property. double propertyValue = controllerConfigurationMachineElement_var->maxNormalSpeed();  // Set the value of the property, where value_var is a double. bool returnValue = controllerConfigurationMachineElement_var->maxNormalSpeed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |