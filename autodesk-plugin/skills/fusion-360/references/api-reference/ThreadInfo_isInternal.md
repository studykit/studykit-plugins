# ThreadInfo.isInternal Property

Parent Object: [ThreadInfo](ThreadInfo.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadInfo.h>

## Description

Returns and sets if the thread is an internal or external thread. A value of true indicates an internal thread. It defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadInfo\_var" is a variable referencing a ThreadInfo object. |

"threadInfo\_var" is a variable referencing a ThreadInfo object. ```` ``` #include <Fusion/Features/ThreadInfo.h>  // Get the value of the property. boolean propertyValue = threadInfo_var->isInternal();  // Set the value of the property, where value_var is a boolean. bool returnValue = threadInfo_var->isInternal(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |