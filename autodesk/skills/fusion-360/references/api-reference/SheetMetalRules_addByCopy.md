# SheetMetalRules.addByCopy Method

Parent Object: [SheetMetalRules](SheetMetalRules.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRules.h>

## Description

Creates a new sheet metal rule by copying an existing rule. The new rule can then be edited to define the rule characteristics you want.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRules\_var" is a variable referencing a [SheetMetalRules](SheetMetalRules.htm) object.```` ``` returnValue = sheetMetalRules_var.addByCopy(existingSheetMetalRule, name) ``` ```` |

"sheetMetalRules\_var" is a variable referencing a [SheetMetalRules](SheetMetalRules.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SheetMetalRule](SheetMetalRule.htm) | Returns the new SheetMetalRule object or will assert in the case where it fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| existingSheetMetalRule | [SheetMetalRule](SheetMetalRule.htm) | The existing SheetMetalRule object you want to copy. This can be a rule from the library or the design. |
| name | string | The name to assign to the new sheet metal rule. This name must be unique with respect to other sheet metal rules in the design or library it's created in. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |