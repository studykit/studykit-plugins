# FlatPatternComponent.activeSheetMetalRule Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Gets and sets the active sheet metal rule. This can return null in the case where the component has never contained any sheet metal related data.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. Ptr<SheetMetalRule> propertyValue = flatPatternComponent_var->activeSheetMetalRule();  // Set the value of the property, where value_var is a SheetMetalRule. bool returnValue = flatPatternComponent_var->activeSheetMetalRule(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SheetMetalRule](SheetMetalRule.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |