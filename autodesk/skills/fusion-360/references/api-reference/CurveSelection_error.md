# CurveSelection.error Property

Parent Object: [CurveSelection](CurveSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/CurveSelection.h>

## Description

Gets the last warning string encountered after the selection was applied to a parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveSelection\_var" is a variable referencing a CurveSelection object. |

"curveSelection\_var" is a variable referencing a CurveSelection object. ```` ``` #include <Cam/GeometrySelections/CurveSelection.h>  // Get the value of the property. string propertyValue = curveSelection_var->error(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |