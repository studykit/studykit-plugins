# SheetMetalRule.kFactor Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

The K Factor value that is used when calculating the flat pattern. It must be a value between 0 and 1.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. double propertyValue = sheetMetalRule_var->kFactor();  // Set the value of the property, where value_var is a double. bool returnValue = sheetMetalRule_var->kFactor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |