# Machine.description Property

Parent Object: [Machine](Machine.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/Machine.h>

## Description

Gets and sets the description of the machine.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machine\_var" is a variable referencing a Machine object. |

"machine\_var" is a variable referencing a Machine object. ```` ``` #include <Cam/Machine/Machine.h>  // Get the value of the property. string propertyValue = machine_var->description();  // Set the value of the property, where value_var is a string. bool returnValue = machine_var->description(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |