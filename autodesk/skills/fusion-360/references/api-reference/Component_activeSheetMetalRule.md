# Component.activeSheetMetalRule Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Gets and sets the active sheet metal rule. This can return null in the case where the component has never contained any sheet metal related data.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<SheetMetalRule> propertyValue = component_var->activeSheetMetalRule();  // Set the value of the property, where value_var is a SheetMetalRule. bool returnValue = component_var->activeSheetMetalRule(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SheetMetalRule](SheetMetalRule.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |