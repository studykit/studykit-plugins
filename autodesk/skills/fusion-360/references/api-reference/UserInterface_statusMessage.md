# UserInterface.statusMessage Property

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Gets and sets the current message displayed in the lower-right corner of the Fusion window. This is useful when displaying progress information to the user for the current process. Set the value to an empty string to remove the message. The lifetime of your message is indeterminant because Fusion uses the same field to display messages.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a UserInterface object.  ```` ``` # Get the value of the property. propertyValue = userInterface_var.statusMessage  # Set the value of the property. userInterface_var.statusMessage = propertyValue ``` ```` |

"userInterface\_var" is a variable referencing a UserInterface object. ```` ``` #include <Core/UserInterface/UserInterface.h>  // Get the value of the property. string propertyValue = userInterface_var->statusMessage();  // Set the value of the property, where value_var is a string. bool returnValue = userInterface_var->statusMessage(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |