# Milestones.isValid Property

Parent Object: [Milestones](Milestones.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestones.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"milestones\_var" is a variable referencing a Milestones object. |

"milestones\_var" is a variable referencing a Milestones object. ```` ``` #include <Core/Dashboard/Milestones.h>  // Get the value of the property. boolean propertyValue = milestones_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |