# MaterialLibrary.isValid Property

Parent Object: [MaterialLibrary](MaterialLibrary.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibrary.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibrary\_var" is a variable referencing a MaterialLibrary object. |

"materialLibrary\_var" is a variable referencing a MaterialLibrary object. ```` ``` #include <Core/Materials/MaterialLibrary.h>  // Get the value of the property. boolean propertyValue = materialLibrary_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |