# GeometricConstraints.objectType Property

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a GeometricConstraints object.  ```` ``` # Get the value of the property. propertyValue = geometricConstraints_var.objectType ``` ```` |

"geometricConstraints\_var" is a variable referencing a GeometricConstraints object. ```` ``` #include <Fusion/Sketch/GeometricConstraints.h>  // Get the value of the property. string propertyValue = geometricConstraints_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |