# ThreadDataQuery.isTapered Property

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

Returns if this ThreadDataQuery was created to query for standard or tapered threads.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadDataQuery\_var" is a variable referencing a ThreadDataQuery object. |

"threadDataQuery\_var" is a variable referencing a ThreadDataQuery object. ```` ``` #include <Fusion/Features/ThreadDataQuery.h>  // Get the value of the property. boolean propertyValue = threadDataQuery_var->isTapered(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |