# ChainSelection.warning Property

Parent Object: [ChainSelection](ChainSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ChainSelection.h>

## Description

Gets the last warning string encountered after the selection was applied to a parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chainSelection\_var" is a variable referencing a ChainSelection object. |

"chainSelection\_var" is a variable referencing a ChainSelection object. ```` ``` #include <Cam/GeometrySelections/ChainSelection.h>  // Get the value of the property. string propertyValue = chainSelection_var->warning(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |