# ListItem.deleteMe Method

Parent Object: [ListItem](ListItem.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItem.h>

## Description

Deletes this item from the list. In cases where there is the concept of active item in the list, like with a DropDownCommandInput, this method will fail if the item you're attempting to delete is currently active. You need to make another item active first, and then you can delete the item.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItem\_var" is a variable referencing a [ListItem](ListItem.htm) object.```` ``` returnValue = listItem_var.deleteMe() ``` ```` |

"listItem\_var" is a variable referencing a [ListItem](ListItem.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |