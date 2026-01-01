# DataFile.milestone Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

If the version this DataFile represents is a milestone, a Milestone object will be returned. If it's not a milestone, null is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object. |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. Ptr<Milestone> propertyValue = dataFile_var->milestone(); ``` ```` |

## Property Value

This is a read only property whose value is a [Milestone](Milestone.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |