# PatternElement.isSuppressed Property

Parent Object: [PatternElement](PatternElement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElement.h>

## Description

Gets and sets whether the element is suppressed or not. A value of True indicates it is suppressed

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElement\_var" is a variable referencing a PatternElement object. |

"patternElement\_var" is a variable referencing a PatternElement object. ```` ``` #include <Fusion/Features/PatternElement.h>  // Get the value of the property. boolean propertyValue = patternElement_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = patternElement_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |