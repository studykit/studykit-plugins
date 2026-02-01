# ListItem.icon Property

Parent Object: [ListItem](ListItem.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItem.h>

## Description

Gets or sets the location for the icon file used for this item in the list. This is the path to a directory that contains the image files associated with this item. This is only valid when this is a standard list or button row and is ignored for check box lists, radio control lists, and radio button groups.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItem\_var" is a variable referencing a ListItem object. |

"listItem\_var" is a variable referencing a ListItem object. ```` ``` #include <Core/UserInterface/ListItem.h>  // Get the value of the property. string propertyValue = listItem_var->icon();  // Set the value of the property, where value_var is a string. bool returnValue = listItem_var->icon(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |