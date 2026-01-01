# CommandEventArgs.isValid Property

Parent Object: [CommandEventArgs](CommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. |

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. ```` ``` #include <Core/UserInterface/CommandEventArgs.h>  // Get the value of the property. boolean propertyValue = commandEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |