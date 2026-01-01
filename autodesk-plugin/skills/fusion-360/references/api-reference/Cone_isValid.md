# Cone.isValid Property

Parent Object: [Cone](Cone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cone.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cone\_var" is a variable referencing a Cone object. |

"cone\_var" is a variable referencing a Cone object. ```` ``` #include <Core/Geometry/Cone.h>  // Get the value of the property. boolean propertyValue = cone_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |