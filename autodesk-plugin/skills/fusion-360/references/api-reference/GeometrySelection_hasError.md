# GeometrySelection.hasError Property

Parent Object: [GeometrySelection](GeometrySelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/GeometrySelection.h>

## Description

Gets if errors were encountered when applying the selection to a a parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometrySelection\_var" is a variable referencing a GeometrySelection object. |

"geometrySelection\_var" is a variable referencing a GeometrySelection object. ```` ``` #include <Cam/GeometrySelections/GeometrySelection.h>  // Get the value of the property. boolean propertyValue = geometrySelection_var->hasError(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |