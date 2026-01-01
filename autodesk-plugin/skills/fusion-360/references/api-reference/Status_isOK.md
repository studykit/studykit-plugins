# Status.isOK Property

Parent Object: [Status](Status.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Status.h>

## Description

If true, the operation was successful without any warnings or errors. This takes into account all of the child status messages.

## Syntax

* [Python](#Python)
* [C++](#C++)

"status\_var" is a variable referencing a Status object. |

"status\_var" is a variable referencing a Status object. ```` ``` #include <Core/Application/Status.h>  // Get the value of the property. boolean propertyValue = status_var->isOK(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |