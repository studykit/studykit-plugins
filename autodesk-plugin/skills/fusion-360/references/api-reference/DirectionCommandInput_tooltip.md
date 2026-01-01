# DirectionCommandInput.tooltip Property

Parent Object: [DirectionCommandInput](DirectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DirectionCommandInput.h>

## Description

Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"directionCommandInput\_var" is a variable referencing a DirectionCommandInput object. |

"directionCommandInput\_var" is a variable referencing a DirectionCommandInput object. ```` ``` #include <Core/UserInterface/DirectionCommandInput.h>  // Get the value of the property. string propertyValue = directionCommandInput_var->tooltip();  // Set the value of the property, where value_var is a string. bool returnValue = directionCommandInput_var->tooltip(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |