# EllipticalCone.minorRadius Property

Parent Object: [EllipticalCone](EllipticalCone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCone.h>

## Description

Gets and sets the minor radius of the ellipse that defines the cone.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCone\_var" is a variable referencing an EllipticalCone object. |

"ellipticalCone\_var" is a variable referencing an EllipticalCone object. ```` ``` #include <Core/Geometry/EllipticalCone.h>  // Get the value of the property. double propertyValue = ellipticalCone_var->minorRadius();  // Set the value of the property, where value_var is a double. bool returnValue = ellipticalCone_var->minorRadius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |