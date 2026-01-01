# Milestone.name Property

Parent Object: [Milestone](Milestone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestone.h>

## Description

Gets and sets the name of the milestone.

## Syntax

* [Python](#Python)
* [C++](#C++)

"milestone\_var" is a variable referencing a Milestone object. |

"milestone\_var" is a variable referencing a Milestone object. ```` ``` #include <Core/Dashboard/Milestone.h>  // Get the value of the property. string propertyValue = milestone_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = milestone_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |