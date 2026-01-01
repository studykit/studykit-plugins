# DropDownCommandInput.selectedItem Property

Parent Object: [DropDownCommandInput](DropDownCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownCommandInput.h>

## Description

Gets the item in the list that is currently selected. This can return null in the case where no item in the list has been selected. This should be ignored for CheckBoxDropDownStyle style drop-downs because multiple items can be selected and each LiteItem should be checked individually.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. |

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. ```` ``` #include <Core/UserInterface/DropDownCommandInput.h>  // Get the value of the property. Ptr<ListItem> propertyValue = dropDownCommandInput_var->selectedItem(); ``` ```` |

## Property Value

This is a read only property whose value is a [ListItem](ListItem.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |