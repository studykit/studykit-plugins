# ThreadInfo.isValid Property

Parent Object: [ThreadInfo](ThreadInfo.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadInfo.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadInfo\_var" is a variable referencing a ThreadInfo object. |

"threadInfo\_var" is a variable referencing a ThreadInfo object. ```` ``` #include <Fusion/Features/ThreadInfo.h>  // Get the value of the property. boolean propertyValue = threadInfo_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |