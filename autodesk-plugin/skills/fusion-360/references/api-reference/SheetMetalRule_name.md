# SheetMetalRule.name Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

The name of the sheet metal rule. When setting the name, it should be unique with respect to other sheet metal rules in the design or library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. string propertyValue = sheetMetalRule_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = sheetMetalRule_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |