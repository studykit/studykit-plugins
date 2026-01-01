# PerpendicularToSurfaceConstraint.objectType Property

Parent Object: [PerpendicularToSurfaceConstraint](PerpendicularToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"perpendicularToSurfaceConstraint\_var" is a variable referencing a PerpendicularToSurfaceConstraint object.  ```` ``` # Get the value of the property. propertyValue = perpendicularToSurfaceConstraint_var.objectType ``` ```` |

"perpendicularToSurfaceConstraint\_var" is a variable referencing a PerpendicularToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>  // Get the value of the property. string propertyValue = perpendicularToSurfaceConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |