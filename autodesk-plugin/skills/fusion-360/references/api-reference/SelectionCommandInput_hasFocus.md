# SelectionCommandInput.hasFocus Property

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Gets and sets if this selection input has focus with respect to other selection inputs on the command dialog. Only one selection input on a dialog can have focus at a time, so setting hasFocus to true will remove the focus from the selection input that previously had focus. When a selection input has focus; any user selections will be added to that selection input, and the selection rules associated with that selection input will apply.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object.  ```` ``` # Get the value of the property. propertyValue = selectionCommandInput_var.hasFocus  # Set the value of the property. selectionCommandInput_var.hasFocus = propertyValue ``` ```` |

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object. ```` ``` #include <Core/UserInterface/SelectionCommandInput.h>  // Get the value of the property. boolean propertyValue = selectionCommandInput_var->hasFocus();  // Set the value of the property, where value_var is a boolean. bool returnValue = selectionCommandInput_var->hasFocus(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |