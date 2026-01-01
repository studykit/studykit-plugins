# MachineLibrary.assetTypeName Property

Parent Object: [MachineLibrary](MachineLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineLibrary.h>

## Description

Get the name of the asset type which can be accessed by the library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineLibrary\_var" is a variable referencing a MachineLibrary object. |

"machineLibrary\_var" is a variable referencing a MachineLibrary object. ```` ``` #include <Cam/Machine/MachineLibrary.h>  // Get the value of the property. string propertyValue = machineLibrary_var->assetTypeName(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |