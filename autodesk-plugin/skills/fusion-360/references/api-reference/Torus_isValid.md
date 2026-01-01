# Torus.isValid Property

Parent Object: [Torus](Torus.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Torus.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torus\_var" is a variable referencing a Torus object. |

"torus\_var" is a variable referencing a Torus object. ```` ``` #include <Core/Geometry/Torus.h>  // Get the value of the property. boolean propertyValue = torus_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |