# ProfileLoop.isOuter Property

Parent Object: [ProfileLoop](ProfileLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoop.h>

## Description

Indicates if this is an outer or inner loop. Profiles always have one outer loop and have an zero to many inner loops defining voids.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileLoop\_var" is a variable referencing a ProfileLoop object. |

"profileLoop\_var" is a variable referencing a ProfileLoop object. ```` ``` #include <Fusion/Sketch/ProfileLoop.h>  // Get the value of the property. boolean propertyValue = profileLoop_var->isOuter(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |