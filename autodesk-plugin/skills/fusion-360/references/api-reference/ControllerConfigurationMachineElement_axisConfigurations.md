# ControllerConfigurationMachineElement.axisConfigurations Property

Parent Object: [ControllerConfigurationMachineElement](ControllerConfigurationMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/ControllerConfigurationMachineElement.h>

## Description

Gets the collection of axis configuration objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"controllerConfigurationMachineElement\_var" is a variable referencing a ControllerConfigurationMachineElement object. |

"controllerConfigurationMachineElement\_var" is a variable referencing a ControllerConfigurationMachineElement object. ```` ``` #include <Cam/Machine/ControllerConfigurationMachineElement.h>  // Get the value of the property. Ptr<MachineAxisConfigurations> propertyValue = controllerConfigurationMachineElement_var->axisConfigurations(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineAxisConfigurations](MachineAxisConfigurations.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |