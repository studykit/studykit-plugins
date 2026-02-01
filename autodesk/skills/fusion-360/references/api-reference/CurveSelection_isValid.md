# CurveSelection.isValid Property

Parent Object: [CurveSelection](CurveSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/CurveSelection.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveSelection\_var" is a variable referencing a CurveSelection object. |

"curveSelection\_var" is a variable referencing a CurveSelection object. ```` ``` #include <Cam/GeometrySelections/CurveSelection.h>  // Get the value of the property. boolean propertyValue = curveSelection_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |