# ListItem.name Property

Parent Object: [ListItem](ListItem.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItem.h>

## Description

Gets or sets the name of this item as displayed in the list. If this control is a separator (isSeparator is true) or it's a button row, setting this property is ignored and getting it will return an empty string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItem\_var" is a variable referencing a ListItem object. |

"listItem\_var" is a variable referencing a ListItem object. ```` ``` #include <Core/UserInterface/ListItem.h>  // Get the value of the property. string propertyValue = listItem_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = listItem_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |