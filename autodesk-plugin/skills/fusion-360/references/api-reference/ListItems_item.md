# ListItems.item Method

Parent Object: [ListItems](ListItems.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItems.h>

## Description

Returns the specified check box list item using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItems\_var" is a variable referencing a [ListItems](ListItems.htm) object.```` ``` returnValue = listItems_var.item(index) ``` ```` |

"listItems\_var" is a variable referencing a [ListItems](ListItems.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ListItem](ListItem.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |