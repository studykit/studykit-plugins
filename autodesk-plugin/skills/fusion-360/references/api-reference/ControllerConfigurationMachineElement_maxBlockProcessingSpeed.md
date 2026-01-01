# ControllerConfigurationMachineElement.maxBlockProcessingSpeed Property

Parent Object: [ControllerConfigurationMachineElement](ControllerConfigurationMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/ControllerConfigurationMachineElement.h>

## Description

Maximum block processing rate for the controller.

## Syntax

* [Python](#Python)
* [C++](#C++)

"controllerConfigurationMachineElement\_var" is a variable referencing a ControllerConfigurationMachineElement object. |

"controllerConfigurationMachineElement\_var" is a variable referencing a ControllerConfigurationMachineElement object. ```` ``` #include <Cam/Machine/ControllerConfigurationMachineElement.h>  // Get the value of the property. uinteger propertyValue = controllerConfigurationMachineElement_var->maxBlockProcessingSpeed();  // Set the value of the property, where value_var is a uinteger. bool returnValue = controllerConfigurationMachineElement_var->maxBlockProcessingSpeed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a uinteger.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |