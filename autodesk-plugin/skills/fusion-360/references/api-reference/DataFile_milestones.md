# DataFile.milestones Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Returns a collection of Milestones associated with all versions of this DataFile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object. |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. Ptr<Milestones> propertyValue = dataFile_var->milestones(); ``` ```` |

## Property Value

This is a read only property whose value is a [Milestones](Milestones.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |