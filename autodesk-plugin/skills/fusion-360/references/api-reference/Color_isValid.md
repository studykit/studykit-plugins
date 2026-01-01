# Color.isValid Property

Parent Object: [Color](Color.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Color.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"color\_var" is a variable referencing a Color object. |

"color\_var" is a variable referencing a Color object. ```` ``` #include <Core/Application/Color.h>  // Get the value of the property. boolean propertyValue = color_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |