# MachinePart.parent Property

Parent Object: [MachinePart](MachinePart.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePart.h>

## Description

Get or set the parent of this part. Returns null if this part is a root part. Setting the parent will add this part to the end of the parent's children collection. Setting the parent will throw an error if the new parent is this part or a child of this part.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePart\_var" is a variable referencing a MachinePart object. |

"machinePart\_var" is a variable referencing a MachinePart object. ```` ``` #include <Cam/Machine/MachinePart.h>  // Get the value of the property. Ptr<MachinePart> propertyValue = machinePart_var->parent();  // Set the value of the property, where value_var is a MachinePart. bool returnValue = machinePart_var->parent(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MachinePart](MachinePart.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |