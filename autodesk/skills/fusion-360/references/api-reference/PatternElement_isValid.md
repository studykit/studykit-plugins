# PatternElement.isValid Property

Parent Object: [PatternElement](PatternElement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElement.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElement\_var" is a variable referencing a PatternElement object. |

"patternElement\_var" is a variable referencing a PatternElement object. ```` ``` #include <Fusion/Features/PatternElement.h>  // Get the value of the property. boolean propertyValue = patternElement_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |