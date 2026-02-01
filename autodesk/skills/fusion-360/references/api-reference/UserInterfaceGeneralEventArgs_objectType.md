# UserInterfaceGeneralEventArgs.objectType Property

Parent Object: [UserInterfaceGeneralEventArgs](UserInterfaceGeneralEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterfaceGeneralEventArgs\_var" is a variable referencing a UserInterfaceGeneralEventArgs object.  ```` ``` # Get the value of the property. propertyValue = userInterfaceGeneralEventArgs_var.objectType ``` ```` |

"userInterfaceGeneralEventArgs\_var" is a variable referencing a UserInterfaceGeneralEventArgs object. ```` ``` #include <Core/UserInterface/UserInterfaceGeneralEventArgs.h>  // Get the value of the property. string propertyValue = userInterfaceGeneralEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |