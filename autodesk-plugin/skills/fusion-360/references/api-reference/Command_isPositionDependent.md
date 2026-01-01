# Command.isPositionDependent Property

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

When working in a parametric design in Fusion and you move any occurrences, those move operations are pending and aren't captured until you use the "Capture Position" command from the POSITION panel or use the "Revert" command from the same panel to move them all back to their original positions. If the design is in a pending situation and you run a command like "Create Sketch", a dialog appears asking if you want to capture the current position or not before continuing. This is because the creation of a sketch can be dependent on the current positions of occurrences in the design. Other commands, like "Fillet", depend directly on model geometry and do not rely on occurrence positions so running the Fillet command does not display the dialog and does not affect the pending state of the occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a Command object.  ```` ``` # Get the value of the property. propertyValue = command_var.isPositionDependent  # Set the value of the property. command_var.isPositionDependent = propertyValue ``` ```` |

"command\_var" is a variable referencing a Command object. ```` ``` #include <Core/UserInterface/Command.h>  // Get the value of the property. boolean propertyValue = command_var->isPositionDependent();  // Set the value of the property, where value_var is a boolean. bool returnValue = command_var->isPositionDependent(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |