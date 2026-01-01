# Polyline3D.isValid Property

Parent Object: [Polyline3D](Polyline3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline3D.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polyline3D\_var" is a variable referencing a Polyline3D object. |

"polyline3D\_var" is a variable referencing a Polyline3D object. ```` ``` #include <Core/Geometry/Polyline3D.h>  // Get the value of the property. boolean propertyValue = polyline3D_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |