# CoincidentToSurfaceConstraint.objectType Property

Parent Object: [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentToSurfaceConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object.  ```` ``` # Get the value of the property. propertyValue = coincidentToSurfaceConstraint_var.objectType ``` ```` |

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentToSurfaceConstraint.h>  // Get the value of the property. string propertyValue = coincidentToSurfaceConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |