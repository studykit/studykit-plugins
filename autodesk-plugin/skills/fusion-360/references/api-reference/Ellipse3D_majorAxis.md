# Ellipse3D.majorAxis Property

Parent Object: [Ellipse3D](Ellipse3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse3D.h>

## Description

Gets and sets the major axis of the ellipse.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipse3D\_var" is a variable referencing an Ellipse3D object. |

"ellipse3D\_var" is a variable referencing an Ellipse3D object. ```` ``` #include <Core/Geometry/Ellipse3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = ellipse3D_var->majorAxis();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = ellipse3D_var->majorAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |