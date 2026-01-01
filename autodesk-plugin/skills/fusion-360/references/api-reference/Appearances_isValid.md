# Appearances.isValid Property

Parent Object: [Appearances](Appearances.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Appearances.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearances\_var" is a variable referencing an Appearances object. |

"appearances\_var" is a variable referencing an Appearances object. ```` ``` #include <Core/Materials/Appearances.h>  // Get the value of the property. boolean propertyValue = appearances_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |