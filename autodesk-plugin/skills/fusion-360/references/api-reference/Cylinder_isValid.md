# Cylinder.isValid Property

Parent Object: [Cylinder](Cylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cylinder.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinder\_var" is a variable referencing a Cylinder object. |

"cylinder\_var" is a variable referencing a Cylinder object. ```` ``` #include <Core/Geometry/Cylinder.h>  // Get the value of the property. boolean propertyValue = cylinder_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |