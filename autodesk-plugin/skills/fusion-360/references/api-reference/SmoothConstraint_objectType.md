# SmoothConstraint.objectType Property

Parent Object: [SmoothConstraint](SmoothConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SmoothConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"smoothConstraint\_var" is a variable referencing a SmoothConstraint object.  ```` ``` # Get the value of the property. propertyValue = smoothConstraint_var.objectType ``` ```` |

"smoothConstraint\_var" is a variable referencing a SmoothConstraint object. ```` ``` #include <Fusion/Sketch/SmoothConstraint.h>  // Get the value of the property. string propertyValue = smoothConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |