# GeometrySelection.objectType Property

Parent Object: [GeometrySelection](GeometrySelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/GeometrySelection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometrySelection\_var" is a variable referencing a GeometrySelection object.  ```` ``` # Get the value of the property. propertyValue = geometrySelection_var.objectType ``` ```` |

"geometrySelection\_var" is a variable referencing a GeometrySelection object. ```` ``` #include <Cam/GeometrySelections/GeometrySelection.h>  // Get the value of the property. string propertyValue = geometrySelection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |