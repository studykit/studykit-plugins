# OffsetConstraint.objectType Property

Parent Object: [OffsetConstraint](OffsetConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object.  ```` ``` # Get the value of the property. propertyValue = offsetConstraint_var.objectType ``` ```` |

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. ```` ``` #include <Fusion/Sketch/OffsetConstraint.h>  // Get the value of the property. string propertyValue = offsetConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |