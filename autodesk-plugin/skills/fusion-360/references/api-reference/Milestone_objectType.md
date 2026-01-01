# Milestone.objectType Property

Parent Object: [Milestone](Milestone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestone.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"milestone\_var" is a variable referencing a Milestone object.  ```` ``` # Get the value of the property. propertyValue = milestone_var.objectType ``` ```` |

"milestone\_var" is a variable referencing a Milestone object. ```` ``` #include <Core/Dashboard/Milestone.h>  // Get the value of the property. string propertyValue = milestone_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |