# SymmetryConstraint.objectType Property

Parent Object: [SymmetryConstraint](SymmetryConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SymmetryConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object.  ```` ``` # Get the value of the property. propertyValue = symmetryConstraint_var.objectType ``` ```` |

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object. ```` ``` #include <Fusion/Sketch/SymmetryConstraint.h>  // Get the value of the property. string propertyValue = symmetryConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |