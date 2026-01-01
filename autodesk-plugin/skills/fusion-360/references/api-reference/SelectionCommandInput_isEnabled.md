# SelectionCommandInput.isEnabled Property

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object.  ```` ``` # Get the value of the property. propertyValue = selectionCommandInput_var.isEnabled  # Set the value of the property. selectionCommandInput_var.isEnabled = propertyValue ``` ```` |

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object. ```` ``` #include <Core/UserInterface/SelectionCommandInput.h>  // Get the value of the property. boolean propertyValue = selectionCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = selectionCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |