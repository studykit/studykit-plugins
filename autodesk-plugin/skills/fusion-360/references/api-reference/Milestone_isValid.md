# Milestone.isValid Property

Parent Object: [Milestone](Milestone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestone.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"milestone\_var" is a variable referencing a Milestone object. |

"milestone\_var" is a variable referencing a Milestone object. ```` ``` #include <Core/Dashboard/Milestone.h>  // Get the value of the property. boolean propertyValue = milestone_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |