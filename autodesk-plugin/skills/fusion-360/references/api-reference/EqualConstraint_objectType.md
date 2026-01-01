# EqualConstraint.objectType Property

Parent Object: [EqualConstraint](EqualConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/EqualConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"equalConstraint\_var" is a variable referencing an EqualConstraint object.  ```` ``` # Get the value of the property. propertyValue = equalConstraint_var.objectType ``` ```` |

"equalConstraint\_var" is a variable referencing an EqualConstraint object. ```` ``` #include <Fusion/Sketch/EqualConstraint.h>  // Get the value of the property. string propertyValue = equalConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |