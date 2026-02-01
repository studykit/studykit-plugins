# ComponentList.item Method

Parent Object: [ComponentList](ComponentList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ComponentList.h>

## Description

Function that returns the specified component using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"componentList\_var" is a variable referencing a [ComponentList](ComponentList.htm) object.```` ``` returnValue = componentList_var.item(index) ``` ```` |

"componentList\_var" is a variable referencing a [ComponentList](ComponentList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Component](Component.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |