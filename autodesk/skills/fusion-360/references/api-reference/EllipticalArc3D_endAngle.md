# EllipticalArc3D.endAngle Property

Parent Object: [EllipticalArc3D](EllipticalArc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc3D.h>

## Description

Gets and sets the end angle of the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. |

"ellipticalArc3D\_var" is a variable referencing an EllipticalArc3D object. ```` ``` #include <Core/Geometry/EllipticalArc3D.h>  // Get the value of the property. double propertyValue = ellipticalArc3D_var->endAngle();  // Set the value of the property, where value_var is a double. bool returnValue = ellipticalArc3D_var->endAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |