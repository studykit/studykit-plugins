# ListItem.parentList Property

Parent Object: [ListItem](ListItem.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItem.h>

## Description

Gets the parent CheckBoxListControlDefinition or object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItem\_var" is a variable referencing a ListItem object. |

"listItem\_var" is a variable referencing a ListItem object. ```` ``` #include <Core/UserInterface/ListItem.h>  // Get the value of the property. Ptr<Base> propertyValue = listItem_var->parentList(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |