# GeometricConstraintList.isValid Property

Parent Object: [GeometricConstraintList](GeometricConstraintList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraintList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraintList\_var" is a variable referencing a GeometricConstraintList object. |

"geometricConstraintList\_var" is a variable referencing a GeometricConstraintList object. ```` ``` #include <Fusion/Sketch/GeometricConstraintList.h>  // Get the value of the property. boolean propertyValue = geometricConstraintList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |