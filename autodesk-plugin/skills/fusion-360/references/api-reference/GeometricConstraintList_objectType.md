# GeometricConstraintList.objectType Property

Parent Object: [GeometricConstraintList](GeometricConstraintList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraintList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraintList\_var" is a variable referencing a GeometricConstraintList object.  ```` ``` # Get the value of the property. propertyValue = geometricConstraintList_var.objectType ``` ```` |

"geometricConstraintList\_var" is a variable referencing a GeometricConstraintList object. ```` ``` #include <Fusion/Sketch/GeometricConstraintList.h>  // Get the value of the property. string propertyValue = geometricConstraintList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |