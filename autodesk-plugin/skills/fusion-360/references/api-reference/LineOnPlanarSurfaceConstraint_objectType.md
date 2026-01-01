# LineOnPlanarSurfaceConstraint.objectType Property

Parent Object: [LineOnPlanarSurfaceConstraint](LineOnPlanarSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/LineOnPlanarSurfaceConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"lineOnPlanarSurfaceConstraint\_var" is a variable referencing a LineOnPlanarSurfaceConstraint object.  ```` ``` # Get the value of the property. propertyValue = lineOnPlanarSurfaceConstraint_var.objectType ``` ```` |

"lineOnPlanarSurfaceConstraint\_var" is a variable referencing a LineOnPlanarSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/LineOnPlanarSurfaceConstraint.h>  // Get the value of the property. string propertyValue = lineOnPlanarSurfaceConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |