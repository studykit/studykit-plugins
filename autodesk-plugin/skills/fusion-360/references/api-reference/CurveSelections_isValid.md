# CurveSelections.isValid Property

Parent Object: [CurveSelections](CurveSelections.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/CurveSelections.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveSelections\_var" is a variable referencing a CurveSelections object. |

"curveSelections\_var" is a variable referencing a CurveSelections object. ```` ``` #include <Cam/GeometrySelections/CurveSelections.h>  // Get the value of the property. boolean propertyValue = curveSelections_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |