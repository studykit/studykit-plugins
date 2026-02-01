# SheetMetalRule.twoBendReliefSize Property

Parent Object: [SheetMetalRule](SheetMetalRule.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRule.h>

## Description

The relief size used when two bends meet in the flat pattern and the relief shape is round or square. Use the returned SheetMetalRuleValue object to get and set the current value of the relief size.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. |

"sheetMetalRule\_var" is a variable referencing a SheetMetalRule object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRule.h>  // Get the value of the property. Ptr<SheetMetalRuleValue> propertyValue = sheetMetalRule_var->twoBendReliefSize(); ``` ```` |

## Property Value

This is a read only property whose value is a [SheetMetalRuleValue](SheetMetalRuleValue.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |