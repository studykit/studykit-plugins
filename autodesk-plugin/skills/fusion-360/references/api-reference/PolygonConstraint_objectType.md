# PolygonConstraint.objectType Property

Parent Object: [PolygonConstraint](PolygonConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PolygonConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object.  ```` ``` # Get the value of the property. propertyValue = polygonConstraint_var.objectType ``` ```` |

"polygonConstraint\_var" is a variable referencing a PolygonConstraint object. ```` ``` #include <Fusion/Sketch/PolygonConstraint.h>  // Get the value of the property. string propertyValue = polygonConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |