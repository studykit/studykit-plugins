# ConcentricConstraint.objectType Property

Parent Object: [ConcentricConstraint](ConcentricConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ConcentricConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object.  ```` ``` # Get the value of the property. propertyValue = concentricConstraint_var.objectType ``` ```` |

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object. ```` ``` #include <Fusion/Sketch/ConcentricConstraint.h>  // Get the value of the property. string propertyValue = concentricConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |