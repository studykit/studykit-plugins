# PocketSelection.error Property

Parent Object: [PocketSelection](PocketSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketSelection.h>

## Description

Gets the last warning string encountered after the selection was applied to a parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketSelection\_var" is a variable referencing a PocketSelection object. |

"pocketSelection\_var" is a variable referencing a PocketSelection object. ```` ``` #include <Cam/GeometrySelections/PocketSelection.h>  // Get the value of the property. string propertyValue = pocketSelection_var->error(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |