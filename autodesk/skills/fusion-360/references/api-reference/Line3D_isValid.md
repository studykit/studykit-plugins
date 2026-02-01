# Line3D.isValid Property

Parent Object: [Line3D](Line3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Line3D.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"line3D\_var" is a variable referencing a Line3D object. |

"line3D\_var" is a variable referencing a Line3D object. ```` ``` #include <Core/Geometry/Line3D.h>  // Get the value of the property. boolean propertyValue = line3D_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |