# ThreadInfo.taperAngle Property

Parent Object: [ThreadInfo](ThreadInfo.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadInfo.h>

## Description

Returns the angle of the tapered thread in centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadInfo\_var" is a variable referencing a ThreadInfo object.  ```` ``` # Get the value of the property. propertyValue = threadInfo_var.taperAngle ``` ```` |

"threadInfo\_var" is a variable referencing a ThreadInfo object. ```` ``` #include <Fusion/Features/ThreadInfo.h>  // Get the value of the property. double propertyValue = threadInfo_var->taperAngle(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |