# Command.isAutoExecute Property

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets and sets whether this command will automatically execute if no command inputs have been defined. If any command inputs have been created, the value of this property is ignored and the command dialog will be displayed and the command will execute when the user clicks 'OK'. if no command inputs have been defined and this is set to False, then the command will not execute but will remain running.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a Command object.  ```` ``` # Get the value of the property. propertyValue = command_var.isAutoExecute  # Set the value of the property. command_var.isAutoExecute = propertyValue ``` ```` |

"command\_var" is a variable referencing a Command object. ```` ``` #include <Core/UserInterface/Command.h>  // Get the value of the property. boolean propertyValue = command_var->isAutoExecute();  // Set the value of the property, where value_var is a boolean. bool returnValue = command_var->isAutoExecute(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version April 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |