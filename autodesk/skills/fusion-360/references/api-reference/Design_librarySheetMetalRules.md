# Design.librarySheetMetalRules Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Gets the collection of sheet metal rules in the sheet metal rule library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<SheetMetalRules> propertyValue = design_var->librarySheetMetalRules(); ``` ```` |

## Property Value

This is a read only property whose value is a [SheetMetalRules](SheetMetalRules.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |