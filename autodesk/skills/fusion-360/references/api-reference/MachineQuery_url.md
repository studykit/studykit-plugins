# MachineQuery.url Property

Parent Object: [MachineQuery](MachineQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineQuery.h>

## Description

The URL specifies the location and folder to search for in the machine library. Setting the URL updates the location.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineQuery\_var" is a variable referencing a MachineQuery object. |

"machineQuery\_var" is a variable referencing a MachineQuery object. ```` ``` #include <Cam/Machine/MachineQuery.h>  // Get the value of the property. Ptr<URL> propertyValue = machineQuery_var->url();  // Set the value of the property, where value_var is a URL. bool returnValue = machineQuery_var->url(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [URL](URL.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |