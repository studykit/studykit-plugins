# MachineFromTemplateInput.objectType Property

Parent Object: [MachineFromTemplateInput](MachineFromTemplateInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineFromTemplateInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineFromTemplateInput\_var" is a variable referencing a MachineFromTemplateInput object.  ```` ``` # Get the value of the property. propertyValue = machineFromTemplateInput_var.objectType ``` ```` |

"machineFromTemplateInput\_var" is a variable referencing a MachineFromTemplateInput object. ```` ``` #include <Cam/Machine/MachineFromTemplateInput.h>  // Get the value of the property. string propertyValue = machineFromTemplateInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |