# MachinePart.children Property

Parent Object: [MachinePart](MachinePart.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePart.h>

## Description

Get the collection of child parts.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePart\_var" is a variable referencing a MachinePart object. |

"machinePart\_var" is a variable referencing a MachinePart object. ```` ``` #include <Cam/Machine/MachinePart.h>  // Get the value of the property. Ptr<MachineParts> propertyValue = machinePart_var->children(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineParts](MachineParts.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |