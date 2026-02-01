# Ellipse3D.normal Property

Parent Object: [Ellipse3D](Ellipse3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse3D.h>

## Description

Gets the normal of the ellipse.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipse3D\_var" is a variable referencing an Ellipse3D object. |

"ellipse3D\_var" is a variable referencing an Ellipse3D object. ```` ``` #include <Core/Geometry/Ellipse3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = ellipse3D_var->normal(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |