# ConfigurationSheetMetalRuleCell.sheetMetalRule Property

Parent Object: [ConfigurationSheetMetalRuleCell](ConfigurationSheetMetalRuleCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleCell.h>

## Description

Gets and sets the sheet metal rule defined for this cell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleCell\_var" is a variable referencing a ConfigurationSheetMetalRuleCell object. |

"configurationSheetMetalRuleCell\_var" is a variable referencing a ConfigurationSheetMetalRuleCell object. ```` ``` #include <Fusion/Configurations/ConfigurationSheetMetalRuleCell.h>  // Get the value of the property. Ptr<SheetMetalRule> propertyValue = configurationSheetMetalRuleCell_var->sheetMetalRule();  // Set the value of the property, where value_var is a SheetMetalRule. bool returnValue = configurationSheetMetalRuleCell_var->sheetMetalRule(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SheetMetalRule](SheetMetalRule.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |