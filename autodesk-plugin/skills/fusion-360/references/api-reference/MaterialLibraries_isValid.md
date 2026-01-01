# MaterialLibraries.isValid Property

Parent Object: [MaterialLibraries](MaterialLibraries.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibraries.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibraries\_var" is a variable referencing a MaterialLibraries object. |

"materialLibraries\_var" is a variable referencing a MaterialLibraries object. ```` ``` #include <Core/Materials/MaterialLibraries.h>  // Get the value of the property. boolean propertyValue = materialLibraries_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |