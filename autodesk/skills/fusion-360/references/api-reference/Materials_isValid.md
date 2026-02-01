# Materials.isValid Property

Parent Object: [Materials](Materials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Materials.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materials\_var" is a variable referencing a Materials object. |

"materials\_var" is a variable referencing a Materials object. ```` ``` #include <Core/Materials/Materials.h>  // Get the value of the property. boolean propertyValue = materials_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |