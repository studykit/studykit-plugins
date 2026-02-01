# ListItems.addSeparator Method

Parent Object: [ListItems](ListItems.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItems.h>

## Description

Adds a separator to the list. This is not supported for button rows.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItems\_var" is a variable referencing a [ListItems](ListItems.htm) object.```` ``` returnValue = listItems_var.addSeparator(beforeIndex) ``` ```` |

"listItems\_var" is a variable referencing a [ListItems](ListItems.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ListItem](ListItem.htm) | Returns the new ListControlItem or null in the case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| beforeIndex | integer | The position of the item within the list. This value indicates the index of the current item to insert this new item just before. For example, a value of 0 will insert it before the first item in the list. An index of -1 will position the button at the bottom of the list. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |