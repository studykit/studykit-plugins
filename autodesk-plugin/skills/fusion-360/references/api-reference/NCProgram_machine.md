# NCProgram.machine Property

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Gets and sets the machine of this NC program. When a machine is set, "use machine configuration" is automatically set to true. If this machine has a default post assigned, this post will be set for the NC program as well.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a NCProgram object. |

"nCProgram\_var" is a variable referencing a NCProgram object. ```` ``` #include <Cam/NCProgram/NCProgram.h>  // Get the value of the property. Ptr<Machine> propertyValue = nCProgram_var->machine();  // Set the value of the property, where value_var is a Machine. bool returnValue = nCProgram_var->machine(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Machine](Machine.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |