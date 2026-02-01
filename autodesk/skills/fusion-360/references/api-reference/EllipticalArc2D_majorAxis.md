# EllipticalArc2D.majorAxis Property

Parent Object: [EllipticalArc2D](EllipticalArc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc2D.h>

## Description

Gets and sets the major axis of the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. |

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. ```` ``` #include <Core/Geometry/EllipticalArc2D.h>  // Get the value of the property. Ptr<Vector2D> propertyValue = ellipticalArc2D_var->majorAxis();  // Set the value of the property, where value_var is a Vector2D. bool returnValue = ellipticalArc2D_var->majorAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector2D](Vector2D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |