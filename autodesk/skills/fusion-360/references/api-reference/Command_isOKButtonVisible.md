# Command.isOKButtonVisible Property

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Specifies if the OK button is visible or not. If set to false then the OK button is removed and the "CANCEL" button text changes to "CLOSE". You can override the default button text using the cancelButtonText property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a Command object. |

"command\_var" is a variable referencing a Command object. ```` ``` #include <Core/UserInterface/Command.h>  // Get the value of the property. boolean propertyValue = command_var->isOKButtonVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = command_var->isOKButtonVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |