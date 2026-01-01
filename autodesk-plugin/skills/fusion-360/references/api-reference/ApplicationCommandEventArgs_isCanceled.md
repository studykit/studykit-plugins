# ApplicationCommandEventArgs.isCanceled Property

Parent Object: [ApplicationCommandEventArgs](ApplicationCommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEventArgs.h>

## Description

Used during the commandStarting event to get or set if the command should be allowed to continue executing or be canceled. This defaults to false, which will allow the command to execute. Setting this to true will cancel the command and not begin the execution. This property should be ignored for all events besides the commandStarting event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. |

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. ```` ``` #include <Core/UserInterface/ApplicationCommandEventArgs.h>  // Get the value of the property. boolean propertyValue = applicationCommandEventArgs_var->isCanceled();  // Set the value of the property, where value_var is a boolean. bool returnValue = applicationCommandEventArgs_var->isCanceled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |