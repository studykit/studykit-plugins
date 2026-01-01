# HorizontalPointsConstraint.objectType Property

Parent Object: [HorizontalPointsConstraint](HorizontalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/HorizontalPointsConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object.  ```` ``` # Get the value of the property. propertyValue = horizontalPointsConstraint_var.objectType ``` ```` |

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object. ```` ``` #include <Fusion/Sketch/HorizontalPointsConstraint.h>  // Get the value of the property. string propertyValue = horizontalPointsConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |