# SheetMetalRules.item Method

Parent Object: [SheetMetalRules](SheetMetalRules.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRules.h>

## Description

Function that returns the specified sheet metal rule using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sheetMetalRules\_var" is a variable referencing a [SheetMetalRules](SheetMetalRules.htm) object.```` ``` returnValue = sheetMetalRules_var.item(index) ``` ```` |

"sheetMetalRules\_var" is a variable referencing a [SheetMetalRules](SheetMetalRules.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SheetMetalRule](SheetMetalRule.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |