# CurveSelection.objectType Property

Parent Object: [CurveSelection](CurveSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/CurveSelection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveSelection\_var" is a variable referencing a CurveSelection object.  ```` ``` # Get the value of the property. propertyValue = curveSelection_var.objectType ``` ```` |

"curveSelection\_var" is a variable referencing a CurveSelection object. ```` ``` #include <Cam/GeometrySelections/CurveSelection.h>  // Get the value of the property. string propertyValue = curveSelection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |