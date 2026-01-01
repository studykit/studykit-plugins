# CircularPatternConstraint.objectType Property

Parent Object: [CircularPatternConstraint](CircularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object.  ```` ``` # Get the value of the property. propertyValue = circularPatternConstraint_var.objectType ``` ```` |

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraint.h>  // Get the value of the property. string propertyValue = circularPatternConstraint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |