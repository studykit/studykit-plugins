# ListItem.isSelected Property

Parent Object: [ListItem](ListItem.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItem.h>

## Description

Gets or sets whether this item is selected. If the item is being displayed as a check box, this controls whether it is checked or not. If it's a drop-down list or button row it controls whether this is the single selected item. Setting a drop-down list, button row item, or radio button from a group to be selected will unselect the currently selected item. For a standard list, this will get or set the single item currently selected. For a separator, setting this property is ignored and it will always return false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItem\_var" is a variable referencing a ListItem object. |

"listItem\_var" is a variable referencing a ListItem object. ```` ``` #include <Core/UserInterface/ListItem.h>  // Get the value of the property. boolean propertyValue = listItem_var->isSelected();  // Set the value of the property, where value_var is a boolean. bool returnValue = listItem_var->isSelected(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |