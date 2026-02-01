# PocketSelection.isSelectingSamePlaneFaces Property

Parent Object: [PocketSelection](PocketSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketSelection.h>

## Description

True if all planar faces lying in the same plane as the selected face should be automatically selected as well. False by default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketSelection\_var" is a variable referencing a PocketSelection object. |

"pocketSelection\_var" is a variable referencing a PocketSelection object. ```` ``` #include <Cam/GeometrySelections/PocketSelection.h>  // Get the value of the property. boolean propertyValue = pocketSelection_var->isSelectingSamePlaneFaces();  // Set the value of the property, where value_var is a boolean. bool returnValue = pocketSelection_var->isSelectingSamePlaneFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |