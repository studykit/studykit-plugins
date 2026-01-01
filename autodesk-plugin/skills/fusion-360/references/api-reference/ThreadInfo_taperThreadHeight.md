# ThreadInfo.taperThreadHeight Property

Parent Object: [ThreadInfo](ThreadInfo.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadInfo.h>

## Description

Returns the height of a tapered thread in centimeters. This is only valid when isTapered is true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadInfo\_var" is a variable referencing a ThreadInfo object. |

"threadInfo\_var" is a variable referencing a ThreadInfo object. ```` ``` #include <Fusion/Features/ThreadInfo.h>  // Get the value of the property. double propertyValue = threadInfo_var->taperThreadHeight(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |