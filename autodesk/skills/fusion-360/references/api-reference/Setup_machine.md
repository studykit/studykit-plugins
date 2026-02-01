# Setup.machine Property

Parent Object: [Setup](Setup.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Gets and sets the Machine associated with the setup. The returned Machine is a transient copy, so the Machine needs to be set to the Setup again to apply any changes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a Setup object. |

"setup\_var" is a variable referencing a Setup object. ```` ``` #include <Cam/CAM/Setup.h>  // Get the value of the property. Ptr<Machine> propertyValue = setup_var->machine();  // Set the value of the property, where value_var is a Machine. bool returnValue = setup_var->machine(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Machine](Machine.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |