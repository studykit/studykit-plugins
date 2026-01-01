# CommandEventArgs.isValidResult Property

Parent Object: [CommandEventArgs](CommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEventArgs.h>

## Description

Used during the commandStarting event to get or set that the result of preview is valid and the command can reuse the result when OK is hit. This property should be ignored for all events besides the executePreview event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. |

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. ```` ``` #include <Core/UserInterface/CommandEventArgs.h>  // Get the value of the property. boolean propertyValue = commandEventArgs_var->isValidResult();  // Set the value of the property, where value_var is a boolean. bool returnValue = commandEventArgs_var->isValidResult(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |