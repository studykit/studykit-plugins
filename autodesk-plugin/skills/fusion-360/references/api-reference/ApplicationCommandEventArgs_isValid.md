# ApplicationCommandEventArgs.isValid Property

Parent Object: [ApplicationCommandEventArgs](ApplicationCommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. |

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. ```` ``` #include <Core/UserInterface/ApplicationCommandEventArgs.h>  // Get the value of the property. boolean propertyValue = applicationCommandEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |