# EllipticalArc2D.objectType Property

Parent Object: [EllipticalArc2D](EllipticalArc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc2D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object.  ```` ``` # Get the value of the property. propertyValue = ellipticalArc2D_var.objectType ``` ```` |

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. ```` ``` #include <Core/Geometry/EllipticalArc2D.h>  // Get the value of the property. string propertyValue = ellipticalArc2D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |