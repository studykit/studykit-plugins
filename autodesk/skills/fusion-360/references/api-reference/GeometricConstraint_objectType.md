# GeometricConstraint.objectType Property

Parent Object: [GeometricConstraint](GeometricConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraint\_var" is a variable referencing a GeometricConstraint object.  ```` ``` # Get the value of the property. propertyValue = geometricConstraint_var.objectType ``` ```` |

"geometricConstraint\_var" is a variable referencing a GeometricConstraint object. ```` ``` #include <Fusion/Sketch/GeometricConstraint.h>  // Get the value of the property. string propertyValue = geometricConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |