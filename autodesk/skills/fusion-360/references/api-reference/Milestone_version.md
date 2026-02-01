# Milestone.version Property

Parent Object: [Milestone](Milestone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Milestone.h>

## Description

Returns the file version associated with this milestone.

## Syntax

* [Python](#Python)
* [C++](#C++)

"milestone\_var" is a variable referencing a Milestone object. |

"milestone\_var" is a variable referencing a Milestone object. ```` ``` #include <Core/Dashboard/Milestone.h>  // Get the value of the property. Ptr<DataFile> propertyValue = milestone_var->version(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFile](DataFile.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |