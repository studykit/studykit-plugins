# SheetMetalRules.itemByName Method

Parent Object: [SheetMetalRules](SheetMetalRules.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRules.h>

## Description

Function that returns the specified sheet metal rule using the name of the rule.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRules\_var" is a variable referencing a [SheetMetalRules](SheetMetalRules.htm) object.```` ``` returnValue = sheetMetalRules_var.itemByName(name) ``` ```` |

"sheetMetalRules\_var" is a variable referencing a [SheetMetalRules](SheetMetalRules.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SheetMetalRule](SheetMetalRule.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the rule within the collection to return. This is the name seen in the Sheet Metal Rules dialog. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |