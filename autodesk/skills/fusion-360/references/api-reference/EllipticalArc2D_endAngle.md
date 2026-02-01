# EllipticalArc2D.endAngle Property

Parent Object: [EllipticalArc2D](EllipticalArc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc2D.h>

## Description

Gets and sets the end angle of the elliptical arc in radians, where 0 is along the major axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. |

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. ```` ``` #include <Core/Geometry/EllipticalArc2D.h>  // Get the value of the property. double propertyValue = ellipticalArc2D_var->endAngle();  // Set the value of the property, where value_var is a double. bool returnValue = ellipticalArc2D_var->endAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |