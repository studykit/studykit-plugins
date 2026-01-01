# Decal.isValid Property

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a Decal object. |

"decal\_var" is a variable referencing a Decal object. ```` ``` #include <Fusion/Image/Decal.h>  // Get the value of the property. boolean propertyValue = decal_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |