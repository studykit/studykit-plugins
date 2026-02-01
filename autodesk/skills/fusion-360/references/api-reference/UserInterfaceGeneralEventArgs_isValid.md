# UserInterfaceGeneralEventArgs.isValid Property

Parent Object: [UserInterfaceGeneralEventArgs](UserInterfaceGeneralEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterfaceGeneralEventArgs\_var" is a variable referencing a UserInterfaceGeneralEventArgs object. |

"userInterfaceGeneralEventArgs\_var" is a variable referencing a UserInterfaceGeneralEventArgs object. ```` ``` #include <Core/UserInterface/UserInterfaceGeneralEventArgs.h>  // Get the value of the property. boolean propertyValue = userInterfaceGeneralEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |