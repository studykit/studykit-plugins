# SelectionCommandInput.tooltip Property

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object. |

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object. ```` ``` #include <Core/UserInterface/SelectionCommandInput.h>  // Get the value of the property. string propertyValue = selectionCommandInput_var->tooltip();  // Set the value of the property, where value_var is a string. bool returnValue = selectionCommandInput_var->tooltip(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |