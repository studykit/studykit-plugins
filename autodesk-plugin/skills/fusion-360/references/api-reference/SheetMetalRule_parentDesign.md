# SheetMetalRule.parentDesign Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

Returns the parent design for a sheet metal rule in a design or it returns null if the sheet metal rule is in the library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. Ptr<Design> propertyValue = sheetMetalRule_var->parentDesign(); ``` ```` |

## Property Value

This is a read only property whose value is a [Design](Design.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |