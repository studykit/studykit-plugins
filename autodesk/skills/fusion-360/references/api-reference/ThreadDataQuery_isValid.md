# ThreadDataQuery.isValid Property

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a ThreadDataQuery object. |

"threadDataQuery\_var" is a variable referencing a ThreadDataQuery object. ```` ``` #include <Fusion/Features/ThreadDataQuery.h>  // Get the value of the property. boolean propertyValue = threadDataQuery_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |