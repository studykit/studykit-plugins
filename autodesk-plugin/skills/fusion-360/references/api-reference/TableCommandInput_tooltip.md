# TableCommandInput.tooltip Property

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. |

"tableCommandInput\_var" is a variable referencing a TableCommandInput object. ```` ``` #include <Core/UserInterface/TableCommandInput.h>  // Get the value of the property. string propertyValue = tableCommandInput_var->tooltip();  // Set the value of the property, where value_var is a string. bool returnValue = tableCommandInput_var->tooltip(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |