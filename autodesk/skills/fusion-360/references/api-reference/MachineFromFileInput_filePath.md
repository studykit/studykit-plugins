# MachineFromFileInput.filePath Property

Parent Object: [MachineFromFileInput](MachineFromFileInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineFromFileInput.h>

## Description

The path to a file to act as a base for creating a machine from. The filePath is expected to be an absolute path to the local machine file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineFromFileInput\_var" is a variable referencing a MachineFromFileInput object. |

"machineFromFileInput\_var" is a variable referencing a MachineFromFileInput object. ```` ``` #include <Cam/Machine/MachineFromFileInput.h>  // Get the value of the property. string propertyValue = machineFromFileInput_var->filePath(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |