# GeometrySelection.warning Property

Parent Object: [GeometrySelection](GeometrySelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/GeometrySelection.h>

## Description

Gets the last warning string encountered after the selection was applied to a parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometrySelection\_var" is a variable referencing a GeometrySelection object. |

"geometrySelection\_var" is a variable referencing a GeometrySelection object. ```` ``` #include <Cam/GeometrySelections/GeometrySelection.h>  // Get the value of the property. string propertyValue = geometrySelection_var->warning(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |