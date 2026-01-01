# SheetMetalRule.bendRadius Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

The interior radius of the bends. Use the returned SheetMetalRuleValue object to get and set the current value of the radius.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. Ptr<SheetMetalRuleValue> propertyValue = sheetMetalRule_var->bendRadius(); ``` ```` |

## Property Value

This is a read only property whose value is a [SheetMetalRuleValue](SheetMetalRuleValue.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |