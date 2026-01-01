# CommandEventArgs.executeFailedMessage Property

Parent Object: [CommandEventArgs](CommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEventArgs.h>

## Description

Used during the execute event to get or set a description of an execute failure. This property should be ignored for all events besides the Execute event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. |

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. ```` ``` #include <Core/UserInterface/CommandEventArgs.h>  // Get the value of the property. string propertyValue = commandEventArgs_var->executeFailedMessage();  // Set the value of the property, where value_var is a string. bool returnValue = commandEventArgs_var->executeFailedMessage(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |