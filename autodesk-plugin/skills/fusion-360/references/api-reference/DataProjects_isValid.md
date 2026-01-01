# DataProjects.isValid Property

Parent Object: [DataProjects](DataProjects.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProjects.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProjects\_var" is a variable referencing a DataProjects object. |

"dataProjects\_var" is a variable referencing a DataProjects object. ```` ``` #include <Core/Dashboard/DataProjects.h>  // Get the value of the property. boolean propertyValue = dataProjects_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |