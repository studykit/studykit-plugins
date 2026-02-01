# DataProject.isValid Property

Parent Object: [DataProject](DataProject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProject.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProject\_var" is a variable referencing a DataProject object. |

"dataProject\_var" is a variable referencing a DataProject object. ```` ``` #include <Core/Dashboard/DataProject.h>  // Get the value of the property. boolean propertyValue = dataProject_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |