# ControllerConfigurationMachineElement.objectType Property

Parent Object: [ControllerConfigurationMachineElement](ControllerConfigurationMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/ControllerConfigurationMachineElement.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"controllerConfigurationMachineElement\_var" is a variable referencing a ControllerConfigurationMachineElement object.  ```` ``` # Get the value of the property. propertyValue = controllerConfigurationMachineElement_var.objectType ``` ```` |

"controllerConfigurationMachineElement\_var" is a variable referencing a ControllerConfigurationMachineElement object. ```` ``` #include <Cam/Machine/ControllerConfigurationMachineElement.h>  // Get the value of the property. string propertyValue = controllerConfigurationMachineElement_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |