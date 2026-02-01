# PerpendicularConstraint.objectType Property

Parent Object: [PerpendicularConstraint](PerpendicularConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"perpendicularConstraint\_var" is a variable referencing a PerpendicularConstraint object.  ```` ``` # Get the value of the property. propertyValue = perpendicularConstraint_var.objectType ``` ```` |

"perpendicularConstraint\_var" is a variable referencing a PerpendicularConstraint object. ```` ``` #include <Fusion/Sketch/PerpendicularConstraint.h>  // Get the value of the property. string propertyValue = perpendicularConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |