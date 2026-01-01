# Joint.isSuppressed Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Gets and sets if this joint is suppressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object. |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. boolean propertyValue = joint_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = joint_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |