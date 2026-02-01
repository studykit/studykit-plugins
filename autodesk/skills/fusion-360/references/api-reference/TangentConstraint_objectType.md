# TangentConstraint.objectType Property

Parent Object: [TangentConstraint](TangentConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/TangentConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentConstraint\_var" is a variable referencing a TangentConstraint object.  ```` ``` # Get the value of the property. propertyValue = tangentConstraint_var.objectType ``` ```` |

"tangentConstraint\_var" is a variable referencing a TangentConstraint object. ```` ``` #include <Fusion/Sketch/TangentConstraint.h>  // Get the value of the property. string propertyValue = tangentConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |