# ButtonRowCommandInput.selectedItem Property

Parent Object: [ButtonRowCommandInput](ButtonRowCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ButtonRowCommandInput.h>

## Description

Gets the button in the row that is currently selected. This can return null in the case where no button in the row has been selected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"buttonRowCommandInput\_var" is a variable referencing a ButtonRowCommandInput object. |

"buttonRowCommandInput\_var" is a variable referencing a ButtonRowCommandInput object. ```` ``` #include <Core/UserInterface/ButtonRowCommandInput.h>  // Get the value of the property. Ptr<ListItem> propertyValue = buttonRowCommandInput_var->selectedItem(); ``` ```` |

## Property Value

This is a read only property whose value is a [ListItem](ListItem.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |