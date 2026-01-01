# PatternElements.isValid Property

Parent Object: [PatternElements](PatternElements.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElements.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElements\_var" is a variable referencing a PatternElements object. |

"patternElements\_var" is a variable referencing a PatternElements object. ```` ``` #include <Fusion/Features/PatternElements.h>  // Get the value of the property. boolean propertyValue = patternElements_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |