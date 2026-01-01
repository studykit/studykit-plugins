# SheetMetalRuleValue.value Property

Parent Object: [SheetMetalRuleValue](SheetMetalRuleValue.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRuleValue.h>

## Description

Gets and sets the value of the sheet metal rule value in centimeters. Setting this value will create a new expression that is equivalent to the new value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRuleValue\_var" is a variable referencing a SheetMetalRuleValue object. |

"sheetMetalRuleValue\_var" is a variable referencing a SheetMetalRuleValue object. ```` ``` #include <Fusion/SheetMetal/SheetMetalRuleValue.h>  // Get the value of the property. double propertyValue = sheetMetalRuleValue_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = sheetMetalRuleValue_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |